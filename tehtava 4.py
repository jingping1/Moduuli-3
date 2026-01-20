vuosi = int(input("anna vuosi"))
if vuosi%400==0:
    print("karkausvuosi")
elif vuosi%100==0:
    print("ei ole karkausvuosi")
elif vuosi%4==0:
    print("karkausvuosi")
else:
    print("ei ole karkausvuosi")


