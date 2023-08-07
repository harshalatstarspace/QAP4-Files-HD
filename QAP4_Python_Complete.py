# python for QAP One Stop Insurance Company

# import libraries

import datetime

# Constants
HST_RATE = .15
BASIC_PREMIUM = 869.00

# program
today = datetime.datetime.now()

# initializing variables to write to file

f = open("OSICDef.dat", "r")

policyNum = (f.readline())
policyNum = int(policyNum[0:4])
basicPremium = (f.readline())
basicPremium = float("{:.2f}".format(float(basicPremium[0:7])))
discountAdditonalCars = (f.readline())
discountAdditonalCars = float("{:.2f}".format(float(discountAdditonalCars[0:3])))
costLiabitlityCoverage = (f.readline())
costLiabitlityCoverage = float("{:.2f}".format(float(costLiabitlityCoverage[0:7])))
glassCoverage = (f.readline())
glassCoverage = float("{:.2f}".format(float(glassCoverage[0:7])))
loanerCar = (f.readline())
loanerCar = float("{:.2f}".format(float(loanerCar[0:7])))
hst = (f.readline())
hst = float("{:.2f}".format(float(hst[0:7])))
processingFeeMonthly = (f.readline())
processingFeeMonthly = float("{:.2f}".format(float(processingFeeMonthly[0:7])))

f.close()

while True:

    custName = input("Enter the customer's first name: ").title()
    custLastName = input("Enter the customer's last name: ").title()
    custAddress = input("Enter the customer's address: ")
    custCity = input(("Enter the customer's city: ")).title()

    while True:
        custProvAllowed = ["NL", "ON", "QC", "NS", "BC", "NB", "MB", "PEI", "AB","SK", "NWT", "NU", "YK"]
        custProv = input("Enter the customer's province: ").upper()
        if custProv not in custProvAllowed:
            print("Invalid entry, please enter a valid province.")
        elif custProv == "":
            print("Must enter a province.")
        else:
            break

    custPostal = input("Enter the customer's postal code: ")

    custPhone = input("Enter the customer's phone number: ")

    numCarsInsured = int(input("Enter number of cars insured: "))

    while True:
        allowedYN = ["Y", "N"]
        liabilityOption = input("Does customer want liabiltiy options (Y/N)? ").upper()
        if liabilityOption not in allowedYN:
            print("Invalid entry")
        elif liabilityOption == '':
            print("Can't be blank")
        else:
            break

    while True:
        glassCoverageOption = input("Does customer want glass coverage options (Y/N)? ").upper()
        if glassCoverageOption not in allowedYN:
            print("Invalid entry")
        elif glassCoverageOption == '':
            print("Can't be blank")
        else:
            break

    while True:
        loanerCarOption = input("Does customer want loaner car options (Y/N)? ").upper()
        if loanerCarOption not in allowedYN:
            print("Invalid entry")
        elif loanerCarOption == '':
            print("Can't be blank")
        else:
            break

    while True:
        fullOrMonthlyAllowed = ["Full", "Monthly"]
        fullOrMonthly = input("Does customer want to pay full or monthly?: ").title()
        if fullOrMonthly not in fullOrMonthlyAllowed:
            print("Invalid entry")
        elif fullOrMonthly == '':
            print("Can't be blank")
        else:
            break

    # calculations

    premiumAmtBasicTotal = BASIC_PREMIUM + ((numCarsInsured - 1) * (BASIC_PREMIUM * .25))

    if liabilityOption == "Y":
        premiumLiabilityAmt = costLiabitlityCoverage * numCarsInsured
    else:
        premiumLiabilityAmt = 0.00

    if glassCoverageOption == "Y":
        glassCoverageAmt = glassCoverage * numCarsInsured
    else:
        glassCoverageAmt = 0.00

    if loanerCarOption == "Y":
        loanerCarOptionAmt = loanerCar * numCarsInsured
    else:
        loanerCarOptionAmt = 0.00

    additionalAmtTotal = loanerCarOptionAmt + glassCoverageAmt + loanerCarOptionAmt

    totalPremiumSubtotal = premiumAmtBasicTotal + additionalAmtTotal

    totalPremium = totalPremiumSubtotal * (1 + HST_RATE)

    hSTAmt = totalPremium - totalPremiumSubtotal

    if fullOrMonthly == "MONTHLY":
        amtDue = ((totalPremium + processingFeeMonthly) / 8)
        amtDueDsp = str("${:.2f}".format(amtDue))
        fullOrMonthlyDispString = f"MONTHLY PAYMENTS OF {amtDueDsp}."
    else:
        amtDue = totalPremium
        amtDueDsp = str("${:.2f}".format(amtDue))
        fullOrMonthlyDispString = f"FULL PAYMENT OF {amtDueDsp}."

    invDate = today
    invDate = datetime.datetime.strftime(invDate, "%m-%d-%Y")
    paymentDate = today + datetime.timedelta(days=30)
    paymentDateDsp = datetime.datetime.strftime(paymentDate, "%m-%d-%Y")

    policyNumDsp = f"${policyNum:.2f}"
    numCarsInsuredDsp = str(numCarsInsured)
    basicPremiumDsp = f"${basicPremium:.2f}"
    premiumLiabilityAmtDsp = f"${premiumLiabilityAmt:.2f}"
    glassCoverageAmtDsp = f"${glassCoverageAmt:.2f}"
    loanerCarOptionAmtDsp = f"${loanerCarOptionAmt:.2f}"
    additionalAmtTotalDsp = f"${additionalAmtTotal:.2f}"
    totalPremiumSubtotalDsp = f"${totalPremiumSubtotal:.2f}"
    totalPremiumDsp = f"${totalPremium:.2f}"
    hSTAmtDsp = f"${hSTAmt:.2f}"


    # file updating
    f = open("Policies.dat", "a")

    f.write(f"{policyNum}, ".format(str(policyNum)))
    f.write(f"{invDate}, ".format(str(invDate)))
    f.write(f"{custName}, ")
    f.write(f"{custLastName}, ")
    f.write(f"{custAddress}, ")
    f.write(f"{custCity}, ")
    f.write(f"{custProv}, ")
    f.write(f"{custPostal}, ")
    f.write(f"{custPhone}, ")
    f.write(f"{numCarsInsured}, ".format(str(numCarsInsured)))
    f.write(f"{liabilityOption}, ".format(str(liabilityOption)))
    f.write(f"{glassCoverageOption}, ".format(str(glassCoverageOption)))
    f.write(f"{loanerCarOption}, ".format(str(loanerCar)))
    f.write(f"{fullOrMonthly}, ")
    f.write(f"{totalPremium}\n".format(str(totalPremium)))

    f.close()

    print()
    print("Policy information processed and saved.")
    print()

    print()
    print(f"=" * 40)
    print(f"   ONE STOP INSURANCE COMPANY RECEIPT   ")
    print(f"        AS OF {invDate:<9s}          ")
    print(f"          DUE {paymentDateDsp:<9s}      ")
    print(f"=" * 40)
    print(f"Customer: {custName + custLastName:<20s}  ")
    print(f"Customer Address:")
    print(f"{custAddress:<20s}, {custProv:<2s}, {custPostal:<5s}")
    print(f"Customer Phone: {custPhone:<13s}     ")
    print(f"=" * 40)
    print(f"Policy Number: {policyNumDsp:<5s} | Cars: {numCarsInsuredDsp:<1s}")
    print(f"")
    print(f"Basic premium:                   {basicPremiumDsp:>5s}")
    print(f"Liability option:                {premiumLiabilityAmtDsp:>6s}")
    print(f"Glass Coverage:                  {glassCoverageAmtDsp:>6s}")
    print(f"Loaner Car:                      {loanerCarOptionAmtDsp:>5s}")
    print(f"Total Additional Coverage Charge:{additionalAmtTotalDsp:>6s}")
    print(f"=" * 40)
    print(f"Totals:")
    print()
    print(f"Subtotal:                         {totalPremiumSubtotalDsp:>6s}")
    print(f"HST:                              {hSTAmtDsp:>6s}")
    print(f"Total:                            {totalPremiumDsp:6s}")
    print()
    print(f"Thank you for choosing One Stop Insurance")
    print()
    print(f"=" * 40)

    # the policy number gets updated here
    f = open("OSICDef.dat", "a")
    f.write(str(policyNum))
    f.close()

    policyNum += 1

    redoprogramQuestionAllowed = ["Y", "N"]
    redoprogramQuestion = input("Do you want to do enter another policy? ").upper()
    if redoprogramQuestion not in redoprogramQuestionAllowed:
        rint("Y or N please.")
    elif len(redoprogramQuestion) != 1:
        print("Y or N please.")
    elif redoprogramQuestion == "Y":
        pass
    else:
        break
