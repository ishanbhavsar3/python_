
Num_List = 1, 2, 3, 4
print(Num_List)
Day_of_week_num = input("Input the day of the week  in numbers and i will tell which day it is.")
int(Day_of_week_num)
if int(Day_of_week_num) == 1:
    print("The day is a Sunday.")
elif int(Day_of_week_num) == 2:
    print("The day is a Monday.")
elif int(Day_of_week_num) == 3:
    print("The day is a Tuesday.")
elif int(Day_of_week_num) == 4:
    print("The day is a Wednesday.")
elif int(Day_of_week_num) == 5:
    print("The day is a Thursday.")
elif int(Day_of_week_num) == 6:
    print("The day is a Friday")
elif int(Day_of_week_num) == 7:
    print("The day is Saturday.")
else:
    print("The number you inputted is not a day of the week or within 7.")







num_input = input("Input a number to test if it is odd or even.")
if int(num_input) % 2 == 0:
    print(f"The number {num_input} is even.")
    print(f"The number {num_input} gives a 0 as a remainder when divided with 2.")
else:
    print(f"The number {num_input} is odd ")
    print(f"The number {num_input} does not give remainder as 0 when divided with 2.")

# Spacing between lines of code.

Guess_Number = 1
while Guess_Number <= 5:
    print(Guess_Number)
    Guess_Number = Guess_Number + 1

# Spacing between lines of code.

Guess_Number = 1
while Guess_Number <= 1:
    print('*' * Guess_Number)
    Guess_Number = Guess_Number + 1

# Spacing between lines of code.

secret_Number = 9
Guess_Number = 0
while Guess_Number < 3:
    Guess_Input = int(input("Guess a number from 1 to 10 and input it here."))
    Guess_Number += 1
    if Guess_Input == secret_Number:
        print("You won the prize.Well Guessed!")
        break
else:
    print("Sorry,you failed!")

    # Spacing between lines of code.
    # While Loop Up and IfElseElif Down.

price1 = 1000
print(f"The price of the property is ${price1}")
int(price1)
if_cred_good = False
down_p = 0.1*int(price1)
if_cred_bad = True
down_p1 = 0.2*int(price1)

if if_cred_good:
    print(f"Your down payment is ${down_p}")
elif if_cred_bad:
    print(f"Your down payment is ${down_p1}")
else:
    print("You are not buying the house.")

# IfElseElif Practice 1.
# Spacing between two files.

name = "This is a girl"
if_name = False
messages = "Ishan is a boy."
if_messages = True
if if_messages:
    print(messages)
elif if_name:
    print(name)
else:
    print("404 Not Found")

# IfElseElif Practice 2.
# Spacing between two files.

is_hot = False
is_cold = True
if is_hot:
    print("The day is hot.")
    print("Wear cotton clothes.")
    print("Drink plenty of water.")
elif is_cold:
    print("The day is cold.")
    print("Wear warm clothes.")
else:
    print("It is a lovely day.")

# IfElseElif Practice 3.
# Spacing between two files.

is_new = True
if is_new:
    print("The thing is new")
    print("I hope you are happy.")
else:
    print("The thing is old")
    print("It's common to be unhappy.")

# IfElseElif Practice 4.
# Spacing between two files.

price = 1000000
print(f"Price of the property is ${price}")
is_credit_good = True
if is_credit_good:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Your Down Payment will be: ${down_payment}")

# IfElseElif Practice 5.
# Spacing between two files.

price1 = 2000000
print(f"Price of property is ${price1}")
is_credit_bad = True
if is_credit_bad:
    down_payment1 = 0.2 * 20000000
else:
    down_payment1 = 0.1 * 20000000
print(f"Your down payment is: ${down_payment1}")
is_nice = True
if is_nice:
    print("The file is nice")
else:
    print("The file is not nice")
print('''The file is good is an if/else option which occurs due to presence of boolean values who are true or false
The boolean value in this case is true therefore the file is nice gets printed.
Its printing is dependant upon the  boolean value is_nice.''')
print("The person making the file is Ishan Bhavsar.")

# IfElseElif Practice 6.
# Spacing between two files.

Ishan_Is_A_Boy = True
if Ishan_Is_A_Boy:
    print("Ishan is a boy")
else:
    print('Ishan is a girl.')

print("Differentiating files start.")
# Spacing between lines of code
# Made on 16th March 2020.
# Day : Monday.
# Event Updation at 8:17 P.M.
print("Welcome to differentiating files.")

print(
    '''WELCOME!!!!'''
)

weight_in_kg = input("Please input your weight to get it converted to pounds: ")
int(weight_in_kg)

weight_in_pounds = int(weight_in_kg) * 0.45
int(weight_in_pounds)
print(f"{weight_in_pounds} is your weight in pounds.")

# Spacing between lines of code.

distance_in_km = input("Input distance of journey in kms to know it in miles: ")
int(distance_in_km)
distance_in_miles = int(distance_in_km) * 0.621371
int(distance_in_miles)
print(f"{distance_in_miles} is the distance of your journey in miles.")

# Spacing between lines of code.

temperature = input("Input today's temperature(!!!in numbers only!!!): ")
int(temperature)
if int(temperature) >= 30:
    print("The day is hot.")
else:
    print("The day is not hot.")

# Spacing between lines of code.

has_high_income = input("Do you have high income? Reply in 'True' or 'False' only. ")
has_criminal_record = input("Do you have any criminal record? Reply in 'True' or 'False' only. ")
has_high_credit = input("Do you have high credit? Reply in 'True' or 'False' only. ")

bool(has_high_income)
bool(has_criminal_record)
bool(has_high_credit)


one = input('Your loan value is: ')
int(one)
if has_high_credit and not has_criminal_record:
    print(f"You are eligible for the loan of $ {one}.")
else:
    print(f"You are not eligible for the loan of $ {one}")

# Spacing between lines of code.

if has_high_credit and has_high_income:
    print(f"You are eligible for the loan of $ {one}")

# Spacing between lines of code.

name_of_man = input("What is your name?")
if len(name_of_man) < 3:
    print("Your name is too short.")
elif len(name_of_man) > 50:
    print("Your name is too long.")
else:
    print("Your name is of good size.")

# Spacing between lines of code.

is_your_car_new = input("Is your car new(True/False)")
is_your_car_middle_aged = input("Is your car middle aged?(True/False)")
bool(is_your_car_new)
bool(is_your_car_middle_aged)
if bool(is_your_car_new):
    print("You will get a good price for your car.")
elif bool(is_your_car_middle_aged):
    print("You will get a fair price for your car.")
else:
    print("Your car is old.So you will get a low price.")

name_of_car = input("What is the name of your car?")
str(name_of_car)

Review = input("Is this file good?(Yes/No)").upper()
Yes = "YES"
if str(Review) == Yes:
    print("Thank you for your good review.")
elif str(Review) == "NO":
    print("I will try to improve my software.Thank you.")
else:
    print("you have inputted something different than what i asked you to.")
    print("Input yes or no only.")
Tallest_Mountain = input("What is the name of the tallest mountain in the world?").upper()

if Tallest_Mountain == "MT.EVEREST":
    print(f"Your guess of {Tallest_Mountain} is indeed correct!")
elif Tallest_Mountain == "Godwin Austin Peak":
    print(f"Your input {Tallest_Mountain} is the second tallest mountain in the world.")
else:
    print("You have inputted some wrong information here.Please quit if you don't wish to continue the game.")







