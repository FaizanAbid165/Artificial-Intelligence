#------------------------Stack using Python
print("Stack using python")
stack = ["Amir","Sufyan","Iqbal"]
stack.append("Talha")
stack.append("Usama")
print(stack)
#Remove the last item from stack  
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
#------------------------Queue using Python
print("Queue Using Python")
queue = ["Awais","Farhan","Raju"]
queue.append(2)
queue.append("sultan")
print(queue)
#Remove the first item from queue
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)
#-------------------------Binary Search in Python
print("Binary Search in python")
def binarySearch(e,list):
    length = len(list)
    start = 0
    end = length-1
    
    while(start<=end):
        mid = (start+end)/2
        m = int(mid)
        if(e==list[m]):
            return True
        elif(e<list[m]):
            end = m-1
        elif(e>list[m]):
            start = m+1
    return False
list = [1,2,3,4,5]
print(binarySearch(0,list))

        
        

        


