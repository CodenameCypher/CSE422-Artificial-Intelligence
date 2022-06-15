print("\n#####CSE-422-Lab1-Tamanna-Afroz-18301153#####\n")

# Task 1


def covid_tracer(file_name):
    # file input
    with open(file_name, 'r') as file:
        matrix = [[ele for ele in line.split(' ')] for line in file]

    # removing line break(\n)
    for index in range(len(matrix)):
        matrix[index][-1] = matrix[index][-1].replace('\n', '')

    # creating a touple list of the positions of infect
    infect = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if 'Y' in matrix[row][col]:
                infect.append((row, col))

    counter = []  # counter to keep track of visited touples or position within matrix
    # appliying DFS to all areas in matrix
    for pair in infect:
        stack = [pair]
        visited = [pair]
        infect.remove(pair)
        # DFS Algo and checking for neighbour infect's
        while len(stack):
            pos = stack.pop(-1)

            if (pos[0], pos[1] + 1) in infect and (pos[0], pos[1] + 1) not in visited:  # right
                stack.append((pos[0], pos[1] + 1))
                visited.append((pos[0], pos[1] + 1))
                infect.remove((pos[0], pos[1] + 1))
            if (pos[0], pos[1] - 1) in infect and (pos[0], pos[1] - 1) not in visited:  # left
                stack.append((pos[0], pos[1] - 1))
                visited.append((pos[0], pos[1] - 1))
                infect.remove((pos[0] - 1, pos[1] - 1))
            if (pos[0] - 1, pos[1]) in infect and (pos[0] - 1, pos[1]) not in visited:  # up
                stack.append((pos[0] - 1, pos[1]))
                visited.append((pos[0] - 1, pos[1]))
                infect.remove((pos[0] - 1, pos[1]))
            if (pos[0] + 1, pos[1]) in infect and (pos[0] + 1, pos[1]) not in visited:  # down
                stack.append((pos[0] + 1, pos[1]))
                visited.append((pos[0] + 1, pos[1]))
                infect.remove((pos[0] + 1, pos[1]))
            if (pos[0] - 1, pos[1] + 1) in infect and (pos[0] - 1, pos[1] + 1) not in visited:  # upper right
                stack.append((pos[0] - 1, pos[1] + 1))
                visited.append((pos[0] - 1, pos[1] + 1))
                infect.remove((pos[0] - 1, pos[1] + 1))
            if (pos[0] + 1, pos[1] + 1) in infect and (pos[0] + 1, pos[1] + 1) not in visited:  # lower right
                stack.append((pos[0] + 1, pos[1] + 1))
                visited.append((pos[0] + 1, pos[1] + 1))
                infect.remove((pos[0] + 1, pos[1] + 1))
            if (pos[0] - 1, pos[1] - 1) in infect and (pos[0] - 1, pos[1] - 1) not in visited:  # upper left
                stack.append((pos[0] - 1, pos[1] - 1))
                visited.append((pos[0] - 1, pos[1] - 1))
                infect.remove((pos[0] - 1, pos[1] - 1))
            if (pos[0] + 1, pos[1] - 1) in infect and (pos[0] + 1, pos[1] - 1) not in visited:  # lower left
                stack.append((pos[0] + 1, pos[1] - 1))
                visited.append((pos[0] + 1, pos[1] - 1))
                infect.remove((pos[0] + 1, pos[1] - 1))
            counter.append(len(visited))

    return (max(counter))  # returning max value of infected area

# Task 2


def apocalypse(file_name):
    # file input
    with open(file_name, 'r') as file:
        row = file.readline()
        col = file.readline()
        matrix = [[ele for ele in line.split(' ')] for line in file]

    # removing line break(\n)
    for index in range(len(matrix)):
        matrix[index][-1] = matrix[index][-1].replace('\n', '')

    # creating a touple list of the positions of aliens
    alien = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if 'A' in matrix[row][col]:
                alien.append((row, col))

    # creating a touple list of the positions of humans
    human = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if 'H' in matrix[row][col]:
                human.append((row, col))

    visited = []
    Flag = False
    level = []  # to keep track of the time to kill
    # Applying BFS on every pair o alien touple
    for pair in alien:
        queue = [pair]
        count = 0
        # BFS and checking right, left, up, down for neighbours
        while len(queue):
            pos = queue.pop(0)

            if (pos[0], pos[1] + 1) in human and (pos[0], pos[1] + 1) not in visited:  # right
                queue.append((pos[0], pos[1] + 1))
                visited.append((pos[0], pos[1] + 1))
                Flag = True
            if (pos[0], pos[1] - 1) in human and (pos[0], pos[1] - 1) not in visited:  # left
                queue.append((pos[0], pos[1] - 1))
                visited.append((pos[0], pos[1] - 1))
                Flag = True
            if (pos[0] - 1, pos[1]) in human and (pos[0] - 1, pos[1]) not in visited:  # up
                queue.append((pos[0] - 1, pos[1]))
                visited.append((pos[0] - 1, pos[1]))
                Flag = True
            if (pos[0] + 1, pos[1]) in human and (pos[0] + 1, pos[1]) not in visited:  # down
                queue.append((pos[0] + 1, pos[1]))
                visited.append((pos[0] + 1, pos[1]))
                Flag = True
            # checker to count only when the queue is pushed when neigbour found.
            if (Flag):
                count += 1
                Flag = False
        level.append(count)

    print(f"Time: {max(level)} minutes")

    if (len(visited) == len(human)):
        print("No one survived")
    else:
        print(len(human) - len(visited), "survived")


apocalypse("Question2 input1.txt")
