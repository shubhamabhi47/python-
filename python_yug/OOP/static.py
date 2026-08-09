class Bank:
    bank_name = "BOI"
    rate_of_interest = 12.25

    @staticmethod
    def simple_interest(p , t):
        si = (p*Bank.rate_of_interest*t)/100
        print(si)

p = int(input("Enter principle ammount: "))
t = int(input("Enter number of years: "))
Bank.simple_interest(p , t)