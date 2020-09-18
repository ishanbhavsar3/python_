length_of_rect = input("Input the length of a rectangle in numbers only.")
breadth_of_rect = input("Input the breadth of rectangle in numbers only.")

int(length_of_rect)
int(breadth_of_rect)

print(f"The length of your rectangle is {length_of_rect} unit")
print(f"The breadth of rectangle is {breadth_of_rect} unit")

perimeter_of_rect = 2 * (int(length_of_rect)+int(breadth_of_rect))
print(f"The perimeter of a rectangle with length {length_of_rect} and breadth {breadth_of_rect} is {perimeter_of_rect}")

area_of_rect = int(length_of_rect) * int(breadth_of_rect)
print(f"{area_of_rect} is the area of the rectangle with length of {length_of_rect} and breadth of {breadth_of_rect} ")

PIE = 3.141
Radius = input("Input a radius in float type (fractional part)")
area_circle = (float(Radius)*float(Radius))*PIE
print(f"The area of the circle having radius {Radius} units is {area_circle} square units.")

Radius = input("Input a radius in int type (base 10)")
area_circle_int = (int(Radius)*int(Radius))*PIE
print(f"The area of the circle having radius of {Radius} units is {area_circle_int} square units.")


math = [1, 2, 3, 5, 7, 20]
print(math[-1])
print(len(math))
if len(math) == 4:
    print("The number of values in math variable is 4.")
else:
    print("The number of the value iss not 4")
num_input = input("Input a number to test if it is odd or even.")
int(num_input)
if int(num_input) % 2 == 0:
    print(f"The number {num_input} is even.")
else:
    print(f"The number {num_input} is odd ")

Messages = "You are a good man."
print(Messages.replace('You', 'I'))
print(Messages.lower())
print(Messages.upper())
print(Messages.capitalize())
print(Messages[0:0])
print(Messages.center(100))
print(len(Messages))
squares = [2, 4, 9, 16, 25]
squares[0] = 1
print(squares)
print('''!!!!DISCLAIMER!!!!
!!!!DISCLAIMER!!!!
This is the personal data of Ishan Bhavsar and you will be booked if u try to copy it.
''')
print('This is not a very good Python file.')
print('+____+')
print('|    |')
print('|    |')
print('*' * 6)
price = 20
print(price)
rating = 4.9
print(rating)
deci_value = 99.99
print(deci_value)
name = 'Ishan'
print('Ishan' in name)
is_published = True
print(name)
print(price)
name = 'John Smith'
print(name)
age = 20
print(age)
is_new = True
print(rating)
print('You seem interesting to me.')
print("Let's talk more.")
name = input('What is your name? ')
fav_color = input('What is your favourite color? ')
print(name + 'likes' + fav_color)
print(f'{name} likes {fav_color}')

birth_year = input('Birth Year: ')
age = 2020 - int(birth_year)

print(age)
print('is your precise age.')
birth_month = input('In which month were you born? ')

print(f'Oh I see!So you were born in {birth_month}')
parent_name = input('Name both your parents. ')
print(f'Your parents name is {parent_name}')
friend_name = input('Name any of your friend ')
friends_favcolor = input('What is the favourite color of your friend? ')
print(f'So, {friend_name} likes {friends_favcolor} color.')
cousin_name = input('What is the name of your cousin? ')
cousin_favcolor = input('What is the favourite color of your cousin? ')
cousin_gender = input('What gender is your cousin? ')
cousin_age = input('What is the age of your cousin? ')
print(f'So,the name of your cousin is {cousin_name},their favourite colour is {cousin_favcolor} and, ')
print(f'the gender of your cousin is {cousin_gender},while their age is {cousin_age}.')
rough_typing = input('Type anything roughly and it will be printed by the computer on pressing enter.')
print(f'{rough_typing} is what you have typed roughly.')
print('''
Hello World!

Ishan Bhavsar here.
''')
king_name_bhutan = input('What is the name of the king of Bhutan? ')
print(f'{king_name_bhutan} is the name of the King of Bhutan according to you.')
hindu_name = 'Amar'
muslim_name = 'Akbar'
christian_name = 'Anthony'
print(f'The Hindu name (A) {hindu_name},the Muslim one is {muslim_name} while the Christian Name is {christian_name}.')
print("This is Ishan Bhavsar making his first python file.")
print("[111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111]")
Do_you_know_me = input("Do you know who is Ishan Bhavsar(Yes or No only!)")
print(f'{Do_you_know_me} ,you know/you do not know Ishan Bhavsar')
weight_lbs = input('Weight in pounds: ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
last_prompt = input('It is  the last input i am making.After This,im gonna learn something new.(True or False?) ')
print(last_prompt)
a = 90
print(a)
print('Type in marks out of 100 to get a percentage in a subject. ')
marks_div_100 = input('Please input your marks only. ')
sub_percentage = int(marks_div_100) * 1
print(sub_percentage)
first_name = 'John'
last_name = '[Smith]'
message = f'{first_name} {last_name} is a coder.'
print(message)
print(len(message))
print('coder' in message)
friend_first_name = input("What is your friend's first name? ")
friend_name_2 = f"So, {friend_first_name} is your friend's first name."
print(friend_name_2)
print(len(friend_name_2))
print('''
Hello there!

hope you are enjoying typing in things to my files or giving inputs to it!

If not,then leave the file!

it's quite simple to do so.
Click the red button with x on the top and exit my file.
Bye!

Regards,
Ishan Bhavsar.
''')
last_minute_of_videos = 'At Forty-five minutes and twenty-ninth second of Code with mosh python for beginners video.'
print(f"{last_minute_of_videos} was where u left watching mosh's tutorials u r taking for learning python.")
name_2_Practice = 'English is the language in which i study at my school.'
address_2_practice = "I live in Mumbai,Maharashtra and my school's name is Children's Academy."
print('study at my school' in name_2_Practice)
print("Children's Academy" in address_2_practice)
nonsense_just_for_practice = 'India currently has no king.It is a democratic state ruled by the people of the country.'
print(nonsense_just_for_practice.upper())
print(nonsense_just_for_practice.lower())
print(nonsense_just_for_practice.find('d'))
print(nonsense_just_for_practice.find('democratic'))
print('India' in nonsense_just_for_practice)
print(nonsense_just_for_practice.replace('India', 'I'))
print('This is my first python file.')
file_is_new = True
course = 'python for beginners'
print(course.replace('beginners', 'absolute beginners'))
print(course[:])
Indian_string = 'This is the Indian String made by Ishan Bhavsar'
print(Indian_string[0:7])
print(Indian_string.replace('Ishan Bhavsar', 'An Anonymous Guy'))
print(Indian_string.find('I'))
print('This is the king of nowhere,Ishan Bhavsar.')
timepass = input('What do you do for timepass? ')
print(f'Oh,I see.For timepass, you {timepass}')
just_for_fun = input('What are You?A doctor,engineer,what? ')
print(f'{just_for_fun},I see.')
TheKing = input('Wht?!!')
print(f'{TheKing} is 1')

print("This is Ishan's error free file.")
print(''' Hello there!
This is Ishan Bhavsar's first python file.

I know you are  enjoying going through it, 
 if not then you are welcome to leave it.

 press the red button in the top right corner with a cross to leave.
 Bye if you are leaving!
 ''')
Lordship = input('''What is your name?

When is your birthday?

When is your parent's birthday?

That's all I require.

''')
print(f''' {Lordship} 

This is what you typed in inside Lordship.

''')
Kingliness = input('This is a good or a bad file?')
print(f'It is a {Kingliness} file.Thank you for the review.')
print(f'''These are all the inputs I made: 
{timepass}
{name}
{name_2_Practice}
{christian_name}
{cousin_name}
{first_name}
{friend_first_name}
{friend_name}
{friend_name_2}
{friends_favcolor}
{hindu_name}
{muslim_name}
{last_name}
{last_minute_of_videos}
{king_name_bhutan}
{last_prompt}
{Do_you_know_me}
{Indian_string}
{rough_typing}
{cousin_age}
{cousin_favcolor}
{cousin_gender}
{birth_month}
{birth_year}
{fav_color}
{just_for_fun}
{parent_name}
{TheKing}
{Lordship}
{Kingliness}
{Radius}
{area_circle_int}
{area_circle}
{area_of_rect}
{marks_div_100}
{length_of_rect}
{breadth_of_rect}
{PIE}
''')
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 ** 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
x = 10 * 3 + 2
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
z = 3.33
print(round(z))
import math

a = 2.9
print(math.ceil(a))
print(math.floor(a))
print("This is Ishan Bhavsar's File.")
print(input("What is your name?"))

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
# The file is set to end.
print("This is Ishan Bhavsar's file")
print('Goodbye!')
is_good = input("Is it good?(True/False)")
if is_good:
    print("It is good.")
else:
    print("It is bad.")
# This marks the probable end of this python file
print("I don't know why i am learning python.")
pancakes = input("Why are you in my file?")
print(f"Oh so you are in my file to {pancakes}.")
math_num_array = [1, 2, 3, 4, 5]
print(math_num_array)
if math_num_array[2] == 2:
    print(f"The second number of {math_num_array} is 2.")



print("My name is Lakhan...")
nigga = input("Hey...wassup")

print(nigga)


