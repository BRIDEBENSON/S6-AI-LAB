# N-Queens problem
from itertools import permutations   
n=int(input("Enter value of n: "))
final_list=[] 
all_possible_permutations=list(permutations([i for i in range(n)]))
for i in all_possible_permutations:
    main_count=0
    for j,k in enumerate(i):
        flag=0
        for l,m in enumerate(i):
            if j-k==l-m or j+k==l+m:
                flag+=1
        if flag>1:
            break
        else:
            main_count+=1
    if main_count==n:
        final_list.append(i)
for z,i in enumerate(final_list):
    print("Combination ",z+1,":")
    for j in i:
        for k in range(n):
            print("Q" if j==k else ".",end=" ")
        print()
    print("\n")
    
        
        




