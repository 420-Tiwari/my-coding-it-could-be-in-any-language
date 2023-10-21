#WHILE LOOP
"""age=int(input("Enter your age for joining any com :-"))
while age<=58:
    print(age)
    age=age+1
else :
    print("Am going to be 60 && it's time to get retirement ")"""

#FOR WITH RANGE S=FUNCTION
"""i=int(input("Enter your number from start:- "))
for i in range(i,50):
        if i%2==0:
            print(i)
else:
    print("Progran is completed thank you ")"""

#PATTERN
"""n=int(input("Enter the any number for creating pattern:-"))
for i in range(0, n):
    for j in range(0, i+1):
        print("*",end="")
    print("\r")#\r it is carriage return means it will go next line not create space over there
print("\n")
print("Your pattern created Thank you")"""

#FOR LOOP OVER LIST WITH BREAK
"""lt=["Apple","Banana","charrey",1,1,2,3,5,"nitesh"]
print(lt[6])
for i in lt:
    if i==2:
        print("Thank you")#It will print message at the last of output
        break
    print(i)"""

#CONTINUE STATEMENT
lt=["Apple","Banana","charrey",1,1,2,3,5,"nitesh"]
for i in lt:
    if i==2:
        continue
    print(i)
print("Thank you")
