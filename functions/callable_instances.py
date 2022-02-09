# state preserver pattern can be achieved by __call__ dunder
class CallMe():
    def __call__(self, name):
        print(name)

instance_callme = CallMe()
# print(callable(instance_callme))
# instance_callme("Amit")