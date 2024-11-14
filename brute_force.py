import numpy as np

class FormerGame:
    def __init__(self,grid, grid_size, num_symbols):
        self.grid_size = grid_size
        self.num_symbols = num_symbols
        self.reset(grid)

    def reset(self, grid):
        self.grid = grid
        return self.get_state()
    
    def get_state(self):
        return self.grid.copy()

    def get_valid_actions(self):
        valid_actions = []
        rows, cols = self.grid.shape
        for row in range(rows):
            for col in range(cols):
                symbol = self.grid[row, col]
                if symbol != 0:
                    valid_actions.append((row, col))
        return valid_actions  

    def step(self, action):
        row, col = action
        symbol = self.grid[row, col]
        if symbol == 0:
            return self.get_state(), 0, False

        connected_blocks = self.find_connected_blocks(row, col, symbol)

        for r, c in connected_blocks:
            self.grid[r, c] = 0

        self.apply_gravity()

        done = np.all(self.grid == 0)

        return self.get_state(), done

    def find_connected_blocks(self, row, col, symbol):
        visited = set()
        to_visit = [(row, col)]
        while to_visit:
            r, c = to_visit.pop()
            if (r, c) in visited:
                continue
            if self.grid[r, c] != symbol:
                continue
            visited.add((r, c))

            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.grid.shape[0] and 0 <= nc < self.grid.shape[1]:
                    if self.grid[nr, nc] == symbol:
                        to_visit.append((nr, nc))
        return visited

    def apply_gravity(self):
        rows, cols = self.grid.shape
        for col in range(cols):
            column = self.grid[:, col]
            non_zero = column[column != 0]
            zeros = np.zeros(rows - len(non_zero), dtype=int)
            self.grid[:, col] = np.concatenate((zeros, non_zero))

def find_unique_moves(game):
    moves = game.get_valid_actions()

    for m in moves:
        if m in moves:
            alike_moves = game.find_connected_blocks(m[0], m[1], game.grid[m[0], m[1]])
            alike_moves.remove(m)

            moves = [move for move in moves if move not in alike_moves]

    return moves

def get_states(current_state, game, shortest_path, depth):

    if shortest_path < depth:
        return current_state
    
    states = []
    for move in find_unique_moves(game):
        temp = game.step(move)
        new_state, done = temp[0], temp[1]
        if done:
            shortest_path = depth
            game.reset(current_state)    
            return True
        states.append((move, get_states(new_state, game, shortest_path, depth + 1)))
        game.reset(current_state)        
    return states

def unwrap(states, moves, depth, current_solution):
    print(moves)
    if depth >= 14:
        moves.pop(-1)
    else:
        if type(states) == bool:
            print(len(moves), len(current_solution))
            if states == True:
                if len(current_solution) > len(moves):
                    current_solution = moves[:]
                moves.pop(-1)
        else:
            for state in states:
                print(f"\nThis is state[0]:{state[0]}\n")
                moves.append(state[0])
                unwrap(state[1], moves, depth+1, current_solution)
                

def main():
    

    #state = game.get_state()
    original_state =  np.random.randint(1, 5, size=(4,4))
    game = FormerGame(original_state, grid_size=(4, 4), num_symbols=4)
    print("Initial game state:")
    print(original_state)

    #action = (int(input()), int(input()))
    #new_state, done = game.step(action)

    #games = [([move, move,...], grid)]

    shortest_game = 10
   
    states = get_states(original_state, game, shortest_game, 0)
    print(states)


    print(states)

    solution = [0]*15

    unwrap(states, [], 0, solution)

    print(solution)
    print("\nShortest path to clear the board:")
 
if __name__ == "__main__":
    main()