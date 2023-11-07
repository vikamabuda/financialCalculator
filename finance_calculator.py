import math

user_investment = {"investment", "Investment", "INVESTMENT"}
user_bond = {"bond", "Bond", "BOND"}

print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("Investment - Calculate the amount of interest you'll earn on an investment")
print("Bond - Calculate the amount you'll have to pay for a home loan\n")

user_choice = input("Enter your choice here: ").capitalize()

if user_choice in user_investment:
    try:
        user_deposit_amount = float(input("What is the amount you are depositing?: "))
        interest_rate_input = input("What is the interest rate of your investment? (e.g., 7.7 or 7, not 7%): ")

        if "." in interest_rate_input:
            interest_rate = float(interest_rate_input)
        else:
            interest_rate = int(interest_rate_input)

        period_of_investment = int(input("How long are you planning to invest? (Years): "))
        interest = input("Do you want 'simple' or 'compound' interest: ").lower()

        if interest == "simple":
            future_amount = round(user_deposit_amount * (1 + interest_rate * period_of_investment / 100), 2)
            print("The amount you will have is : R%.2f" % future_amount)
        elif interest == "compound":
            future_amount = round(user_deposit_amount * math.pow(1 + interest_rate / 100, period_of_investment), 2)
            print("The total amount you will have is : R%.2f" % future_amount)
        else:
            print("Invalid interest type. Please choose 'simple' or 'compound'.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

elif user_choice in user_bond:
    try:
        present_value = float(input("What is the present value of the house?: "))
        interest_rate_input = input("What is the annual interest rate? (e.g., 7.7 or 7, not 7%): ")

        if "." in interest_rate_input:
            annual_interest_rate = float(interest_rate_input)
        else:
            annual_interest_rate = int(interest_rate_input)

        period_of_return = int(input("How long do you plan to repay the bond? (Months): "))

        monthly_interest_rate = annual_interest_rate / 12
        monthly_payment = round((monthly_interest_rate * present_value) / (1 - math.pow(1 + monthly_interest_rate, - period_of_return)), 2)


        print("You will need to pay {monthly_payment : R%.2f" % monthly_payment)

    except ValueError:
         print("Invalid input. Please enter valid numerical values.")

else:
    print("You have not entered a valid option. Please choose 'investment' or 'bond'.")

