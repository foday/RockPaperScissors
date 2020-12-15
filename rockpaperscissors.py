import random 

def play(): 
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    #Rules 
    if user == computer: 
        return 'tie'

    #r > s, s > p, p > r

