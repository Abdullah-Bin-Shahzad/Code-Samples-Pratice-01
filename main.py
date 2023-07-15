import random #using in random number guess game


# This is a Grade Calculor

'''Grade Calculator:
Write a program that takes a numerical grade as input and uses match cases 
to determine the corresponding letter grade. 
For example, if the input is 85, the program should output "B". 
Consider using match cases for grade ranges like "90-100: A", "80-89: B", etc.'''

# Thing we need to know
# 1. Number as a input
# 2. Use match case

#Taking numerical grade as a input
score=int(input("Enter you total marks: "))
#matching score using case and if
match score:
    case _ if 100>=score>=90:
        print("Your grade is A")
    case _ if 80<= score < 90:
        print("Your grade is B")
    case _ if 70<= score < 80:
        print("Your grade is C")
    case _ if score <=69:
        print("Your grade is D")

''''----------------------------------------------------------'''

'''Leap Year Checker:
Create a program that prompts the user to enter a year and uses match cases 
to determine whether it's a leap year or not. 
Use if-else statements for the following conditions:

If the year is divisible by 4, it is a leap year, unless...
If the year is divisible by 100, it is not a leap year, unless...
If the year is divisible by 400, it is a leap year.'''

# Thing we need to know
# 1. Number as a input for user enter year
# 2. Use match case along with if-else

#Geting user input year as number 

year=int(input("Lets find if this is a leap year or not. Enter the year: "))

#Checking if the year is leap?
match year:
    case _ if year%4 == 0:
            print(year," is a leap year")
    case _ if year%100 == 0:
            print(year," is a leap year")
    case _ if year%400 == 0:
            print(year," is a leap year")
    case _:
            print(year," is not a leap year")   

''''----------------------------------------------------------'''

'''Calculator:
Build a basic calculator that performs arithmetic operations based on user input. 
Use match cases to identify the operation requested (+, -, *, /)
and perform the calculation accordingly. 
If the input doesn't match any of the specified cases, display an error message.'''


#Getting User Input

value1 = float(input("Enter First Number: "))
value2 = float(input("Enter Second Number: "))
operator = input("What operation do you want to perform (+, -, *, /): ")

match operator:
    case "+":
        result = value1 + value2
        print("Result:", result)
    case "-":
        result = value1 - value2
        print("Result:", result)
    case "*":
        result = value1 * value2
        print("Result:", result)
    case "/":
        result = value1 / value2
        print("Result:", result)
    

'''Number Guessing Game:
Develop a simple number guessing game where the computer generates a random number between 
1 and 100, and the user has to guess it. 
Use match cases or if-else statements to provide feedback to the user 
(e.g., "Too high!" or "Too low!") and track the number of attempts taken 
until the correct guess.'''



random_number = random.randint(0,100)
user_number=[]
number_of_attempt=0

while user_number!=random_number:
        
        user_number= int(input("Guess the number between 0 to 100: "))
        number_of_attempt= number_of_attempt+1
        match user_number:
        
            case _ if user_number<random_number:
                print("Try higher Number")
            case _ if user_number>random_number:
                print("Try low Number")
            case _:
                print("What you type and what you need to guess is matched which is: ", random_number)
       
print("Number of attempts: ",number_of_attempt)



'''BMI Calculator:
Write a program that calculates the Body Mass Index (BMI)
based on user input for weight and height.
Use match cases to categorize the BMI into different weight classes 
(e.g., "Underweight", "Normal Weight", "Overweight", "Obese") 
based on the following ranges:

BMI < 18.5: Underweight
18.5 <= BMI < 25: Normal Weight
25 <= BMI < 30: Overweight
BMI >= 30: Obese'''

#Getting user input weight(kg) and height(m)
print("Lets calculate your BMI")
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in Meter: "))
#Formula of BMI
BMI=weight/height*2

if BMI<18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal Weight")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obese")

''''''