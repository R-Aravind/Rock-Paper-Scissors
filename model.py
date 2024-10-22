import random

class MarkovChain():
    
    def __init__(self, decay=1.0):
        self.matrix = self.create_matrix()
        self.decay = decay
        self.prev_pred = ''
        
    def create_matrix(self):
        keys = ['PP', 'PR', 'PS', 'RP', 'RR', 'RS', 'SP', 'SR', 'SS']
        
        matrix = {}
        
        for key in keys:
            matrix[key] = {'R': {'prob' : 1 / 3,
                                 'n_occ' : 0
                                },
                           'P': {'prob' : 1 / 3,
                                 'n_occ' : 0
                                },
                           'S': {'prob' : 1 / 3,
                                 'n_occ' : 0
                                }
                          }
            
        return matrix
    
    def update_matrix(self, key, prev_play):

        for i in self.matrix[key]:
            self.matrix[key][i]['n_occ'] = self.decay * self.matrix[key][i]['n_occ']
            
        self.matrix[key][prev_play]['n_occ'] = self.matrix[key][prev_play]['n_occ'] + 1

        total = 0
        for i in self.matrix[key]:
                total += self.matrix[key][i]['n_occ']
                
        for i in self.matrix[key]:
            self.matrix[key][i]['prob'] = self.matrix[key][i]['n_occ'] / total
        
    def predict(self, prev_play=''):
        
        defeats = { "R" : "P",
                    "P" : "S",
                    "S" : "R",}
        
        if self.prev_pred == '':
            self.prev_pred = random.choice(['R', 'P', 'S'])
            return self.prev_pred
     
        key = self.prev_pred + prev_play
     
        self.update_matrix(key,prev_play)
        
        probs = self.matrix[key]
        
        if max(probs.values()) == min(probs.values()):
            pred = random.choice(['R', 'P', 'S'])       
        else:
            pred = defeats[max([(i[1], i[0]) for i in probs.items()])[1]]
            
        self.prev_pred = pred
        return pred