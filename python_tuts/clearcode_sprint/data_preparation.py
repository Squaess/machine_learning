import random
n = 10000


with open('data.csv', "w") as f:
    f.write('task_id,story_points,KSP\n')
    for i in range(n):
        f.write(str(i))
        f.write(',')
        f.write(str(random.randrange(1, 7, 1)))
        f.write(',')
        f.write(str(random.randrange(1, 20, 1)))
        f.write("\n")
