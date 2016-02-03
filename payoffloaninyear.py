def calculateCompound(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12
    minMonthly = balance * monthlyPaymentRate
    remainingBalance = balance
    monthlyUnpaid = balance
    totalPaid = 0


    for m in range(1,13):
        print "Month: %s" %m
        minMonthly = balance * monthlyPaymentRate

        print "Minimum monthly payment: %s" % round(minMonthly,2)
        monthlyUnpaid = balance - minMonthly
        #print "MUnpaid = %s" %monthlyUnpaid

        remainingBalance = monthlyUnpaid * (1+monthlyInterestRate)
        print "Remaining balance: %s" %round(remainingBalance, 2)

        balance = round(remainingBalance, 2)
        totalPaid = totalPaid + minMonthly

    print "Total paid: %s" %round(totalPaid,2)
    print "Remaining balance: %s" %balance





balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate  = 0.04

calculateCompound(balance, annualInterestRate, monthlyPaymentRate)
