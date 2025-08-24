import random


def rock_paper_scissors():

    num = random.randint(1, 3)  # 1 aur 3 dono include honge
    computer_choice = num

    n = (input("Enter your choice (1=Stone, 2=Paper, 3=Scissors): "))



    reverse_dict = {1: "🪨", 2: "📄", 3: "✂️"}

    input_map = {
        "1": 1, "stone": 1, "🪨": 1,
        "2": 2, "paper": 2, "📄": 2,
        "3": 3, "scissors": 3, "✂️": 3
    }

    if n in input_map:
        n = input_map[n]

    if n in input_map.values():
        if n == computer_choice:
            print("It's a tie!")
        elif n == 1 and computer_choice == 3:
            print("you choose stone and computer choose scissors")
            print("You win🏆!")
        elif n == 2 and computer_choice == 1:
            print("you choose paper and computer choose stone")
            print("You win🏆!")
        elif n == 3 and computer_choice == 2:
            print("you choose scissors and computer choose paper")
            print("You win🏆!")
        elif n == 1 and computer_choice == 2:
            print("you choose stone and computer choose paper")
            print("You lose🥲!")
        elif n == 2 and computer_choice == 3:
            print("you choose paper and computer choose scissors")
            print("You lose🥲!")
        elif n == 3 and computer_choice == 1:
            print("you choose scissors and computer choose stone")
            print("You lose🥲!")


rock_paper_scissors()

a1 = input("wanna play again? (yes/no)")

if a1.lower() == "yes":
    rock_paper_scissors()
else:
    print("Thanks for playing☺️!")
