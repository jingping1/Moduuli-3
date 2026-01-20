sukupuoli=input("Anna sukupuoli")
hemo = float(input("Anna hemoglobiiniarvo"))
if sukupuoli=="nainen":
    if hemo<= 117:
        print("alhainen")
    elif hemo <= 175:
        print("normaali")
    else:
        print("korkea")
elif sukupuoli=="mies":
    if hemo <= 134:
        print("alhainen")
    elif hemo <= 195:
        print("normaali")
    else:
        print("korkea")







