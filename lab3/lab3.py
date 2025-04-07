
import random
# def temperatureConverter(temp,unit):
#    result=0
#    if(unit=='c'):
#       result=((temp)*9/5)+32
#       print(str(result) +'f')
#    elif(unit=='f'):
#      result=(temp-32)*5/9
#      print(str(result) +'c') 

# temperatureConverter(60,'c')
# temperatureConverter(45,'f')
  #-----------------------------------
# for i in range(1500,2701):
#  if(i%7==0 and i%5==0):
#   print(i) 

 #-----------------------------------
# number = random.randint(1,9)
# while(True):
#    n= int(input("Guess a number between 1 and 9"))
#    if(n==number):
#     print("Well guessed\n")
#     break
#    else:
#       print("Wrong choice")
 #-----------------------------------
# n=5
# temp=1
# reachedmax=False
# for i in range(0,2*n):
#    for j in range(0,temp):
#       print("*",end="")
#    print("")
#    if (temp<n and not reachedmax):
#       temp=temp+1
#    elif(temp==n and not reachedmax):
#       reachedmax=True
#       temp=temp-1
#    else:
#       temp=temp-1

# word=input("Enter a word and i will reverse it")
# reversed=word[::-1]
# print(reversed)
#----------------------
# reversed=""
# word=input("Enter a word and i will reverse it")     
# for i in range(1,len(word)+1):
#    reversed = reversed+ word[len(word)-i]
  
# print(reversed)


# list1= [1,3,12,14,35,24]
# evenValues=0
# oddValues=0
# for i in list1:
#    if(i%2==0):
#     evenValues=evenValues+1
#    else:
#       oddValues +=1
# print("Number of even numbers",evenValues,"\n Number of odd values",oddValues)

# list2=[123,1.24,1+2j,True,"Hello",(2,5),[2,5],{"String":1,"Section":2}]

# for i in list2:
#    print(i," ",type(i))

# for i in range(7):
#    if(i==3 or i==6):
#       continue
#    print(i,end=" ")
#------------------------------
# val1=0
# val2=1
# sum=0
# while(True):
#    print(sum)
  
#    val1=val2
#    val2=sum
#    sum=val1+val2
#    if(sum>50):
#     break

#---------------------------------------------------------------------------------------------------------------------14

row=3
col=4
array_2d= [[0 for j in range(col)] for i in range(row)]
for i in range(row):
  for j in range(col):
   array_2d[i][j]= i*j
  print("")
for i in range(row):
  for j in range(col):
   print(array_2d[i][j],end="")
  print("")
