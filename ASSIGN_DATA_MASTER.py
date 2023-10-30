            ### ASSIGNMENT QUESTION BY DATA SCINCE MASTER COURSE ###

#Q.1:-Characteristic of Tuple
#Tuple is data structure or data type wich used to stor any type of data
#element with is tuple is immutable that means If once tuple is creted with it's
#element then element can not be changed

tuple_1=(1,3,5,'Nitesh',34.45,'a')
print(tuple_1)
#tuple_1['Nitesh']=4#It will give you an error assignment does not support
print(tuple_1)

#Q.2 NOT REMEMBER TUPLES TWO BUILD-IN METHOD

#Q.3 DUPLICATE ITEMS            #PARTIALLY THIS QUESTION DONE HALF QUESTION 
#Tuple doest not support to having double element or duplicate value


#Q.4 NO

#Q.5 Dictionary is also a type of data structure in python and dictionary is
#a key value pair and element is stored in dictionary are unordered and it can
# be orederd by it's method

#Q.6 Dictionary can be nested means a dictionary can have an another dictionary
#within a dictionary OVERALL dictionary can be nested

d1={'name':{'male':'Nitesh','female':'Anjali'},'age':{'male':19,'female':18}}
print(d1)

#Q.7 SET-DEFAULT METHOD ON DICTIONARY

dict={}
dict.setdefault('topic', {'language' : 'Python', 'course': 'Data Science Masters'})
print(dict)
