print("THIS IS NEW QUIZ!! \n")

player = input("Dou you want play?: ")
exitText = "Thanks you for visit!"
endText = "thanks for playings!"
score = 0

if player.lower() != "yes":
    print(exitText.upper())
    exit()
    
else :
    print ("Let's have fun")

answer = input("what is square of 5? :")
if answer == "25":
    print("Good answer")
    score += 1

else :
    print("incorrect")

answer = input("what is this country name?: ")
if answer.lower() == "south africa":
    print("Good answer")
    score += 1
else :
    print("incorrect")

answer = input("what is surname of south african President?: ")
if answer.lower() == "cyril ramaphosa":
    print("Good answer")
    score += 1
else :
    print("incorrect")

answer = input("what is this programing language name?: ")
if answer.lower() == "python":
    print("Good answer")
    score += 1
else :
    print("incorrect")

answer = input("what is this city name?: ")
if answer.lower() == "johannesburg":
    print("Good answer")
    score += 1
else :
    print("incorrect")


print(endText.upper())

print("You made", score , "on this Quiz and got", (score/5) * 100 , "%." )
