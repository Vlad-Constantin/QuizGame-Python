# quiz game
import random

def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 1
    for key in questions:
        print(" -----------------------")
        print(key)
        for i in options[questions_num-1]:
            print(i)

        guess = input("A / B/ C------> ").upper()
        guesses.append(guess)
        correct_guesses += check_answers(questions.get(key),guess)
        questions_num +=1
    display_score(correct_guesses,guesses)
    use_points(correct_guesses)
# -----------------------
def check_answers(answer, guess):

    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0

# -----------------------
def display_score(correct_guesses,guesses):
    print(" -----------------------")
    print("RESULTS!!!")
    print(" -----------------------")
    print("Correct Answers", end=" ")
    for i in questions :
        print(questions.get(i),end= " ")
    print()
    print("Guesses", end=" ")
    for i in guesses:
        print((i), end=" ")
    print()
    score = str(correct_guesses/len(options)*100)
    score_points = str(correct_guesses)
    print(score,"%")
    print("Nr points = ",score_points)
# -----------------------
def use_points( correct_guesses):
    points = correct_guesses
    enchant = 0
    for i in range(points):
        print("Use point: nr. ", i+1)
        user_input = input("Press 1 to use the point.(60%) :")
        if user_input == "1":
            points -= 1
            if random.random() < 0.6:
                enchant += 1
                print("Enchant  +1")
            else:
                print("No LUCK!")
        else:
            print("You did not press the 1 key")
        print(points," remaining points. " )
        print("You have ",enchant," remaining points for enchanting.")
    print("You have run out of points. You have a total of ",enchant," enchantments!")



#------------------------
def play_again():
    response = input("play again? (yes/no): ").upper()
    if response == "YES":
        return True
    else:
        return False




questions = {
    "What is the capital of France? ":"C",
    "What is the capital of Italy? ":"B",
    "What is the capital of Spain? ":"B",
    "What is the capital of Moldova? ":"B"
            }
options = [["A. Bucuresti","B. Athena","C. Paris"],
            ["A. Madrid","B. Rome","C. Berna"],
            ["A. Ankara","B. Madrid","C. Kiev"],
            ["A. Praga","B. Chisinau","C. Viena"]
            ]

new_game()
while play_again():
    new_game()
