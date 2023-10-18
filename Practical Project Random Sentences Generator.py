import random
from colorama import Fore
names = ["Emily", "Daniel", "Olivia", "Liam", "Sophia", "Benjamin", "Ava", "Noah", "Isabella", "William"]
places = ["Sofia", "Paris", "London", "Rome", "Berlin", "Barcelona", "Amsterdam", "Prague", "Vienna", "Athens"]
adverbs = ["quickly", "quietly", "loudly", "happily", "carefully", "suddenly", "always", "often", "well", "badly","sincerely", "rarely", "anxiously", "briefly", "silently"]
verbs = ["runs", "jumps",  "sings", "dances", "eats", "sleeps", "writes", "reads", "talks", "swims", "laughs", "cooks", "plays", "studies", "drives"]
nouns = ["cat", "bicycle", "ocean", "books", "tree", "rainbow", "coffee", "guitar", "keys", "mountain", "phone", "hats", "dog", "backpacks", "moon"]
details = ["near the riverbank", "at the top of a mountain", "inside a cozy cafe", "under a starry night sky", "in a bustling city square", "on a remote island", "amidst a dense forest", "at a seaside resort", "inside an ancient castle", "within a hidden cave"]

def get_random_word(words):
    return random.choice(words)

print(Fore.YELLOW + "Hello, this is your first random sentence: ")

while True:
    print(Fore.BLUE + "")
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_adverb = get_random_word(adverbs)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_detail = get_random_word(details)
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")
    print(Fore.YELLOW + "")
    decision = input("Type [y] to generate a new one or [n] to quit: ")
    if decision == "y":
        continue
    elif decision == "n":
        break
print("Thank you for coming!")






