class HighScores:
    def __init__(self, scores):
        self.scores = scores
    
    def latest(self):
        return self.scores[(len(self.scores) - 1)]
    
    def personal_best(self):
        return max(self.scores)
    
    def personal_top_three(self):
        reverse_order = sorted(self.scores, reverse=True)
        return reverse_order[:3]
