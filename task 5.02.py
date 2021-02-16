import random

def create_matrix():
    a = 0
    x = int(4)
    y = int(4)
    matrix = []

    for i in range(x):
        matrix.append([])
        for j in range(y):
            matrix[i].append(random.randint(1,10))


        if i in matrix % 3 == 0:
            print(sum(i))

    return matrix

print(create_matrix())
#print(sum([y for y in range(x)  if y % 3 == 0]))