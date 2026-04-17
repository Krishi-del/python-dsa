weight = float(input("Weight: "))
unit = input("L(bs) or K(g): ")
L = weight*0.45
K = weight/0.45
if unit.upper() == "L":
    print(f"Your weight is {L}")
elif unit.upper() == "K":
    print(f"Your weight is {K}")    