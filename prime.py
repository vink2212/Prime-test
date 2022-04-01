print("program start")
from math import floor


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
    n = floor(number**0.5)
    i = 0
    prime = 0
    run = True
    while run:
        if check_prime(n - i):
            if number % (n - i) == 0:
                prime = n - i
                print(prime)
                run = False
                break
        i += 1


largest_factor(300)


