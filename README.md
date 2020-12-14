# RockPaperScissors
Importing Random &amp; playing against the computer 

The function will need input from the user and then the computer will choose between rock, paper or scissors.
The next step is setting up the rule:
1. if the user and computer has the same info it will be a tie. 
2. To see or setup winner there will be a function that has a user and computer parameter, that function will return a 'you won'
3. #r>s, s>p, p>r
4. Create a function 'is_win(player, opponent)' with two parameters it will return true if the player wins
  a. now we express the #r>s, s>p, p>r with an if statement...ex: if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'): return True 
  If True a as if statement "is_win(user, computer):" will return 'you won!' If the player does not win the play function will return 'you lost'
  To see result a print function is used print(play())
  
  1. random is imported
  2. a function called play() is created with two if statements in it and a return if the player lost
  3. But before the play() function returns anything the is_win function with two parameters is ran first with an if statement that returns true if the player wins. 
