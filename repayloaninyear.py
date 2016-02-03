def PayOffInYear(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12
    monthlyPayment = round((balance * (1+monthlyInterestRate))/11, -1)

    print " Lowest Payment:", monthlyPayment

balance = 3329
annualInterestRate = 0.2

PayOffInYear(balance, annualInterestRate)
