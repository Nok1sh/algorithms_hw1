from test_alg import universal_test_system
from test_for_all_tasks import task8

def func(N, k):
    result = 0

    board = []
    for i in range(N):
        board.append([0]*N)

    horse_move = [(-2, 1), (-2, -1), (-1, 2), (-1, -2),
                  (2, -1), (2, 1), (1, -2), (1, 2)]
    
    def check_move(x1, y1):

        for i in range(N):
            if board[x1][i] or board[i][y1]:
                return False
        
        for i in range(N):
            for j in range(N):
                if abs(i - x1) == abs(j - y1) and board[i][j]:
                    return False
        
        for dx, dy in horse_move:
            dx += x1
            dy += y1

            if 0 <= dx < N and 0 <= dy < N and board[dx][dy]:
                return False
        
        return True

    def move_mag(count_mag, s):
        nonlocal result
        if count_mag == k:
            result += 1
            return

        for i in range(s, N**2):
            x = i // N
            y = i % N
            if board[x][y]:
                continue
            if check_move(x, y):
                board[x][y] = 1
                move_mag(count_mag+1, i+1)
                board[x][y] = 0

    move_mag(0, 0)
    return result

name, solutions, tests = task8()

solutions[name] = func

universal_test_system(solutions, tests)