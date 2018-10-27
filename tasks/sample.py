from tasks.task import Task


def repeatedString(s, n):
    na = s.count("a")
    full_repeats = n // len(s)
    leftover = n % len(s)
    last_na = s[0:leftover].count("a")
    return (full_repeats * na) + last_na


class Sample(Task):
    def input(self):
        return ["aba", 10]

    def expected_output(self):
        return 7

    def run(self):
        return repeatedString(*self.input())
