# it works like a factory pattern
class CallMe():
    def __init__(self):
        pass

cm = CallMe
print(callable(cm))