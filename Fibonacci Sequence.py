def sequence():
    print ("~" * 44)
    print ("Welcome to the Fibonacci Sequence Generator!")
    print ("~" * 44)
    
    iteration = int(input("What iteration of the Fibonacci Sequence would you like me to travel to? "))
    print ("Traveling to iteration number", iteration, "\n")

    for i in range(0, iteration):
        print (fibonacci(i))

        
def fibonacci(n):
    fib = 0
    onacci = 1
    for i in range(0, n):
        thirdnum = fib
        fib = onacci
        onacci = thirdnum + onacci

    return fib

def main():
    sequence()
    input("\nHit Enter to exit")
    
main()
