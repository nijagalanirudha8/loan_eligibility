Basic code:

name = input("Enter your name\n")
print("Your name is", name)

age = int(input("Enter your age\n"))
print("Your age is", age)

grad = input("Enter if you have completed your graduation (yes or no)\n")
job = input("Enter if you are employed or not employed (yes or no)\n")

salary = int(input("Enter your salary\n"))
print("Your salary is", salary)

dep = int(input("Enter the number of dependents (number of people who depend on your salary)\n"))

cb = int(input("Enter the CIBIL score of yours\n"))
print("Your CIBIL score is", cb)

loan1 = int(input("Enter the loan amount you want\n"))

if age > 18 and grad == 'yes' and job == 'yes' and 575 <= cb <= 900:
    print("You are eligible to apply for loan")
    base_amt = (10 / 100) * salary
    ded = (0.05) * dep * base_amt
    loan2 = base_amt - ded
    loan2 = int(loan2)
    print("The loan amount sanctioned for", name, "of age", age, "is rupees", loan2)
else:
    print("You are not eligible for loan")
