import importlib


class Runner:

    def __init__(self, package, class_name):
        self.package = package
        self.class_name = class_name

    def run(self):
        action = getattr(importlib.import_module(self.package), self.class_name)()
        result = action.run()
        print(result)
        print("Correct" if action.expected_output() == result else "Wrong")
