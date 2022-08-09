lines = open('16.in').read().strip().split(',')
default_state = list("abcdefghijklmnop")

def dance(lines, state):
    for change in lines:
        if change.startswith('s'):
            skips = int(change[1:])
            new_state = ['' for _ in range(16)]
            for i in range(len(new_state)):
                old_idx = i - skips
                if old_idx < 0:
                    old_idx = 16 + old_idx
                new_state[i] = state[old_idx]
            state = new_state
        elif change.startswith('x'):
            p1, p2 = [int(val) for val in change[1:].split('/')]
            state[p1], state[p2] = state[p2], state[p1]
        elif change.startswith('p'):
            c1, c2 = change[1:].split("/")
            p1, p2 = state.index(c1), state.index(c2)
            state[p1], state[p2] = state[p2], state[p1]
    return state

print("".join(dance(lines, default_state.copy())))

state_to_idx =dict()
state_to_idx["".join(default_state)] = 0
state = default_state.copy()
for i in range(1, 1000000001):
    state = dance(lines, state)
    if "".join(state) in state_to_idx:
        cycle_length = i - state_to_idx["".join(default_state)]
        idx = (int(1e9) - i) % cycle_length 
        for k, v in state_to_idx.items():
            if v == idx:
                print(k)
                break
        break
    else:
        state_to_idx["".join(state)] = i
