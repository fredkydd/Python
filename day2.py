# DATA TYPES AND MANIPULATING STRINGS
# String  str()
print("Hello World!"[0])
name = "Fred"[-1]
print(name)
name = "Alice"[4]
print(name)

# Integer (Whole numbers) int()
print(123 + 456)
# 100000 = 100_000 we use underscore for LARGE INTEGER to understand it
print(100_000 + 50_000)
print(100000 + 50000)

# Float , Floating Point Numbers (Decimal Numbers)
print(8.11)

# Boolean (must be uppercase)
active = True
passive = False

# type() for cheking for types
myScore = len(input("what number is your IELTS score?"))
print(myScore)
print(type(myScore))
print(type(9.5))
# 👇 this would givce us an error because we cant concatinate different types
# print('my IELTS score is ' + myScore + '!')

fNum = float("5.7")
# 👇str() int() float() converting data types to their names
print(str(5) + str(7) + str(fNum))  # 575.7
print(int("56") + int(5.7) + 7)  # 68
print(float("5") + float(5) + 5.8)

# TASK
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
firstNum = int(two_digit_number[0])
secondNum = int(two_digit_number[1])
print(firstNum + secondNum)
