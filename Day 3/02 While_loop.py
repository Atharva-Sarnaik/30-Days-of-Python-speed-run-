# While loop

r=int(input("Enter the no. of rows: "))
a=int(input("Enter the value of a: "))
while(r>=a):
    print(a)
    r=r-1  # absence of this line of code will result in an infinite while loop

# While loop with else

num=10
while(num>0):
    print(num)
    num=num-1
else:
    print("im inside else now")

# Do-While loop (Loop will be executed atleast once irrespective if condition)
# In python do while loop does not exist, that is why we have to emulate it using while loop

i=0
while True:
    print(i)
    i=i+1
    if(i%10==0):
        break
print("---Code Ended---")

# Output
'''
Enter the no. of rows: 5
Enter the value of a1
1
1
1
1
1
10
9
8
7
6
5
4
3
2
1
im inside else now
0
1
2
3
4
5
6
7
8
9
---Code Ended---
'''
