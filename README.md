#FINANCIAL CALCULATORS

##What is the purpose of this project and who can use it?

This is a simple program that allows the user to access two different financial calculators, namely, an investment calculator and a home loan repayment calculator. This program is appropriate for small financial companies and can be used by clients to calculate the amount they could earn from an investment or how much they would have to pay on a home loan monthly.

##Describing the program

When the program runs, a menu will be displayed to the user. The user can then choose whether they would like to calculate an investment amount or home loan repayment amount.

If the user chooses to calculate an investment amount, the program will prompt the user to enter the amount they would like to invest, the interest rate, the number of years they plan on investing for and whether they would like *simple* or *compound* interest. Based on how the user answers these questions, the program will then calculate and display the amount that they should get after the given period. The following equations are used to calculate the total amount after the given period :

*Simple interest : **A = P(1 + r * t)**
*Compound interest : **A = P(1 + r) ^ t**

A - Total amount once interest has been applied
P - Amount that the user deposits
r - Interest rate divided by 100(example : 7% = 7/100 = 0.07)
t - The number of years the money is being invested for

If the user chooses to calculate a home loan repayment amount, the program will prompt the user to enter the current value of the house, the interest rate and the number of months they plan to repay the bond in. Based on the answers given in these questions, the program will then calculate and display the monthly repayment amount for the bond. The following equation is used to calculate the monthly bond repayment :

*Monthly home loan repayment : **x = (i.P)/(1 - (1+i)^(-n))**

x - Monthly repayment
P - Present value of the house
i - Monthly interest (calculated by dividing the annual interest by 12)
n - The number of moonths over which the bond will be repaid

##How to get this code to work

To access this program and get it working, simply download and install Python, then run the program code (press F5).
