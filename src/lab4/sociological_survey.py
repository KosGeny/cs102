class Age_Group:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, age):
        return self.start < age <= self.end

    def str(self):
        if self.start == 101:
            return "101+"

        return f"{self.start}-{self.end}"


class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def str(self):
        return f"{self.name} ({self.age})"