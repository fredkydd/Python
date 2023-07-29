# print is the same as JavaScript's console.log()
print("Hello World! 0\nHello World! 1\nHello World! 2")
print("Hello" + " " + "Angela")
print("Hello " + "Angela")
print("Hello" + " Angela")
# This triple single or double quotes are used for multi line comments like JavaScaript's backtick
print(
    """
  Hello There Triple double quotes for multi-line comments
  I'm the second line of the string
  I'm the third line of the string
"""
)

print(
    """
  Hello There Triple single quotes for multi-line comments
  I'm the second line of the string
  I'm the third line of the string
"""
)

# input is the same as JavaScript's prompt()
input("How old are you ?")
print("Hello " + input("What is your first name?") + "!")

# len() is the same as JavaScript's .length() function
print(len(input("What is your name? ")))

# variables are dynamics as JavaScript's let and var keyword. Thehy can be reassign and redeclare
firstName = "Illusion"
secondName = "Fancy"
fullName = firstName + " " + secondName
fullName = "My full name is " + fullName
length = len(fullName)
print(length)
