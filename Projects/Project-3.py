# Developer = Talha Tahir
print("Welcome to Rock-Paper-Scissors!")

while True:
    user = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    if user == 'quit':
        break
    if user not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue

    import random
    computer = random.choice(['rock', 'paper', 'scissors'])
    print("Computer chose: " + computer)

    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")
