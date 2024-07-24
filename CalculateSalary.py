def overtimepaid(n, s, t):
    if t > 40:
        ot = t - 40
    else:
        ot = 0
    
    otp = ((t-ot)*100)+(ot*(100*1.5))
    tp = s+otp
    
    print("-----------------\nName: %s" % n)
    print("Salary: %.2f" % s)
    print("Overtime Hours: %d" % t)
    print("Overtime Paid: %.2f" % otp)
    print("Total Paid: %.2f" % tp)
    
    
n = input("Input Name: ")
s = float(input("Input salary: "))
t = int (input("Input OT hours: "))

overtimepaid(n, s, t)