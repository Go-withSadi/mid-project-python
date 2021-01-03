score = 0

#QUESTION 1
answer1 = input("What is the capital of Queensland? \na. Townsville \nb. Brisbane \nc. Noosa \nAnswer: ")
if answer1 == "b" or answer1 == "Brisbane":
    score += 1
    print("Correct!")
    print("Score: ",score)
else:
    print("Incorrect! The answer is Brisbane.")
    print("Score: ",score)
    print("\n")

#QUESTION 2
answer2 = input("In which state is Birdsville found? \na. NSW \nb. SA \nc. QLD \nAnswer: ")
if answer2 == "c" or answer1 == "QLD":
    score += 1
    print("Correct!")
    print("Score: ",score)
else:
    print("Incorrect! The answer is QLD.")
    print("Score: ",score)
    print("\n")

#QUESTION 3
answer3 = input("When is Gourmeet in Gundy held? \na. August \nb. September \nc. October \nAnswer: ")
if answer3 == "b" or answer3 == "September":
    score += 1
    print("Correct!")
    print("Score: ",score)
else:
    print("Incorrect! The answer is September.")
    print("Score: ",score)
    print("\n")

    #FINAL MESSAGE
if score <= 1:
    print("Your total sucore is:", score, "- You suck!")
elif score == 2:
    print("Your total score is", score, "- You went ok.")
else:
    print("Your total score is:", score, "- You are awesome!")
