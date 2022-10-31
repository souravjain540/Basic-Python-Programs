def check_winner(board, win_condition = 4):
    rows = len(board)
    cols = len(board[0])
    
    memo = tuple(tuple([1]*4 for j in range(cols)) for i in range(rows))
    
    for i in range(rows):
        for j in range(cols):
            cur = (i,j)
            for k in range(4):
                prev = get_prev(cur,k)
                if (-1 < prev[0] < rows) and (-1 < prev[1] < cols) and value(board, prev) == value(board, cur):
                    value(memo, cur)[k] = value(memo, prev)[k]+1
                    if (value(memo, cur)[k] == win_condition) and (value(board, cur) != None):
                        return (value(board, cur))
    return None
    
def get_prev(v,k):
    u = ((0,-1),(-1,-1),(-1,0),(-1,1))[k]
    return ((v[0]+u[0]), (v[1]+u[1]))
    
def value(board, incices):
    return board[incices[0]][incices[1]]

def test_check_winner():
    board = [[ None, None, None, None, None, None, None, None ],
             [ None, None, None, None, None, None, None, None ],
             [ None, None, None, None, None, None, None, None ],
             [ "p2", None, None, None, None, None, None, None ],
             [ "p3", "p2", "p1", None, None, None, None, None ],
             [ "p3", "p1", "p2", "p2", "p3", "p1", None, None ],
             [ "p1", "p3", "p2", "p2", "p1", "p3", "p1", "p3" ]]
    assert(check_winner(board) == "p2")
    assert(check_winner(board, win_condition = 5) == None)
