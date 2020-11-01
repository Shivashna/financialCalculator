import math

# The purpose of this program is to calculate the amount that the user will earn on their investment or to calculate the amount that the user will have to pay on a home loan.

menu = (input("Choose either 'investment' or 'bond' from the menu below to proceed : \n\ninvestment\t-to calculate the amount of interest you'll earn on an investment \nbond\t\t-to calculate the amount you'll have to pay on a home loan\n\nEnter 'investment' or 'bond' to continue : ")).lower()

P = 0
interest_str = ''
interest = 0
num_years = 0
interest_type = ''
total_amount = 0
present_value = 0
i = 0
num_months = 0
monthly_amount = 0

# If the user chooses 'investment' the program will ask for the relevant information to calculate the interest on the investment

if (menu == "investment"):

    P = float(input("Enter the amount that you would like to invest : R"))
    interest_str = input("Enter the interest rate you would like to invest at : ")
    interest = (float(interest_str.strip("%")))/100
    num_years = float(input("Enter the number of years you would like to invest for : "))
    interest_type = (input("\nState whether you like to invest using simple or compound interest : \n\nSimple Interest\t\t- is continually calculated on the initial amount that you invest \nCompound Interest\t- is calculated on the accumalated amount which includes the accumalated interest \n\nSimply enter 'simple' or 'compound' to proceed : ")).lower()

# The user must choose whether they want 'simple interest' or 'compound interest' on their investment

    if (interest_type == "simple"):
        total_amount = P * (1 + interest * num_years)
        total_amount = round(total_amount,2)
        print("\nThe total amount you will get at the end of {} years is R{}".format(num_years,total_amount))

    elif (interest_type == "compound"):
        total_amount = P * math.pow((1 + interest),num_years)
        total_amount = round(total_amount,2)
        print("\nThe total amount you will get at the end of {} years is R{}".format(num_years,total_amount))

# If the user chooses 'bond' the program will ask the user to enter the relevent information in order to work out their monthly payment for the bond 

elif (menu == "bond") :

    present_value = float(input("\nEnter the present value of the house : R"))
    interest_str = input("Enter the interest rate : ")
    interest = (float(interest_str.strip("%")))/100
    i = interest/12
    num_months = float(input("Enter the number of months over which you plan to repay the bond : "))
    monthly_amount = (i * present_value)/ (1 - (math.pow((1 + i),(-num_months))))
    monthly_amount = round(monthly_amount,2)
    print("\nYour monthly payment is an amount of R{} for {} months.".format(monthly_amount,num_months))
    
