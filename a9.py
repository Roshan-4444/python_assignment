a = []
for i in range (5):
    b = int(input("Enter number:"))
    a.append(b)
    c = sorted(a)    
    d = sorted(a, reverse=True)
    print(a)
    print(c)
    print(d)
    #Exercise 9: Sorting a List
#Write a Python program that:
#1. Asks the user to input a list of 5 numbers.
#2. Sorts the list in ascending order and displays it.
#3. Sorts the list in descending order and displays it.