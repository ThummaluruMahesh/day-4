# ----> while loop
# -----> break using while loop

# Eg:1
#1.) iterate from 20 to 30 and break the loop in 27
'''
i= 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1
20
21
22
23
24
25
26
'''
#2.)
'''
i= 20
while i<31:
    print(i)
    i+=1
    if i ==27:
        break

20
21
22
23
24
25
26
'''
#3.)
'''
i= 20
while i<31:
    print(i)
    if i ==27:
        break
    i+=1
20
21
22
23
24
25
26
27
'''

#4.)
'''
i= 20
while i<31:
    if i ==27:
        print(i)
        break
    i+=1
27
'''

# ! ------> continue
'''
while i<31:
     i=i+1
     if i==27:
        continue
     print(i)
21
22
23
24
25
26
28
29
30
31
'''
#  while to iterate from 12 to 22
# find the sum of all numbers
'''
i=12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)        
    
187
'''

# ! Eg:6
# find the average of value from 20 to 25
'''
i=20
sum=0
count=0
while i<=25:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)  

22.5
'''
# find the average of value from 20 to 30
'''
i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)  

25.0
'''

# ! ------> nested  for loop
# Eg:1
'''
for i in range(1,3+1):
    for j in range(1,4+1):
        print(i,j)

1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
'''

# ! Eg: 2
# * * * *
# * * * *
# * * * *
# * * * *
'''
for row in range(4):
    for col in range(4):
        print("*", end=" ")
    print()
             
* * * * 
* * * * 
* * * * 
* * * * 
'''
'''
for row in range(4):
    for col in range(4):
        print(row, end=" ")
    print()
    
0 0 0 0 
1 1 1 1 
2 2 2 2 
3 3 3 3 
'''


#! to print stars in right angled triangle


'''
for row in range(0,6):
    for col in range(0,row):
        print("*", end=" ")
    print()

* 
* * 
* * * 
* * * * 
* * * * * 

'''

# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
'''
for row in range(0,6):
    for col in range(row,6):
        print("*", end=" ")
    print()

* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''

# * * * * *
# *       *
# *       *
# *       *
# * * * * *
'''
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''

#      *
#    * * *
#   * * * *
#  * * * * *
'''
for row in range(0,5):
    for col in range(0,6):
        if ((row==0 and col==3) or (row==1 and(col>=2 and  col<=4) or (row ==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

  
      *     
    * * *   
  * * * * * 
'''


# *
# * *
# *   *
# *     *
# *       *
# * * * * * *
'''
for  row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

*           
* *         
*   *       
*     *     
*       *   
* * * * * * 
'''
#----> List

#---> Datatypes
# Primary

# Number---> int,float,complex
# string
# Boolean
# none

# Collection
# List
# tuple
# set
# dictionary

#---> List

#1.) If the collection of elements are surrounded by square brackets, it is considered to be list
##Eg:1
   #l1 = [4, 7, 9, 89, "hello", 7+9], [8,9,0]

#characteristics of list
#1.)list have to surrounded by[]
#2.)It is mutable ( the elements in the list are changable)
#3.)Every element inside list in indexed
#4.)The elements inside list will be ordered format
#5.)It can hold duplicate values
#6.)it is heterogenous

# TO access the elements in list
'''
lst1=[1,4,1,7,89.7,5,"p","i",5,2,20]
#print(l1)
'''
#--->Indexing
#The collection datatypes like list, tuple, string, the elements will be alloted with predefined unique value called index value

#We have 2 types of indexing
#positive indexing --> starts with 0 from left hand side
#Negative indexing --> starts with -1 from right hand side

#--->Positive indexing
'''print(lst1[0])
print(lst1[4])
print(lst1[10])
print(lst1[20]) #--->error'''

#---> Negative indexing
'''
lst1=[1,4,1,7,89.7,5,"p","i",5,2,20]
print(lst1[-1])
print(lst1[-4])
'''

# ----->slicing
lst1=[1, 4, 1, 7,89.7, 7.5, "p", "i"]
#lst1[start_index:end_index;step]
'''
print(lst1[0:4])
[7, 89.7, 7.5]
'''
'''

print(lst1[6:8])
['p', 'i']
'''

'''
print(lst1[3:6])
[7, 89.7, 7.5]
'''
'''
print(lst1[:5])
[1, 4, 1, 7, 89.7]

'''

'''
print(lst1[3:])
[7, 89.7, 7.5, 'p', 'i']
'''

'''
print(lst1[:])
[1, 4, 1, 7, 89.7, 7.5, 'p', 'i']
'''
'''
print(lst1[0:7:1])# lst1[0:7] --> both are same
[1, 4, 1, 7, 89.7, 7.5, 'p']
'''

'''
print(lst1[0:7:2])
[1, 4, 1, 7, 89.7, 7.5, 'p']
[1, 1, 89.7, 'p']
'''


lst1=[1, 4, 1, 7,89.7, 7.5, "p", "i"]
#print(lst1[-4:-1])
#print(lst1[-1:-4]) --> []
#print(lst1[-7:-1])
#print(lst1[-7:-1:2])

# ! To insert ot add element inside list

# append()-> used to add elelement at last position of list
'''
l1 =[9, 8, 0, 6]
l1.append("car")
print(l1)
[9, 8, 0, 6, 'car']
'''










s1="hello world to all"














