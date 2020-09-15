'''
- Load data into program
- iterate through the file
- determine if each number is even or odd
- if odd: odd total = +1
- if even: odd total = +1
- if something else: there's a problem
- determine if one number is greater than the other
- print out statistics
'''

#nums = [41, 468, 145, 198, 306, 360, 133, 333, 26, 449, 88, 321, 482, 258, 354, 382, 378, 318, 35]

iFile = open("numbers.txt", 'r')  #Read

nums = iFile.readlines()  #Reads all lines in the input file


def evenOrOdd():
    for num in nums:  #Gather even numbers
        x = int(num)
        
        if x == 123:
            break
        elif x % 2 == 0:
            print ("These are the even numbers: ", x)

    print ('')

    for num in nums:  #Gather odd numbers
        x = int(num)
        
        if x == 234:
            break
        elif x % 2 != 0:
            
            print ("These are the odd numbers: ", x)

    print ('')


def count():
    
    countEven = 0
    countOdd = 0

    for num in nums:  #Gather count of even and odd numbers
        x = int(num)
        
        if not x % 2:
            countEven+=1
        else:
            countOdd+=1
        

    print ("Number of even numbers: ", countEven)
    print ("Number of odd numbers: ", countOdd)

    print ('')


def largestNum():

    for num in nums:
        num = int(nums)

        num.append(num)
        
        
    print ("The largest number in the list is: ", max(num))



def main():
    evenOrOdd()
    count()
    largestNum()

    input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nPress Enter to exit.")
    
main()
