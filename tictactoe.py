def display_board(matrix):
    for i in matrix:
        print(" ".join(i))

def check_win(matrix, i, j, s):
    try:
        if all(matrix[i + k][j] == s for k in range(3)):
            return True
    except:
        pass
    try:
        if all(matrix[i][j + k] == s for k in range(3)):
            return True
    except:
        pass
    try:
        if all(matrix[i + k][j - k] == s for k in range(3)):
            return True
    except:
        pass
    try:
        if all(matrix[i + k][j + k] == s for k in range(3)):
            return True
    except:
        pass
    return False

matrix=[[" . "]*3 for _ in range (3)]
p1=[]
p2=[]

while True:
    print("Player 1")
    i1,j1=map(int,input("Enter row and column separated by Space ").split())
    matrix[i1][j1]=" X "
    display_board(matrix)
    p1.append((i1,j1))
    for i,j in p1[::-1]:
        if check_win(matrix,i,j," X "):
            print("Player 1 Win ")
            exit()
            
    print("Player 2")
    i2,j2=map(int,input("Enter row and column separated by Space ").split())
    matrix[i2][j2]=" O "
    display_board(matrix)
    p2.append((i2,j2))
    for i,j in p2[::-1]:
        if check_win(matrix,i,j," O "):
            print("Player 2 Win ")
            exit()

