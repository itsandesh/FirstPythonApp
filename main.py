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

# Bracket >> ** >> division >> multiply >>plus >> minus

##################################################################################################################

#  if & else

# is_hot = False
# if is_hot==True:
#     print('its a hot day')
#     print('drink plenty of water')
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
# secret_number = 3
# guess_limit = 3
# guess_count = 0
#
# while guess_count < guess_limit:
#     guess = int(input('Enter your guess number'))
#     guess_count= guess_count +1
#     if guess == secret_number:
#         print('Congratulations you are the winner')
#         break
#     else:
#         print('Incorrect , you have', guess_limit-guess_count,'guesses left')
# else:
#     exit('You failed!!')

#######################################################################################################################
#
# command_count = 0
# while command_count == 0:
#
#     command = input('''
#     Enter  1 to start the car
#     Enter  2 to stop the car
#     Enter  3 for help
#     Enter  4 to quit  : ''')
#     command_count  += 1
#     if int(command) == 1:
#         print('Your car is started ')
#     elif int(command) == 2:
#         print('Your car is stopped ')
#     elif int(command) == 3:
#         print('''
#               Enter  1 to start the car
#               Enter  2 to stop the car
#               Enter  4 to quit  ''')
#     elif int(command) == 4:
#         exit('you quit')
#     else:
#         print('Please Enter the correct Number')
#
# while command_count == 1:
#     command = input('''
#     Enter  1 to start the car
#     Enter  2 to stop the car
#     Enter  3 for help
#     Enter  4 to quit  : ''')
#     if int(command) == 1:
#         print('You fool your car is already started  ')
#     elif int(command) == 2:
#         print('Your car is already  stopped ')
#     elif int(command) == 3:
#         print('''
#         Enter  1 to start the car
#         Enter  2 to stop the car
#         Enter  4 to quit  ''')
#     elif int(command) == 4:
#         exit('you quit')
#     else:
#         print('Please Enter the correct Number')
#
#
#
# Started= False
# while  True:
#
#     command = input('''
#     Enter  1 to start the car
#     Enter  2 to stop the car
#     Enter  3 for help
#     Enter  4 to quit  : ''')
#
#     if int(command) == 1:
#         if Started:
#             print('Car has been already started')
#         else:
#             print('Car started')
#             Started = True
#
#     elif int(command) == 2:
#         if not Started:
#             print('Car has been already stoppd')
#         else:
#             print('Car stopped')
#             Started = False
#
#     elif int(command) == 3:
#         print('''
#               Enter  1 to start the car
#               Enter  2 to stop the car
#               Enter  4 to quit  ''')
#     elif int(command) == 4:
#         exit('you quit')
#     else:
#         print('Please Enter the correct Number')



# for i in 'student':
#     print(i)
#
# for i in [1,2,3,4,5,6]:
#     print(i)
#
# for i in range(1 ,5,8):
#     print(i)

# sum = 0
# for i in [1000,2222,44444,4444]:
#     sum += i
#     print(sum)
#
# for x in range(5):
#     for y in range(3):
#         print(f'{x},{y}')

#######################################################################################################################

#Make Nepal Flag

# list1 = [1,3,5,6,7,9,]
# for num in list1:
#     Stri=''
#     for i in range(num):
#         Stri += 'x'
#     print(Stri)
# for num in list1:
#     Stri=''
#     for i in range(num):
#         Stri += 'x'
#     print(Stri)





#######################################################################################################################

# list1 = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1  ]
# # for i in list1:
# #     print('x'*i)
#
# for num in list1:
#     Stri=''
#     for i in range(num):
#         Stri += 'x'
#     print(Stri)

#######################################################################################################################

#Wap to create a QR code.

# import qrcode
# img = qrcode.make("https://youtu.be/c0yEm1BtBmY")
# img.show("Techno_sandesh.jpg")

#######################################################################################################################


# from datetime import datetime
#
# # now() method is used to
# # get object containing
# # current date & time.
# now_method = datetime.now()
#
# # strftime() method used to
# # create a string representing
# # the current time.
# currentTime = now_method.strftime("%H:%M") #  %S to get the seconds value
# print("Your current Time is ", currentTime,'O clock')

#########################################Lists#############################################################################

# list1 = [1,2,3,4,5,8]
# for item in list1:
#     print(item)
#     # print(list1[item])
#
# list1 = [1,2,3,4,5,8]
# max = 0
# max = list1[0]
# for item in list1:
#     if item>max:
#         max=item
# print(max)

###################################################    Matrix         ###################################################################

# matrix =[[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# print(matrix)
# print(matrix[0])
# print(matrix[0][2])
# for row in matrix:
#     for item in row:
#         print(item)

###############################################      LIST             ########################################################################
#
# list1 = [1,2,3,4,5,8]
# list1.append(9)
#
# list1.insert(0,0)
# print(list1)
#
# list1.remove(8)
# print(list1)
# print(list1.count(2))
#
# list1.sort()
# print(list1)
#
# list1.reverse()
# print(list1)


# list= [1,2,3,4,5,6,3,5,6]
# list1=[]
# for item in list:
#     if item not in list1:
#         list1.append(item)
# print(list1)

################################################     Tuple          ######################################################################

# tuple = (1,2,3,4,5)
# print( tuple.index(2))
# print(tuple.count(3))
# print(tuple.reverse())


###############################################    Dictionary        ################################################################

# customer = {
#     "name": "ram",
#     "age" : 20,
#     "city" : "KTM"
# }
# print(customer)
# print(customer["name"])
# customer["name"] = "shyam"
# print(customer["name"])
# customer["lName"] = "kandariya"
# print(customer)
# print(customer.get("name"))
# print(customer.get("phone_number",987654321))   # best way

##############################################     Function in Dictionary      ##########################################################################

# Numbers = {
#     "0":"zero",
#     "1": "one",
#     "2":"two",
#     "3":"Three",
#     "4":"Four",
#     "5":"five",
#     "6":"six",
#     "7":"seven",
#     "8":"Eight",
#     "9":"nine"
# }
#
#
# Number = input("Enter the numbers")
# output=""
# for num in Number:
#     output +=Numbers.get(num ,"*")+" "
# print(output)
#

 ###########################################################  Function   ###################################################################

# def greet_user(name):
#     print("Hi ")
#     print(f"I am {name}")
# print("start")
# greet_user("sandy")
# greet_user("Puri")
# print("stop")

#
# def greet_user(f_name,l_name):
#     print("Hi ")
#     print(f"I am {f_name} {l_name}")
# print("start")
# greet_user("sandy","bhatt")
# greet_user("Puri","pri")
# print("stop")

############################################### return type in function #############################################################

# def square(number):
#     return number*number
#
# num = 9
# result = square(num)
# print(result)


############################################################   Class  ###########################################################

# class Point:
#     def __init__(self ,x,y):
#         self.x =x
#         self.y =y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
# point1 = Point(10,200)
# # point1.move()
# # point1.x = 10
# point1.y = 20
# # point2 = Point()
# # point2.x = 10
# # print(point2.x)
# print(point1.x,point1.y)

#######################################################     INHRITENCE #################################################################
class Person :

    def __init__(self,name):
        self.name= name

    def talk(self):
        print(f"i am {self.name}")


ram = Person("ram")
ram.talk()

shyam = Person("shyam")
shyam.talk()



class Mammel():
    def walk(self):
        print("walk")

class Dog(Mammel):
    def bark(self):
        print("bark")

class Cat(Mammel):
    def meow(self):
        print("meow")

tommy = Dog()
tommy.walk()

tom = Cat()
tom.meow()
tom.walk()
