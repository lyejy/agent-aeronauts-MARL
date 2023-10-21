import pulp
import random


# Parameters
num_requests = 15000
num_timeslots_per_day = 288
num_days = 182 
total_timeslots = num_requests * num_timeslots_per_day
capacity = 10  # Fixed capacity for each timeslot
movements = 5  # Maximum allowed distance from the original timeslot


# Constants for original arrival and departure slots
original_arrival = {i: random.randint(0, total_timeslots - 1) for i in range(num_requests)}
original_departure = {i: (original_arrival[i] + 7) % total_timeslots for i in range(num_requests)}


# Create a PuLP problem
problem = pulp.LpProblem("FlightAssignment", pulp.LpMinimize)

# Binary decision variables: 
# arrival[i, j] is 1 if request i arrives at timeslot j
# departure[i, j] is 1 if request i departs from timeslot j
arrival = pulp.LpVariable.dicts("Arrival", ((i, j) for i in range(num_requests) for j in range(total_timeslots)), cat=pulp.LpBinary)
departure = pulp.LpVariable.dicts("Departure", ((i, j) for i in range(num_requests) for j in range(total_timeslots)), cat=pulp.LpBinary)

# Constraints
# Each request arrives at exactly one timeslot
for i in range(num_requests):
    problem += pulp.lpSum(arrival[i, j] for j in range(total_timeslots)) == 1

# Each request departs from exactly one timeslot
for i in range(num_requests):
    problem += pulp.lpSum(departure[i, j] for j in range(total_timeslots)) == 1

# Capacity constraint for each timeslot
for j in range(total_timeslots):
    problem += pulp.lpSum(arrival[i, j] for i in range(num_requests)) + pulp.lpSum(departure[i, j] for i in range(num_requests)) <= capacity

# Ensure that the departure and arrival timeslots for a flight request are not the same 
for i in range(num_requests):
    for j in range(total_timeslots):
        problem += arrival[i, j] + departure[i, j] <= 1  # A request can't arrive and depart from the same timeslot

# Ensure that the updated slot is at most a certain number of slots away  
for i in range(num_requests):
    for j in range(total_timeslots):
        problem += arrival[i, j] * abs(original_arrival[i] - j) <= movements//2 

for i in range(num_requests):
    for j in range(total_timeslots):
        problem += departure[i, j] * abs(original_departure[i] - j) <= movements//2 


#Minimize the number of timeslots between the original timeslot and the updated timeslot 
problem += pulp.lpSum(
    arrival[i, j] * abs(original_arrival[i] - j) + departure[i, j] * abs(original_departure[i] - j)
    for i in range(num_requests)
    for j in range(total_timeslots)
)


# Solve the problem
problem.solve()

if problem.status == pulp.LpStatusOptimal:
    # Print the optimal assignments
    for i in range(num_requests):
        arrival_slot = next(j for j in range(total_timeslots) if pulp.value(arrival[i, j]) == 1)
        departure_slot = next(j for j in range(total_timeslots) if pulp.value(departure[i, j]) == 1)
        print(f"Request {i} arrives at timeslot {arrival_slot} and departs from timeslot {departure_slot}")

    # Print the total distance
    total_distance = sum(abs(arrival_slot - departure_slot) for i in range(num_requests))
    print(f"Total distance: {total_distance}")
else:
    # Print number of remaining requests violating constraints 
    print("No optimal solution found.")
