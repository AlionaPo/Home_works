# Algo-Riddles: The Coding Conundrum
# You have 100 cats.
# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
# In The first round, you stop at every cat, placing a hat on each one.
# In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.
# Optional: Make a function that can calculate hats with any amount of rounds and cats.
# Here you should write an algorithm, and after that, try to make pseudo code. Only after that start to work. The code is simple here, but you might struggle with the algorithm. Therefore don`t try to write a code from the first attempt. Don't forget to calculate the complexity of your algorithm.
# Homework should be uploaded at GitHub.com
# The result of this HW should be a link to your GitHub code
# To learn how to work in Git, read the first three chapters of this book

hats_on_cats = []
attempts = 100

for rounds in range(1, 100+1):
    for cat in range(1, 100+1):
        if cat % rounds ==0:
            hats_on_cats[cat] += 1
            if hats_on_cats[cat] = 1:
                hats_on_cats[cat] -= 1
            else:
                hats_on_cats[cat] += 1

for cat in range(1, 100+1):
    if hats_on_cats[cat] == 1:
            hats_on_cats.append(cat)

