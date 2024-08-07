
import random

user_input = ""

def generate_random_number():
    return random.randint(1, 1000)

def store_user_input(input_string):
    global user_input
    user_input = input_string
    return user_input
