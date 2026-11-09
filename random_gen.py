#A109, 08/11/26
#24/2496, CS-A
#Computer Science
#Define the SimpleRandom class with a __init__ method and a next method"""
class SimpleRandom:
    def __init__(self, seed):
        #Set up the generator with a starting seed.
        self.state = seed
        self.a = 1103515245
        self.c = 12345
        self.m = 2**31

    def next(self):
        #Generate the next pseudo-random number between 0 and 1.
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m

simpleRandom_object = SimpleRandom(seed=77)
for i in range(10):
    print(simpleRandom_object.next())

print()

#Retesting to show that the formula works and is deterministic
objectretest = SimpleRandom(seed=77)
print(objectretest.next())
print(objectretest.next())
print(objectretest.next())
print(objectretest.next())
print(objectretest.next())