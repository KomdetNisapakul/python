def bmi(kg, cm):
    bmi = kg/(cm/100)**2
    return bmi

def check(bmi):
    

kg = int(input("Weight: "))
cm = int(input("Height: "))
print("bmi %.2f" % bmi(kg,cm))