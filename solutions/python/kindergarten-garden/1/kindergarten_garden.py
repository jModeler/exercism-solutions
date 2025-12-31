PLANTS = {
    'G': "Grass",
    'C': "Clover",
    'R': "Radishes",
    'V': "Violets"
}

STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split("\n")
        if students:
            self.students = sorted(students)
        else:
            self.students = STUDENTS
    
    def plants(self, student):
        ind = self.students.index(student)
        plant_indices = [2*ind, 2*ind+1]
        result = []
        for row_plants in self.diagram:
            for ii in plant_indices:
                plant_name = PLANTS[row_plants[ii]]
                result.append(plant_name)
        return result