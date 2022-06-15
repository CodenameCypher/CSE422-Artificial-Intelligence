def alien(file):
    mat = []
    aliens = []
    humans = []
    bfs_counts = []

    with open(file, 'r') as f:
        lines = f.readlines()
        for line in range(2, len(lines)):
            t = lines[line].split(' ')
            t[-1] = t[-1].replace('\n', '')
            t[-1] = t[-1].replace('\t\t', '')
            mat.append(t)

    for row in range(len(mat)):
        for column in range(len(mat[row])):
            if mat[row][column] == 'A':
                aliens.append((row, column))

            if mat[row][column] == 'H':
                humans.append((row, column))

    visited = []
    # bfs from every alien regions
    for p in aliens:
        queue = [p]
        count = 0

        while len(queue) > 0:
            current = queue.pop(0)
            human_found = False

            # checking up
            if (current[0]-1, current[1]) in humans and (current[0]-1, current[1]) not in visited:
                queue.append((current[0]-1, current[1]))
                visited.append((current[0]-1, current[1]))
                human_found = True

            # checking down
            if (current[0]+1, current[1]) in humans and (current[0]+1, current[1]) not in visited:
                queue.append((current[0]+1, current[1]))
                visited.append((current[0]+1, current[1]))
                human_found = True

            # checking left
            if (current[0], current[1]-1) in humans and (current[0], current[1]-1) not in visited:
                queue.append((current[0], current[1]-1))
                visited.append((current[0], current[1]-1))
                human_found = True

            # checking right
            if (current[0], current[1]+1) in humans and (current[0], current[1]+1) not in visited:
                queue.append((current[0], current[1]+1))
                visited.append((current[0], current[1]+1))
                human_found = True

            if human_found == True:
                count += 1

        bfs_counts.append(count)

    print('Time:', str(max(bfs_counts)), 'minutes')

    if len(humans) == len(visited):
        print("No one survived")
    else:
        print(str(len(humans)-len(visited)), 'survived')


alien("Question2 input1.txt")
