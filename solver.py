def main():
    # https://www.gathering4gardner.org/g4g10gift/puzzles/Hoff_Carl-Untouchable_11.pdf
    M = 12
    N = 12
    blocks = [
        [
            [0, 1, 1],
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ],
        [
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ],
        [
            [0, 0, 1],
            [0, 1, 1],
            [1, 1, 0],
            [1, 0, 0]
        ],
        [
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 0],
            [1, 0, 0]
        ],
        [
            [0, 1, 1],
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 0]
        ],
        [
            [0, 1, 1],
            [0, 1, 0],
            [1, 1, 0],
            [1, 0, 0]
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [0, 1, 0],
            [1, 1, 0]
        ],
        [
            [1, 0, 0],
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0]
        ],
        [
            [0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [1, 1, 0],
            [0, 1, 0]
        ]
    ]
    board = [[0 for _ in range(N)] for _ in range(M)]
    solve(board, blocks, 0)

    
def solve(board, blocks, block_id):
    if block_id == len(blocks) - 1:
        print_board(board)
    visited_points_list = get_potential_visited_points(board, block[block_id])
    for p in visited_points:
        board[p[0]][p[1]] = 1
    solve(board, blocks, block_id + 1)
    for p in visited_points:
        board[p[0]][p[1]] = 0

def get_potential_visited_points(board, block):
    return [[]]

def is_safe(board, block):
    return false



def print_board(board):
    for row in board:
        print(''.join(map(lambda x: '✅' if x == 1 else '⬛️', row)))

if __name__ == "__main__":
    main()
