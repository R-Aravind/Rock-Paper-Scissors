import model

def player(prev_play, opponent_history=[], markov_model = model.MarkovChain(0.9)):
    opponent_history.append(prev_play)
        
    if prev_play == '':
        guess = markov_model.predict()
    
    else:
        guess = markov_model.predict(prev_play)
        
    return guess
