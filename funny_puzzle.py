import heapq

def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):

    distance = 0
    for i in range(len(from_state)):
        if from_state[i] == 0:
            continue
        else:
            tile_row = i // 3
            tile_col = i % 3
            goal_row = to_state.index(from_state[i]) // 3
            goal_col = to_state.index(from_state[i]) % 3
            distance += abs(tile_row - goal_row) + abs(tile_col - goal_col)
    return distance

def print_succ(state):

    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):

    succ_states = []

    for i in range(len(state)):
        if state[i] == 0:
            zero_row = i // 3
            zero_col = i % 3
            for j in range(len(state)):
                if state[j] == 0:
                    continue
                else:
                    tile_row = j // 3
                    tile_col = j % 3
                    if tile_row == zero_row:
                        if abs(tile_col - zero_col) == 1:
                            state[i], state[j] = state[j], state[i]
                            succ_states.append(state.copy())
                            state[i], state[j] = state[j], state[i]
                    elif tile_col == zero_col:
                        if abs(tile_row - zero_row) == 1:
                            state[i], state[j] = state[j], state[i]
                            succ_states.append(state.copy())
                            state[i], state[j] = state[j], state[i]
    return sorted(succ_states)


    


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """

    # heapq.heappush(pq ,(cost, state, (g, h, parent_index)))
    # g is the number of moves from the initial state to the current state (i.e., the depth of the search tree)
    # h is the get_manhattan_distance value of the current state

    open = []
    closed = []
    heapq.heappush(open, (get_manhattan_distance(state), state, (0, get_manhattan_distance(state), -1)))
    closed_index = -1
    while open:
        n = heapq.heappop(open)
        closed.append(n)
        if n[1] == goal_state:
            closed_index = closed.index(n)
            break
        for successor in get_succ(n[1]):
            parent_index = closed.index(n)
            g =  n[2][0] + 1
            h = get_manhattan_distance(successor)
            n_next = (g + h, successor, (g, h, parent_index))
            in_closed = False
            in_open = False            
                    
            for s in open:
                if s[1] == successor:
                    in_open = True
                    if s[2][0] > g:
                        open.remove(s)
                        heapq.heapify(open)
                        heapq.heappush(open, n_next)
                        break

            for s in closed:
                if s[1] == successor:
                    in_closed = True
                    if s[2][0] > n_next[2][0]:
                        closed.remove(s)
                        heapq.heappush(open, n_next)
                        break
            
            if (not in_closed) and (not in_open):
                heapq.heappush(open, n_next)

    state_info_list = []

    while True:
        state_info_list.append(closed[closed_index])
        closed_index = closed[closed_index][2][2]
        if closed_index == -1:
            break

    state_info_list.reverse()

    for state_info in state_info_list:
            current_state = state_info[1]
            h = state_info[2][1]
            move = state_info[2][0]
            print(current_state, "h={}".format(h), "moves: {}".format(move))

if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print_succ([2,5,1,4,0,6,7,0,3])
    print()

    print(get_manhattan_distance([2,5,1,4,0,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    solve([2,5,1,4,0,6,7,0,3])
    print()
