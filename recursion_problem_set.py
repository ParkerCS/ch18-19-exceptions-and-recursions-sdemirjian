'''
- Personal investment
Create a single recursive function (or more if you wish), which can answer the first three questions below.  For each question, make an appropriate call to the function. (5pts each)
'''

#1.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY, so MPR is APR/12).  Assuming you make no payments for 6 months, what is your new balance?  Solve recursively.
def interest(starting_amount, interest_rate, depth):
    new_amount = starting_amount + (starting_amount * interest_rate)

    if depth > 0:
        interest(new_amount, interest_rate, depth - 1)
    else:
        print(new_amount)

interest(10000, .20/12, 6)
print()

#2.  You have $5000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  You make the minimum payment of $100 per month for 36 months.  What is your new balance?  Solve recursively.
def interest(starting_amount, interest_rate, depth):
    new_amount = starting_amount + ((starting_amount + 100) * interest_rate)

    if depth > 0:
        interest(new_amount, interest_rate, depth - 1)
    else:
        print(new_amount)
interest(5000, .20/12, 36)
print()

#3.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  If you make the minimum payment of $100 per month, how many months will it take to pay it off?  Solve recursively.
def interest(starting_amount, interest_rate, months):
    new_amount = starting_amount + ((starting_amount + 100) * interest_rate)

    try:
        if new_amount != 0:
            interest(new_amount, interest_rate, months + 1)
    except:
        print("You've exceeded the amount. You spend too much!")
        print("At the end of ", months, "months, you had", new_amount, "monies")
interest(10000, .20/12, 0)
print()

#4  Pyramid of Cubes - (10pts) If you stack boxes in a pyramid, the top row would have 1 box, the second row would have two, the third row would have 3 and so on.  Make a recursive function which calculates the TOTAL NUMBER OF BOXES for a pyramid of boxes n high.  For instance, a pyramid that is 3 high would have a total of 6 boxes.  A pyramid 4 high would have 10.
def pyramid(starting_boxes, n, x):
    total_boxes = starting_boxes + x

    if n > 1:
        pyramid(total_boxes, n - 1, x + 1)
    else:
        print(total_boxes)
pyramid(0, int(input("How tall is the pyramid?")), 1)