def calculatePay():
    # This first line is provided for you
    try:
        hours = int(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))
        
        # pay calculation
        if hours > 40:
            overtime = hours - 40
            pay = (40 * rate) + (overtime * rate * 1.5)
        else:
            pay = hours * rate

        # print results of inputs
        print("Pay: " + str(pay))
        
    except ValueError:
        print("Error, please enter numeric input")
  
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
