k=0
a1=3
a2=1
a3=3
a4=4
n=input("Kā tevi sauc? ")
print("Cau",n)
a=int(input("Tavs milakais filmas zanrs?? 1 - komedija 2 - detektivi 3 - fantastika" ))
if (a==a1):
    k=k+1
a=int(input("Tavs milakais muzikas zanrs? 1- klasika 2 reps 3 pops"))
if (a==a2):
    k=k+1
a=int(input("Tava milaka krasa? 1 - zila 2 - zala 3 - sarkana "))
if (a==a3):
    k=k+1
a=int(input("Tavs milakais gadalaiks! 1- vasara 2 - ziema 3 - pavasaris 4 - rudens "))
if (a==a4):
    k=k+1
if (k>=2):
    print(n," Mes esam lidzigi ")
if (k<2):
    print(n+" Mes esam pavisam dazadi ")