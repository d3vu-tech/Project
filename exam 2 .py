## 1.(a)
    #if,elif and else are decisional control flow statements.
    #if is used to check the first given condition and starts the decision block
    #elif stands for 'else if'and used to check additional multiple conditions if the "if condition" is false.
    #else block will execute when all of the above "if" and "elif" conditions are false
    #syntax:
        #if condition:
            #statement 1
        #elif condition1:
            #statement 2
        #elif condition 2:
            #statement 3
        #else condition:
            #Last statement
    #example:
num=-2
if num==0:
    print("zero")
elif num>0:
    print("positive")
else:
    print("negative")

## 1.(b)
    #Nested if statements contains another if statements either in its 'if' block or 'else' block
    #example:
x=0
if x!=0:
    if x<0:
        print("Negative")
    else:
        print("Positive")
else:
    print("zero")

## 1. (c)
    #Logical conditions are used to evluate multiple conditions at once. AND, OR and NOT are logical operators.
    #AND: all the conditions must be true.
    #OR: atleast one condition must be true.
    #NOT: reverses the result. true becomes false and viceversa.

## 2. (a)
    #for loop is used to iterate over a sequence.used when number of iterations is known.eg:
for i in range(10):
    print(i)
    #while loop is used when condition needs to be checked repeatedly.it repeats as long as the condition is true and it stops when the condition becomes false.eg:
x=1
while (x<10):
    print(x)
    x=x+1

## 2. (b)
    #break statement is used to terminate the loopor statement.
    #continue is to pass controll to the next iteration without exiting the loop.

## 3. (a)
    #A list is the collection of items separated by commas enclosed in square brackets which allows duplicates and can be altered after creation.

## 3. (b)
    #append() - adds an element at the end of the list. 
    #syntax:
    #   numbers=[1,2,3]
    #   numbers.append(4)
    #   print(numbers)
    #output:
    #   [1,2,3,4]
    
    #insert() - inserts an element at the specified position
    #syntax:
    #   fruits=["apple","banana","mango"]
    #   fruits.insert(2,"kiwi")
    #   print(fruits)
    #output:
    #   ["apple","kiwi","banana","mango"]
               
    #sort() - sort the list
    #syntax:
    #   marks=[56,23,89,43,54]
    #   marks.sort()
    #   print(marks)
    #output:
    #   [23,43,54,56,89]

    #clear() - removes all the elements or the specified element from the list
    #syntax:
    #   fruits=["apple","banana","kiwi"]
    #   fruits.clear("banana")
    #   print(fruits)  
    #output:
    #   []

    #copy() - returns the copy of the list(a new list with same elements)
    #syntax:
    #   original_list=[1,2,3,4]
    #   new_list=original_list.copy()
    #   print(new_list)
    #output:
    #   new_list=[1,2,3,4]

## 4. (a)
    #user defined functions can be created or defined by the users according to their needs.
    
