#OPERATORS MAINLY BOOLEAN OPERATOR
"""start=0
stop=1
some_float=-38.90
some_integer=56
print(bool( stop))
print(bool(int(not stop)))
print(f" The first result is {start}")
print(f" The first result is {bool(stop)}")
print(f" The result is {int(not stop)}")
print(f" Float value we have to see {int(bool(some_float))}")
print(f" Float value we have to see {int(bool(not some_float))}")
print(f" Float value we have to see {bool(some_float)}")# 1 means true
print(" Integer value we have to see ",bool(some_integer))
print(f" Integer value we have to see {int(bool(some_integer))}\n\n\n")# 0 means false

school=True
college=False
job=school and college
job1=school or college
#print(f" The final result is {bool(job)}")
print("The final result is ",not(bool(job1)))


print(not(False)*True)
not(False)*True"""


#ABOUT STRING

"""str1="nitesh Tiwari"
for i in str1:
    print(i)
str1.capitalize
print(str1)

#BINARY NUMBER REPRESENTATION
var1=10
var=255
var2=256
print(bin(var1))#0b is used for preffix representation of binary number
print(bin(var))#only till 11111111 no more 1's
print(bin(var))"""

"""LIST=[3,5,6,2,'Nitesh']#list element can be change but 
LIST[2]='Pawan'         # A string element can not be change
print(LIST)"""


#STRING SLICE-ING

cource_name="Data science of master" + "Padega Nitesh Tabhi to Badega Chotu"
str="nitesh tiwari"
str1="NITESH TIWARI"
str2="Tiwari Nitesh Harinarayan"
str3="nITESH tIWARI"
print(cource_name[11:4:-1])
print(cource_name[5:12])
print(cource_name)
print(cource_name*10)#10 times will print the same message
print(len(cource_name))#including space between the strings 
print(len(str))
print(len(str1))#without the space
print(cource_name.find("D"))# it woll return the index number of string
print(cource_name.find("a",5,10))#start and stop in it if character is not found it will return -1
print(cource_name.count(" "))#count is start from 1 not 0 and it return the occurrence of a string(character)
print(str.upper())#LOWER
print(str1.lower())#UPPER
print(str.split("i"))#remove the element from the string
print(str1.partition("i"))
print(str2.swapcase())#except first char. all in the upper case
print(str3.title())
