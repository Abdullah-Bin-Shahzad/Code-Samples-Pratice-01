import random

def play():
    user = input("What's is your choice? 'r' for rock, 's' for scissors and 'p' for paper: ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'
    elif is_win(user,computer):
        print(f'You choose {user} and computer choose {computer}')
        return 'You won'
    else: 
        print(f'You choose {user} and computer choose {computer}')
        return 'You loss'

    

def is_win(player, opponent):
    #return true if player wins
    #rules r>s, s>p, p>r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
while True:  
    print(play())