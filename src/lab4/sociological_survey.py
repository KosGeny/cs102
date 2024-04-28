class AgeGroup:
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


class AgeGroupDivider:
    def __init__(self, age_groups):
        self.age_groups = age_groups
        self.grouped_respondents = {group: [] for group in self.age_groups}

    def add_respondent(self, respondent):
        for group in self.age_groups:
            if group.contains(respondent.age):
                self.grouped_respondents[group].append(respondent)
                break

    def display_groups(self):
        for group in reversed(self.age_groups):
            if self.grouped_respondents[group]:
                print(f"{group.str()}: ", end="")
                print(
                    ", ".join(
                        respondent.str()
                        for respondent in sorted(self.grouped_respondents[group], key=lambda x: (-x.age, x.name))
                    )
                )


def parse_age_groups(args):
    age_groups = [-1] + [int(arg) for arg in args] + [123]
    return [AgeGroup(age_groups[i] + 1, age_groups[i + 1]) for i in range(len(age_groups) - 1)]