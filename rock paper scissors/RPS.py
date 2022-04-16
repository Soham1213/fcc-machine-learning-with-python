# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def player(prev_play, opponent_history=[], player_history=[]):
    if prev_play != "":
      opponent_history.append(prev_play)
      # print(player_history[-1], prev_play)
      if (len(opponent_history) == 999):
        opponent_history.clear()
    
    # 1st turn
    # general strategy - leave to chance
    # most pick rock 1st, so choose paper
    if prev_play == "":
      guess = "P"
      player_history.append(guess)
      return guess
    # 2nd turn onwards
    # special strategy 1 - recognise pattern
    # countering quincy - repeats RPPSR
    if len(opponent_history) >= 5 and opponent_history[0]+opponent_history[1]+opponent_history[2]+ opponent_history[3]+opponent_history[4] == "RPPSR":
      # PSSRP
      if (len(opponent_history)+1)%5 == 1:
        guess = "P"
      elif (len(opponent_history)+1)%5 == 2:
        guess = "S"
      elif (len(opponent_history)+1)%5 == 3:
        guess = "S"
      elif (len(opponent_history)+1)%5 == 4:
        guess = "R"
      else :
        guess = "P"
      player_history.append(guess)
      return guess
      
    # special strategy 2 - 
    # countering abbey - starts with PP
    # looks at previous 2 moves
    if len(opponent_history) >= 2 and opponent_history[0]+opponent_history[1] == "PP":
      if player_history[-2] + player_history[-1] == "RR":
        guess = "S"
        player_history.append(guess)
        return guess
      elif player_history[-2] + player_history[-1] == "PP":
        guess = "R"
        player_history.append(guess)
        return guess
      elif player_history[-2] + player_history[-1] == "SS":
        guess = "P"
        player_history.append(guess)
        return guess
      elif player_history[-1] == "R":
        guess = "R"
        player_history.append(guess)
        return guess
      elif player_history[-1] == "P":
        guess = "P"
        player_history.append(guess)
        return guess
      elif player_history[-1] == "S":
        guess = "S"
        player_history.append(guess)
        return guess
      
    # general strategy 2
    # decisions are solely based on previous move
    # win by scissors
    if prev_play == "P" and player_history[-1] == "S":
      guess = prev_play
      player_history.append(guess)
      return guess
    # win by paper
    if prev_play == "R" and player_history[-1] == "P":
      guess = prev_play
      player_history.append(guess)
      return guess
    # win by rock
    if prev_play == "S" and player_history[-1] == "R":
      guess = prev_play
      player_history.append(guess)
      return guess
    # loss by paper
    if prev_play == "P" and player_history[-1] == "R":
      guess = "S"
      player_history.append(guess)
      return guess
    # loss by scissors
    if prev_play == "S" and player_history[-1] == "P":
      guess = "R"
      player_history.append(guess)
      return guess
    # loss by rock
    if prev_play == "R" and player_history[-1] == "S":
      guess = "P"
      player_history.append(guess)
      return guess
    # if draw
    # rock is likely to be chosen
    guess = 'P'
    player_history.append(guess)
    return guess
