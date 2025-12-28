class School:
    def __init__(self):
        self.students = {}
        self.additions = []

    def add_student(self, name, grade):
        roster = self.roster()
        if name not in roster:
            if grade not in self.students.keys():
                self.students[grade] = [name]
                self.additions.append(True)      
                # sort by grade
                self.students = dict(sorted(self.students.items()))
            else:
                self.students[grade].append(name)
                self.additions.append(True)
                # sort by names within the grade
                self.students[grade] = sorted(self.students[grade])
        else:
            self.additions.append(False)

    def roster(self):
        result = []
        for students in self.students.values():
            result.extend(students)
        return result

    def grade(self, grade_number):
        if grade_number not in self.students.keys():
            return []
        else:
            return self.students[grade_number]
        
    def added(self):
        return self.additions
