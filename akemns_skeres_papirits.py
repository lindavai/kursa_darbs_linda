import random 
user_wins = 0
computer_wins = 0
options = ["akmens", "skeres", "papirits"]


while True:
    user_input = input ("Type akmens/skeres/papirits or beigt to quit:  ").lower()
    if user_input == "beigt":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # akmens = 0 , skeres = 1 , papirits = 2
    computer_pick = options [random_number]
    print("Dators izvelejaas " , computer_pick + ".") 


    if user_input == "akmens" and computer_pick == "skeres":
        print("Tu uzvareeji!")
        user_wins +=1


    elif user_input == "papirits" and computer_pick == "akmens":
        print("Tu uzvareeji!")
        user_wins +=1


    elif user_input == "skeres" and computer_pick == "papirits":
        print("Tu uzvareeji!")
        user_wins +=1

    else: 
        print ("Tu zaudeji!")
        computer_wins +=1 


print ("Tu uzvaeji" , user_wins , "reizes. ")
print ("Dators uzvareja" , computer_wins , "reizes. ")
print ("Ataaaaaa!")
