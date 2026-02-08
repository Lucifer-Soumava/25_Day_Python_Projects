# Title
print("Bob's Space Adventure!")

# Inputs (Same as yours)
adjective1: str = input('Enter an adjective: ')
animal: str = input('Enter an animal: ')
adjective2: str = input('Enter another adjective: ')
noun1: str = input('Enter a noun: ')
verb: str = input('Enter a verb: ')
noun2: str = input('Enter one more noun: ')

# Story (New Custom Story)
story: str = f'''
One night, Bob was reading a book when a {adjective1} {animal} suddenly appeared in his room.
It was holding a {adjective2} {noun1} and looking very mysterious.

Before Bob could react, the {animal} asked him to {verb} using his {noun2}.
Without thinking twice, Bob agreed and was transported to another world.

It turned out to be the most exciting adventure of his life.
'''

# Output
print('Result:')
print(story)