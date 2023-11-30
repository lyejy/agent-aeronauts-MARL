from pulp import *
from scipy.stats import truncnorm
import numpy as np
import random

num_airports = 2
number_of_requests = 1000
flight_requests = generate_scenario(number_of_requests, num_airports)
time_slots = 288 # Time slots and their characteristics
capacity_per_slot = 6
max_movements = 6
arrival_departure = [0,1]

# Create a MILP problem
problem = LpProblem(name="Flight_Scheduling", sense=LpMinimize)

# Creating binary decision variables for each flight request, airport, and arrival/departure slot
x = {(req, flight_type, airport, slot): LpVariable(
        name=f"x_{req}_{airport}_{slot}_{arrival_departure}", cat="Binary")
     for req in range(number_of_requests)
     for flight_type in arrival_departure #0 - departure, 1 - arrival 
     for airport in range(num_airports)
     for slot in range(time_slots)}

# Objective function - minimises the total absolute difference between the requested and allocated time interval
problem += lpSum(abs(sum(x[req, flight_type, airport]) - flight_requests[req][flight_type]) * x[req, flight_type, airport,0]  for req in range(number_of_requests) for flight_type in arrival_departure for airport in range(num_airports))

# Constraints -
# ensure that only one slot is assigned to a flight and no flight can arrive earlier or depart earlier than the beginning of the day. 
for req in range(number_of_requests):
  for flight_type in arrival_departure:
      problem += lpSum(x[req, flight_type, airport, 0] for airport in range(num_airports)) == 1

for req in range(number_of_requests):
  for flight_type in arrival_departure:
    for airport in range(num_airports):
      for slot in range(1, time_slots):
        problem += x[req, flight_type, airport, slot] <= x[req, flight_type, airport, slot - 1]

# ensure that every flight has arrived or departed at the end of the scheduling day
for req in range(number_of_requests):
  for flight_type in arrival_departure:
      problem += lpSum(x[req, flight_type, airport, -1] for airport in range(num_airports)) == 0

# impose interval restriction between arrival and departure flight 
for req in range(number_of_requests):
    for dep_airport in range(num_airports):
      for arv_airport in range(dep_airport + 1, num_airports):
        problem += lpSum(abs(sum(x[req, 0, dep_airport]) - sum(x[req, 1, arv_airport])) * x[req, 0, dep_airport] * x[req, 1, arv_airport]) == flight_requests[req][0] - flight_requests[req][1]

# airport capacity constraints, which limit the number of arrivals and departures at airports
for slot in time_slots:
  for airport in range(num_airports):
    problem += lpSum(int(sum(x[req, flight_type, airport]) == slot) for req in range(number_of_requests) for flight_type in arrival_departure) <= capacity_per_slot

# Solve the MILP problem
problem.solve()

updated_slots = []
max_change = float('-inf')
number_unchanged = 0

# Iterate through the decision variables and check if they are equal to 1
for req in range(number_of_requests):
  for flight_type in arrival_departure:
    change = 0 
    for airport in range(num_airports):
        if x[req, flight_type, airport, 0].varValue == 1:
            slot = sum(x[req, flight_type, airport])
            change = abs(flight_requests[req][flight_type] - slot)
            if change > max_change:
                max_change = change
            if change:
              break 
    if not change:
      number_unchanged += 1 
    else:
        updated_slots.append((req, flight_type, slot, change))

# Print the slot changes
for entry in updated_slots:
    print(f"Flight Request {entry[0]}: Change from slot {flight_requests[entry[0]][entry[1]]} to {flight_requests[entry[2]]}" + "departure" if not entry[1] else "arrival")

print("Status:", LpStatus[problem.status])
print(f"{number_unchanged} flight requests out of {number_of_requests} were not shifted.")
print("Maximum Shift:", max_change)
print("Objective Value:", problem.objective.value())