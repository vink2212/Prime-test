print("program start")
from math import floor

#Checks if a number is prime
def check_prime(number):
    c = 2
    
    counter = 0
    while c < floor(number**0.5):
        if number % c == 0:
            return False
            counter += 1
            break
        
        c += 1
    if counter > 0:
        return False
    if counter == 0:
        return True
        
def largest_factor(number):
    n = floor(number ** 0.5) #finds sqaure root of number
    i = 0
    prime  = 0
    run = True
    while run: #prints largest prime factor by counting down from sqrt of number and checking if its prime.
        if check_prime(n-i):
            if number % (n-i) == 0:
                prime = n-i
                print(prime)
                run = False
                break
        i +=1
        
largest_factor(600851475143)

#Plays a sound when program is done running.
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 5000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
