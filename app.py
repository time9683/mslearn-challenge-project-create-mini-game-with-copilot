from random import choice

Options = ["rock","paper","scissors"]


def main():
    score = 0 
    rounds = 0

    while True:
        option = input("Which attack will you use rock, paper or scissors?: ").lower()
        if(not (option in Options)):
            print("your choice does not exist")
            continue
        option_CPU = choice(Options)

        result = win(option,option_CPU)
        if result == "win":
            score += 1
        rounds += 1
        print(f'you {result}, your score is {score} in the round {rounds}')
        if (input("Do you continue to the next round? (yes|no): ").lower() == "no"):
            break

    print(f'your total score is {score} with {rounds} rounds ')
    print("END GAME")
       





def win(op1,op2):

    if(op1 == op2):
        return "tie"

    if (op1 == "rock" and  op2 == "scissors")  or (op1 == "scissors" and op2 == "paper") or (op1 == "paper" and op2 == "rock" ):
        return "win"
    else:
        return "lose"
 






if __name__ == "__main__":
    main()