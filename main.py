# name = input("What is Your Name ?")
# print(name)
 #####################################################################################################################

# Wap to Find your current Age

# birth_year = input("Enter Your Birth Year ")
# current_year = input("Enter the current year hue")
# age = int(current_year) - int(birth_year)   #this is called type Casting /
# print(age)
# print(f'His age is {age}')

######################################################################################################################

# WAP to Change the User Weight in KG

# weight = input("Enter your Weight in KG:")
# weightInP = int(weight)*2.204
# print("your weight in pound is :",weightInP,'lbs')
# print(f'your weight in pound is :{weightInP}lbs')
#

 #####################################################################################################################

 # WAP to Print in Different Line

# Course='''
# Fundamental Of React
# JavaScript
# JSX
# Props
# States
# Complex States'''
#
# print(Course)

######################################################################################################################

# WAP to Print in Lower and upper Case


# Course='''
# Fundamental Of React
# JavaScript
# JSX
# Props
# States
# Complex States'''
#
# print(Course.upper())
# print(Course.lower())
# print(Course.title())

######################################################################################################################

# WAP to Print in Lower and upper Case

# Course="Its me Sandesh Khanal"
#
# print(Course[0])
# print(Course[-1])
# print(Course[3:8])
# print(Course[3:]) # Print Without some letters from first
# print(Course[:2]) # print some letters
# print(Course.find('a'))
# print(Course.replace('Sandesh','MrSandesh'))

##################################################################################################################

# Arthemetic operation
#
# print(8+3)
# print(9-8)
# print(2*200)
# print(2/3)
# print(5%2)
# print(2**3)
# print(5//2)
# print(7//3)
#
# x = 10
# x = x + 1
# x += 1
# print (x)
#
# print (2+3*5-4)
# print((2*3)*5-4/2**2)

# Braket >> ** >> division >> multiply >>plus >> minus

##################################################################################################################

#  if & else

# is_hot = False
# if is_hot==True:
#     print('its a hot day')
#     print('drinl plenty of water')
# elif is_hot==False:
#     print("its a cold day ")
#     print("wear warm clothes ")
# else:
#     print("It's neither hot nor cold")
#     print("Enjoy your day")

##################################################################################################################

# a = 10
# b = 20
# c = input("Enter the number")
# if int(c)>a and int(c)<b:
#     print("Number is  valid ")
# else:
#     print("invalid")


##################################################################################################################

 # Program to enter the 8 digit username and password

# username = input("Enter your username here:")
# if username == 'sandesh':
#     print('Enter your password:')
# else:
#     print('Only our reputed manager Mr Sandesh khanal can login')
#     exit()
#
# password = input()
# if len(password)<8:
#     print('The password must be at least 8 characters')
# elif len(password)>10:
#     print('The password must below 10 characters')
# else:
#     exit("""Your data is hacked
#     Contact 9812322590 to get your data back  """)


##################################################################################################################

# weight = input('Please enter your weight:')
# final_weight= input('Please enter 1 to get your weight in kg and Enter 0 to get your weight in Pound ')
# if(int(final_weight)==1):
#     print('your weight  in pound  is ', int(weight) * 2.204)
# elif(int(final_weight==0)):
#     print('your weight in kg is ', int(weight)/2.204)
# else:
#     print('Invalid input ')

##################################################################################################################


# i = 7
# while i < 5:
#     print(i)
#     i+=1
# exit('Nasa is hacked by ME')


##################################################################################################################
secret_number = 3
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess = int(input('Enter your guess number'))
    guess_count= guess_count +1
    if guess == secret_number:
        print('Congratulations you are the winner')
        break
    else:
        print('Incorrect , you have', guess_limit-guess_count,'guesses left')
else:
    exit('You failed!!')

