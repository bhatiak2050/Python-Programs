def get_min_moves(moves, N, s):
    visited = [False] * N

    queue = []

    visited[s] = True
    queue.append((0, 0))

    qe=None
    while queue:
        qe = queue.pop(0)
        v = qe[0]

        if v == N - 1:
            break
        
        j = v+1
        while j<=v+6 and j<=N:
            if visited[j] == False:
                visited[j] = True
                a = (moves[j] if moves[j]!=-1 else j, qe[1]+1)
                queue.append(a)
            j+=1
    return qe[1]

# N = 30
# moves = [-1] * N
# # Ladders 
# moves[2] = 21
# moves[4] = 7
# moves[10] = 25
# moves[19] = 28
  
# # Snakes 
# moves[26] = 0
# moves[20] = 8
# moves[16] = 3
# moves[18] = 6

board = [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1],
]

flatBoard = []
for row in range(len(board)-1, -1, - 1):
    isReversed = (len(board) - 1 - row) % 2 
    if isReversed:
        flatBoard += (board[row][::-1])
    else:
        flatBoard += (board[row])

print(get_min_moves(flatBoard, 36, 0))
