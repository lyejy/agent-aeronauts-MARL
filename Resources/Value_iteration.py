from time import time


### Global Settings

# Print formatting
name_alias_max = 5
grid_padding = 10
print_name_alias = True

# MDP config
grid_rows, grid_cols = 3, 4
convergence_tol = 0.01
discount_factor = 0.95


### MDP classes

class State:
    def __init__(self, pos, is_absorb_state, reward, name_alias=None):
        assert len(name_alias) <= name_alias_max if name_alias is not None else True  # Allow single char name only
        self.pos = pos
        self.is_absorb_state = is_absorb_state
        self.reward = reward
        self.name_alias = name_alias
        self.value = 0
        self.value_old = 0
        self.is_converged = True
        self.policy = "--"

class Transition:
    def __init__(self, direction, pos_delta, transition_prob):
        self.direction = direction
        self.pos_delta = pos_delta
        self.transition_prob = transition_prob

class Action:
    def __init__(self, direction, transitions):
        self.direction = direction
        self.transitions = transitions


### Print functions

def print_states(states, value_to_print, print_name_alias):
    if value_to_print == "value":
        f_print_value = lambda state: state.value
    elif value_to_print == "policy":
        f_print_value = lambda state: state.policy
    else:
        raise ValueError("value_to_print must be one of {0}".format(["value", "policy"]))

    for i in reversed(range(1, grid_rows+1)):   # Print like a "mathematical graph"
        out_str = ""
        for j in range(1, grid_cols+1):
            pos = (i, j)
            if pos in states:
                state = states[pos]
                s = str(f_print_value(state))[:name_alias_max]
                if print_name_alias and state.is_absorb_state:
                    s = str(state.name_alias)
            else:
                s = ""
            out_str += s.ljust(grid_padding)
        print(out_str)

def print_states_value(states):
    print_states(states, "value", print_name_alias)

def print_states_policy(states):
    print_states(states, "policy", print_name_alias)


### Main

def main():
    t0 = time()

    ### Create states
    states = {}
    for i in range(1, grid_rows+1):
        for j in range(1, grid_cols+1):
            pos = (i,j)
            states[pos] = State(pos, is_absorb_state=False, reward=-0.025)
    states[(3,4)] = State((3,4), is_absorb_state=True, reward=1, name_alias="Goal")   # End goal
    states[(2,4)] = State((2,4), is_absorb_state=True, reward=-1, name_alias="Tiger")   # Tiger
    states.pop((2,2))   # Wall

    ### Create actions
    pos_deltas = {
        "N": (1,0), "S": (-1,0),
        "E": (0,1), "W": (0,-1),
    }
    actions = {}
    actions["N"] = Action("N", transitions=[
        Transition("N", pos_deltas["N"], 0.8), Transition("W", pos_deltas["W"], 0.1), Transition("E", pos_deltas["E"], 0.1),
    ])
    actions["S"] = Action("S", transitions=[
        Transition("S", pos_deltas["S"], 0.8), Transition("W", pos_deltas["W"], 0.1), Transition("E", pos_deltas["E"], 0.1),
    ])
    actions["E"] = Action("E", transitions=[
        Transition("E", pos_deltas["E"], 0.8), Transition("N", pos_deltas["N"], 0.1), Transition("S", pos_deltas["S"], 0.1),
    ])
    actions["W"] = Action("W", transitions=[
        Transition("W", pos_deltas["W"], 0.8), Transition("N", pos_deltas["N"], 0.1), Transition("S", pos_deltas["S"], 0.1),
    ])

    ### Value Iteration
    # Print initial values
    print_states_value(states)
    print("Initial state values" + "\n")

    i = 0
    while True:
        # Value iteration (estimate state values)
        for state in states.values():
            if state.is_absorb_state: continue
            expected_utils = []
            for action in actions.values():
                expected_util = 0
                for t in action.transitions:
                    pos_new = tuple(a + b for a, b in zip(state.pos, t.pos_delta))
                    pos_new = pos_new if pos_new in states else state.pos   # new pos if within grid and not wall
                    state_new = states[pos_new]
                    expected_util += t.transition_prob * (state_new.reward + (state_new.value_old * discount_factor))
                expected_utils.append((expected_util, action.direction,))
            best_action = max(expected_utils, key=lambda x: x[0])   # Action with max value / expected utility
            state.value, state.policy = best_action

        # Update state values
        for state in states.values():
            state.is_converged = abs(state.value_old - state.value) < convergence_tol
            state.value_old = state.value
        # Print
        i += 1
        print_states_value(states)
        print("Iteration: {0}".format(i) + "\n")
        # Convergence check
        is_converged = all([state.is_converged for state in states.values()])
        if is_converged: break

    print_states_policy(states)
    print("Best policy" + "\n")
    print("Time taken is {:.4f} seconds".format(time() - t0))


if __name__ == "__main__":
    main()

























