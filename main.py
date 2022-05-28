import random

cards = list(range(1,14))
your_cards = [random.choice(cards), random.choice(cards)]
computer_first_hand = random.choice(cards)

print(f"Your cards: {your_cards}")
print(f"Computer's first hand: {computer_first_hand}")

next_move = str(input("Type 'y' to get another card, type 'n' to pass:\n"))
your_final_cards = your_cards + [(random.choice(cards))] #append didn't work here

if next_move == 'y':
    print(f"Your final hand: {your_final_cards}")
else:
    print(f"Your final hand: {your_cards}")
    
computer_final_hand = [computer_first_hand,(random.choice(cards))] #line to figure out later
print(f"Computer's final hand: {computer_final_hand}")
    
if sum(computer_final_hand) == sum(your_final_cards)  or sum(computer_final_hand) == sum(your_cards):
    print("It's a draw")
elif sum(computer_final_hand) >= 21:
    print("Computer bust! You Win!")
elif sum(your_final_cards) >=21:
    print("Bust! You lose.")
elif sum(your_cards) >=21:
    print("Bust! You lose.")
elif sum(your_final_cards)  > sum(computer_final_hand):
    print("You Win!")
elif sum(your_cards) > sum(computer_final_hand):
    print("You Win!")
else:
    print("You lose.")
