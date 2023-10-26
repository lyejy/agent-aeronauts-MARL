from pulp import LpProblem, LpVariable, lpSum, LpMaximize, LpMinimize
from scipy.stats import truncnorm
import numpy as np
import random

def get_truncated_normal(mean, sd, low, upp):
    return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

def one_hot_encode_airport(airport, num_airports):
    encoding = np.zeros(num_airports)
    encoding[airport] = 1
    return encoding

def generate_info_arv(requests):
    ts_arv = np.empty(shape=(len(requests),), dtype='object')
    start_date_arv = np.empty(shape=(len(requests),), dtype='object')
    for i in range(len(requests)):
        ts_arv[i] = requests[i][1] + requests[i][5]/5
        if ts_arv[i] > 287:
            ts_arv[i] = ts_arv[i] - 287
            start_date_arv[i] = requests[i][2] + 1
        else:
            start_date_arv[i] = requests[i][2]
    return ts_arv, start_date_arv

def get_ts_per_year(ts_slots, dates):
    result = np.empty(shape=(len(ts_slots),), dtype='object')
    for i in range(len(ts_slots)):
        result[i] = dates[i] * 287 + ts_slots[i]
    return result 

#Modify the distribution based on historical data later:
def generate_scenario(number_of_requests, num_airports):
    
    #number_of_requests = 15000
    ts_72 = get_truncated_normal(mean=72, sd=12, low=0, upp=287).rvs(int(round(number_of_requests/2)))
    ts_72 = np.round(ts_72)

    ts_216 = get_truncated_normal(mean=216, sd=12, low=0, upp=287).rvs(int(round(number_of_requests/2)))
    ts_216 = np.round(ts_216)

    ts_dep = np.concatenate((ts_72, ts_216))
    ts_dep = ts_dep.astype(int)

    #Generate departure dates:
    start_date_dep = np.random.randint(low = 0, high=146, size=number_of_requests) #146 because period is 182 days and we consider series which span at least 5 weeks (+35 days)

    #Generate index for requests:
    index = np.array(list(range(number_of_requests)))

    origin_airport = np.empty(shape=(number_of_requests,), dtype='object')
    destination_airport = np.empty(shape=(number_of_requests,), dtype='object')
    for i in range(number_of_requests):
        #Generate origin (0 and 1 are two considered origin airports, 2 represent other airports, encoded in one-hot vector):
        _org_airport = one_hot_encode_airport(random.randint(0,1), num_airports)
        _org_airport_list = _org_airport.tolist()
        origin_airport[i] = _org_airport_list
        #Generate destination (the destination will be different with the origin):
        _dest_airport = _org_airport.copy()
        while np.array_equal(_dest_airport, _org_airport):
            np.random.shuffle(_dest_airport)
        _dest_airport_list = _dest_airport.tolist()
        destination_airport[i] = _dest_airport_list

    #Generate flying time (assume between airport 0 and 1 is 2 hour, 0 to 2 and 1 to 2 is arbitrary):
    fly_time = np.empty(shape=(number_of_requests,), dtype='object')
    for i in range (number_of_requests):
        if origin_airport[i] == list([1.0, 0.0]) and destination_airport[i] == list([0.0, 1.0]):
            fly_time[i] = 120
        elif origin_airport[i] == list([0.0, 1.0]) and destination_airport[i] == list([1.0, 0.0]):
            fly_time[i] = random.choice([60, 120, 180])
        else:
            fly_time[i] = random.choice([60, 120, 180])
  
    requests = np.stack((index, ts_dep, start_date_dep, origin_airport, destination_airport, fly_time), axis=1)

    #Generate full info for the arv side:
    ts_arv, start_date_arv = generate_info_arv(requests)

    # Define requests_full as dtype object
    # requests_full = np.stack((index, ts_dep, start_date_dep, num_of_weeks, date_seq_dep, origin_airport, destination_airport, fly_time, status_cap_dep, ts_arv, start_date_arv, date_seq_arv, status_cap_arv), axis=1)
    num_entries = len(index)  # Given that 'index' is defined using np.array(list(range(number_of_requests)))
    # Create an empty array of the desired shape with dtype=object
    requests_full = np.empty((num_entries, 10), dtype=object)
    # Fill the array
    ts_dep = get_ts_per_year(ts_dep, start_date_dep)
    ts_arv = get_ts_per_year(ts_arv, start_date_arv)

    data = [index, ts_dep, origin_airport, ts_arv, destination_airport]
    for i, column_data in enumerate(data):
        requests_full[:, i] = column_data

    return requests_full



num_airports = 3
number_of_requests = 100
flight_requests = generate_scenario(number_of_requests, num_airports)
time_slots = 287 * 182 # Time slots and their characteristics
max_change = 5 
time_slot_cap = 1
 
# Create a MILP problem
model = LpProblem(name="Flight_Scheduling", sense=LpMinimize)

# Create binary decision variables for each flight request and each possible change in time slots
x = {(req, slot_change): LpVariable(name=f"x_{req}_{slot_change}", cat="Binary")
     for req in range(number_of_requests) for slot_change in range(-max_change//2, max_change//2)}

# Objective function: minimize the number of slot changes
model += lpSum(x[req, slot_change] for req in range(number_of_requests) for slot_change in range(-max_change//2, max_change//2))

# Constraints
for airport in range(num_airports):
    for slot in range(time_slots):
        # Demand for each time slot at each airport should be less than the capacity
        model += lpSum(x[req, slot_change] for req in range(number_of_requests)
                       for slot_change in range(-max_change//2, max_change//2)
                       if (flight_requests[req][2] == airport and flight_requests[req][1] + slot_change == slot)
                       or (flight_requests[req][4] == airport and flight_requests[req][3] + slot_change == slot)) <= time_slot_cap
      
        
for req in range(number_of_requests):
    model += lpSum(x[req,slot_change] for slot_change in range(-max_change//2, max_change//2)) == 1

# Solve the MILP problem
model.solve()

slot_changes = []

# Iterate through the decision variables and check if they are equal to 1
for req in range(number_of_requests):
    for slot_change in range(-max_change//2, max_change//2):
        if x[req, slot_change].varValue == 1:
            slot_changes.append((req, slot_change))

# Print the slot changes
for req, slot_change in slot_changes:
    print(f"Flight Request {req}: Change by {slot_change} time slots from dep slot {flight_requests[req][1]} and arv slot {flight_requests[req][3]}")

print("Objective Value:", model.objective.value())
