
'''print "Hello World!"
print "Hello Again"
print "I like ytping this."
print "This is fun."
print "Yay! Printing."
print "i'd much rather you not"
print 'I "said" do not touch this.'
'''


# -----------Commets and compound characters--------------

# print("I could have code like this.")  # and the comment after is ignored

# ------------Numbers and math--------------

# print("I will now count my chickens:")

# print("Hens"), (23 + 30 / 5)
# print("Roosters"), (100 - 25 * 3 % 4)

# print("Now I will count the eggs:")

# print(3 + 3 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# print(" is it true that 3 + 2 < 5 - 7?")

# print(3 + 2 < 5 - 7)

# print("What is 3 + 2?", 3 + 2)

# -------------------Variables and Names-----------------

# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passangers_per_car = passengers / cars_driven

# print("There are", cars, "cars available.")
# print("There are only", drivers, "drivers available.")
# print("There will be", cars_not_driven, "empty cars today.")
# print("We can transport", carpool_capacity, "people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", average_passangers_per_car, "in each car today.")

# -------------Variables and Prints--------------

# my_name = "Zed shaw"
# my_age = 35
# my_height = 45
# my_weight = 140
# my_eyes = 'Blue'
# my_teeth = 'white'
# my_hair = "Brown"

# print("let's talk about %s." % my_name)
# print("He's %d inches tall." % my_height)
# print("He's %d pound heavy." % my_weight)
# print("Actually thats not too heavy")
# print("He's got %s eyes and %s hair" % (my_eyes, my_hair))
# print("His teeth are usually %s depending on the coffee." % my_teeth)

# print("If I add %d, %d, and %d I get %d" % (
#     my_age, my_height, my_weight, my_age + my_height + my_weight))

# ------------Strings formatings--------------

# binary = "binary"
# do_not = "don't"
# x = ("There are %d types of people." % 10)
# y = ("Those who know %s and those who %s." % (binary, do_not))

# print(x)
# print(y)
# print("I said so: %r." % x)
# print("I also said: '%s'." % y)


# hilarius = False
# joke_evaluation = "I'ts a funny joke? %r"
# print(joke_evaluation % hilarius)

# w = ("This is the left side of...")
# e = ("a string with a right side.")
# print(w + e)

# ----------------MORE PRINTING----------

# print("Mary had a little lamb.")  # print statement
# print("Its fleece was white as %s" % 'snow')  # place 'snow' in %s
# print("And everywhere that mary went.")
# print("." * 10)  #print dot 10 times

# end1 = "C"
# end2 = "H"
# end3 = "E"
# end4 = "S"
# end5 = "S"
# end6 = "E"
# end7 = "B"
# end8 = "U"
# end9 = "R"
# end10 = "G"
# end11 = "E"
# end12 = "R"

# print(end1 + end2 + end3 + end4 + end5 + end6)        #Each variable is printed by concatination
# print(end7 + end8 + end9 + end10 + end11 + end12)


# -----------------MORE FORMATTER------------

# FORMATTER = "%r %r %r %r "

# print(FORMATTER % (1, 2, 3, 4))
# print(FORMATTER % (FORMATTER, FORMATTER, FORMATTER, FORMATTER))
# print (" I had this thing\n",
#         "that you could type up right\n",
#         "But it didn't sing.\n",
#         "So I said goodnight.\n")


# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nMarch\nApril\nMay\nJune"

# print("Here are the days:{}".format(days))
# print("Here are the months:{}".format(months))

# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."

# fat_cat = """
# I'll do a list :
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass

# """
# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)


# -------------------ASK QUESTIONS--------------

# print("How old are u")
# age = input()
# print("How tall are u")
# my_height = input()
# print("How much do you weigh")
# my_weight = input()

# print("so you are {}y old, {}m tall, {}pound heavy".format(
#     age, my_height, my_weight))


# -------------PARAMETERS UNPACKING AND VARIABLES-------------

# from sys import argv

# script, first, second, third = argv

# print('the script is called', script)
# print('the first is called', first)
# print('the second is called', second)
# print('the third is called', third)

# ------------PROMPTING AND PASSING-----------

# from sys import argv

# script, user_name = argv
# prompt = '> '

# print('Hi {}, Im the {} script'.format(user_name, script))
# print("I'd like to ask you a few questions.")
# print("Do your like me {}".format(user_name))
# likes = input(prompt)

# print("Where do you live {}".format(user_name))
# lives = input(prompt)

# print("What kind of computer do you have?")
# computer = input(prompt)

# print('''Alright, so you said {} about liking me.
#         You live in {}. Not sure where that is.
#         And you have a {} computer. Nice.'''.format(likes, lives, computer))

# --------------READING FILES-----------------

# from sys import argv
# script, dummy = argv


# file = open("dummy.txt")    # open the dummy file as a reading
# print("Here is your file: %r" % dummy)
# print(file.read())

# open_file_again = input("Open the file again> ")
# open_file_again = open(open_file_again)  # Open the dummy file again
# print(open_file_again.read())  # Print this function

# -------------READ FILES PART 2-----------------

# import argv module
# from sys import argv

# script, test = argv

# print("We are going to erase %r." % test)
# print("If you don't want that hit CTRL-Z (^Z) and press ENTER.")
# print("If you do want that, hit ENTER")

# input("Press enter to continue > ")

# # opens the file and ask for to write new data in the given file
# print("Opening the file....")
# target = open("test.py", 'w')

# # This line clears the data within a file
# print("Terminating the existing data within a file. goodbyee...")
# target.truncate()

# print("Now im going to ask you for three lines.")

# lines1 = input("line 1: ")
# lines2 = input("line 2: ")  # This section ask for data input in a file
# lines3 = input("line 3: ")

# print("I'm going to write these to the file.")

# target.write(lines1)
# target.write("\n")        # To line 242 to 250 is going to write the new data in a file
# target.write(lines2)
# target.write("\n")
# target.write(lines3)
# target.write("\n")

# print("And finally, we close it.")  # And finally it will close the file...
# target.close()


# -------------MORE WORKING WITH FILES----------------

# imported a new module called exists which return a bool statement
# from sys import argv
# from os.path import exists

# script, test, dummy = argv

# print("Copying from %s to %s" %(test, dummy))

# ------>This line open the mentioned file and read the data within a file
# in_file = open("test.py")
# indata = in_file.read()

# ---->This section tells us about the file size and use the exist method to
# -----> to find out if the dummy file exist or not with the help of bool
# print("Does the output file exist? %r" % exists(dummy))
# print("The input file is %d bytes long" % len(indata))
# print("Ready, hit ENTER to continue, CTRL-Z to abort")

# input()

# ------>This line opens the dummy file write the copied data into dummy file
# out_file = open("dummy.txt", 'w')
# out_file.write(indata)

# print("Alright, all done")

# out_file.close()
# in_file.close()  -----> finally close both dummy and test file


# ----------MIX CODE WITH NAMES, VARIABLES, CODE AND FUNCTIONS-----------

# def print_two(*args):
#     arg1, arg2 = args
#     print("arg1: %r, arg2: %r" % (arg1, arg2))  ------->Line 288 to 294 are same function with different method


# def print_two_again(arg1, arg2):
#     print("arg1: %r, arg2: %r" % (arg1, arg2))


# def print_one(arg1):
#     print("arg1: %r" % arg1)   ----->This section print single argument


# def print_none():
#     print("I got nothing")   ------->This section print the string


# print_two("pushpinder", "singh")
# print_two_again("pushpinder", "singh")
# print_one("First!")
# print_none()

# FUNCTIONS AND VARIABLES

# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print("You have %d chesses" % cheese_count)
#     print("You have %d box of crackers" % boxes_of_crackers)
#     print("Man that's enough for a party")
#     print("Get a blanket.\n")


# print("We can just give the function numbers directly")
# cheese_and_crackers(20, 30)

# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)

# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# FUNCTIONS AND  FILES

from sys import argv

script, dummy = argv


def print_all(f):
    print(f.read())  # ------> opens the file to as reading


def rewind(f):
    print(f.seek(0))  # ------>opens the file to choose specific line


# ------>choose the first three lines and print them
def print_a_line(line_count, f):
    print(line_count, f.readline())


print("First let's print the whole file:\n")

current_file = open("dummy.txt")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
print("let's print three lines:")

rewind(current_file)  # ------>call the rewind function
line_count = 1


# ---->This section print the first three lines with calling print_a_line function
print_a_line(line_count, current_file)
line_count = line_count + 1
print_a_line(line_count, current_file)
line_count = line_count + 1
print_a_line(line_count, current_file)
