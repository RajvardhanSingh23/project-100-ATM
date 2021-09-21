class atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number


    def cashWithdrawal(self):
            print("Money has been successfully withdrawaled")
    def balanceEnquiry(self):
            print("You have sufficient balance")
    def cashDeposit(self):
            print("Your cash is safely deposited")
    def transferMoney(self):
            print('Money Has been successfully transfered')

SBI = atm(28382929929, 2020)
# Uncomment lines to Complete the class  

#print(SBI.cashWithdrawal())
#print(SBI.balanceEnquiry())
#print(SBI.cashDeposit())
#print(SBI.transferMoney())
