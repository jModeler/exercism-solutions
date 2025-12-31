SCORES = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128
}

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return (item in self.lst)

    @property
    def lst(self):
        result = []
        if self.score in SCORES.values():
            ind = list(SCORES.values()).index(self.score)
            result.append(list(SCORES.keys())[ind])
        elif self.score == sum(SCORES.values()):
            result.extend(list(SCORES.keys()))
        else:
            result.extend(self.get_ind_allergies())
        return result 

    def get_score_comp(self):
        components = []
        if self.score > 255:
            adjusted_score = self.score % 256
        else:
            adjusted_score = self.score
        while(adjusted_score > 0):
            max_score = max(ii for ii in SCORES.values() if ii <= adjusted_score)
            components.append(max_score)
            adjusted_score -= max_score
        return components
        
    def get_ind_allergies(self):
        components = self.get_score_comp()
        result = []
        for score in components:
            ind = list(SCORES.values()).index(score)
            result.append(list(SCORES.keys())[ind])
        return result