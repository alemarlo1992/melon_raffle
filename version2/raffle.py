"""Randomly pick customer and print customer info"""

import random 
from customers import get_customers_from_file 

def raffle_winner(customers):

    winner = random.choice(customers)

    print('The winner is {name} and their email is {email}'.format(name=winner.name, email=winner.email))

def weekly_raffle():

    customers = get_customers_from_file('customers.txt')
    raffle_winner(customers)

if __name__ == "__main__":
    weekly_raffle()

# Hint: remember to import any functions you need from
# other files or libraries
