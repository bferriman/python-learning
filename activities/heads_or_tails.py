# create a random list filled with 'h' and 't' chars
# output the number of heads and tails
import random

results = []

flip = {
    "heads": (lambda: results.append("h")),
    "tails": (lambda: results.append("t"))
}
# flip 50 times and save results
for i in range(50):
    flip_key = random.choice(["heads", "tails"])
    flip[flip_key]()

print("Heads :", results.count("h"))
print("Tails :", results.count("t"))
