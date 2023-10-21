import pulp

# Parameters
num_requests = 15000
num_timeslots = 288
capacity = 10  # Fixed capacity for each timeslot
movements = 5  # Maximum allowed distance from the original timeslot

# Create a PuLP problem
problem = pulp.LpProblem("FlightAssignment", pulp.LpMinimize)

# Binary decision variables: m[i, j] is 1 if request i is moved to timeslot j
m = pulp.LpVariable.dicts("Movement", ((i, j) for i in range(num_requests) for j in range(movements)), cat=pulp.LpBinary)

# Constraints
# Each request is assigned to exactly one timeslot
for i in range(num_requests):
    problem += pulp.lpSum(m[i, j] for j in range(num_timeslots)) == 1

# Capacity constraint for each timeslot
for j in range(num_timeslots):
    problem += pulp.lpSum(m[i, j] for i in range(num_requests)) <= capacity

# Additional constraint: ensure that the new timeslot is within the max number of moves allowed 
for i in range(num_requests):
    for j in range(num_timeslots):
        problem += m[i, j] * abs(i - j) <= movements//2 

# Solve the problem
problem.solve()

if problem.status == pulp.LpStatusOptimal:
    # Print the optimal assignments
    for i in range(num_requests):
        for j in range(movements):
            if pulp.value(m[i, j]) == 1:
                print(f"Request {i} moved {j} number of slots")

    # Print the total distance
    total_distance = sum(pulp.value(m[i, j]) * abs(i - j) for i in range(num_requests) for j in range(movements))
    print(f"Total distance: {total_distance}")
else:
    # Print number of remaining requests violating constraints 
    print("No optimal solution found.")
