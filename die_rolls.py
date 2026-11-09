#A109, 08/11/26
#24/2496, CS-A
#Computer Science
#Define the SimpleRandom class with a __init__ method and a next method
class SimpleRandom:
    def __init__(self, seed):
        #Set up the generator with a starting seed
        self.state = seed
        self.a = 1103515245
        self.c = 12345
        self.m = 2**31

    def next(self):
        """Generate the next pseudo-random number between 0 and 1."""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m

dieRoll_object = SimpleRandom(seed=123)

#Implementing the simulate_die_rolls funtion using SimpleRandom
def simulate_die_rolls(n):
    total = 0
    for _ in range(n):
        # Convert random [0,1) to die roll [1,6]
        roll = int(dieRoll_object.next() * 6) + 1
        total += roll
    return total / n

# Roll 10, 100, 1000, and 10000 times
for n in [10, 100, 1000, 10000]:
    average = simulate_die_rolls(n)
    print(f"Average of {n:5d} rolls: {average:.4f}")

