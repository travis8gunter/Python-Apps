import random
#import operations


def print_introduction():
    print('''* 1) Introduction ********************************
Welcome to the Goblins Magical Loan System!
Please answer the following questions truthfully,
and we will process your loan request.
Imposters will be fed to the dragons.''')
    return
  


def input_name():
    print('''* 2) Name ****************************************
Please enter your full, legal name.
Magical verification will verify your identity.''')
    name = input("Write your name and press enter: ")
    print('Welcome, ' + name + '!')
    return str(name)


rate = random.randint(0,10)
def print_rating(rate):
    print("* 3) Rating **************************************")
    print("Your user rating has been calculated.")
    print("Your rating is: "+ str(rate) +"/10 points.")
    return int(rate)

    
    
    
def input_loan_amount():
    print('''* 4) Loan ****************************************
Loans are made based on your customer rating.
However, you can request a loan of any size.
How many galleons do you want?''')
    loan = input("Write your loan amount:")
    #loan = int(loan)
    return int(loan)
  
    
def test_loan(rate,loan):
    check = rate**2 * 100 >= loan
    return check

    
def print_loan_availability(rate, loan):
    print('''* 5) Available? **********************************
Your loan request has been evaluated.''')
    available = test_loan(rate,loan)
    print("Loan available:",available)
    
def print_conclusion():
    print('''* 6) Conclusion **********************************
Thanks for using Goblins Magical Loan System!
Best of luck with your new small business.
We hope you'll use Goblins for all your future
banking needs. Remember: Fortius Quo Fidelius!
**************************************************''')


def main():
    print_introduction()
    name = input_name()
    print_rating(rate)
    loan = input_loan_amount()
    print_loan_availability(rate, loan)
    print_conclusion()
    return
if __name__ == '__main__':
    main()