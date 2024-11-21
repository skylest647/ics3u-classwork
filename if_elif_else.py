#elif is essentially if if is false then provides its own if statment only running if the first if is false
#else essentially means if everything else is false then..
team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
#this changes nothing except maybe being inefficent as it has to run 1 more line of code that otherwise would've been unecessary
#no difference because of how the question is formated if team a wins > team b wins then it can't be team b wins > team a wins
if team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    #This is printed because team a have more points than b and thus wins one round right before the number of wins is calculated
    print("Both Teams A and B have the same number of wins.")