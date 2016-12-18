size = 32
board = {}
for i in range(size):
    for j in range(size):
        board[(i, j)] = 0

def find_neighbors(pair):
    l = []
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            if a == b == 0:
                continue
            l.append((pair[0]+a, pair[1]+b))
    return l

def get_list(l):
    r = []
    for p in l:
        r.append(board.get(p, 0))
    return r

def inc():
    global board
    board2 = board.copy()
    for i in range(size):
        for j in range(size):
            board2[(i,j)] = decide((i,j))
    board = board2.copy()

def decide(pair):
    v = 0
    p = board[pair]
    n = get_list(find_neighbors(pair))
    if p == 0:
        v = []
        for p in set(n)-{0}:
            if n.count(p) == 3:
                v.append(p)
        if len(v) == 1:
            v = v[0]
        else:
            v = 0
    else:
        if all(s == 0 or s == p for s in n):
            c = n.count(p)
            if c in [2,3]:
                v = p
    return v

#def decide2(pair):

def disp():
    s = ""
    for j in range(size)[::-1]:
        for i in range(size):
            s += str(board[(i, j)]) + ' '
        s += '\n'
    print(s)

def start():
    clear()
    board[(size/2, size/2)] = 1
    board[(size/2 -1, size/2)] = 1
    board[(size/2, size/2 -1)] = 1
    board[(size/2 -1, size/2 -1)] = 1

def loop():
    states = []
    while True:
        disp()
        inc()
        if board in states:
            break
        states.append(board.copy())
    disp()

def input_coord(p):
    n = set()
    f = set()
    for s in board.keys():
        if board[s] == p:
            n |= set(find_neighbors(s))
        if board[s] != 0:
            f |= {s}
    n -= f
    pair = ()
    while pair not in n:
        x = input('x: ')
        y = input('y: ')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            pass
        pair = (x, y)
        print(pair)
    return pair

def glider(pair, p=1, flip=(1,1)):
    x = pair[0]
    y = pair[1]
    xf = flip[0]
    yf = flip[1]
    adj_same([(x-1*xf,y-1*yf), (x,y-1*yf), (x+1*xf,y-1*yf), (x+1*xf,y), (x,y+1*yf)], p)

def exploder(pair, p=1, flip=(1,1)):
    x = pair[0]
    y = pair[1]
    xf = flip[0]
    yf = flip[1]
    adj_same([(x-1*xf,y), (x,y-1*yf), (x+1*xf,y-1*yf), (x+2*xf,y), (x+1*xf,y+1*yf), (x,y+1*yf), (x+1*xf,y)], p)

def blinker(pair, p=1, flip=(1,1)):
    x = pair[0]
    y = pair[1]
    xf = flip[0]
    yf = flip[1]
    adj_same([(x-1*xf,y), (x,y), (x+1*xf,y)], p)
    
def clear():
    for i in range(size):
        for j in range(size):
            board[(i, j)] = 0

def adj(pair, val):
    board[pair] = val

def adj_many(pair_vals):
    for i in pair_vals:
        adj(i[0], i[1])

def adj_same(pairs, p):
    for i in pairs:
        adj(i, p)

def count(p):
    return list(board.values()).count(p)

def play_solitaire(p):
    start()
    disp()
    while count(1) > 0:
        adj(input_coord(p), 1)
        loop()
