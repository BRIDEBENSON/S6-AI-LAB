n=int(input("Enter value of n: "))
matrix=[[0]*n for i in range(n)]
i,j=0,n//2
for num in range(1,n*n+1):
    matrix[i][j]=num
    i,j=(i-1)%n,(j+1)%n
    if matrix[i][j]!=0:
        i,j=(i+2)%n,(j-1)%n
for i in matrix:
    print(i)    