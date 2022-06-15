import random
import math

count = 0


def minimax(tree, branch, depth, alpha, beta, maximizing_player):
    global count
    if depth == 0:
        value = tree[count]
        count += 1
        return value
    if maximizing_player == True:
        max_val = -math.inf
        for i in range(branch):
            evaluated = minimax(tree, branch, depth-1, alpha, beta, False)
            max_val = max(max_val, evaluated)
            alpha = max(alpha, evaluated)
            if alpha >= beta:
                break
        return max_val
    else:
        min_val = math.inf
        for ind in range(branch):
            evaluated = minimax(tree, branch, depth-1, alpha, beta, True)
            min_val = min(min_val, evaluated)
            beta = min(beta, evaluated)
            if alpha >= beta:
                break
        return min_val


def alpha_beta_pruning(student_id, min_value, max_value):
    global count
    depth = 2 * int(student_id[0])
    hp = int(student_id[-2:][::-1])
    branch = int(student_id[2])
    leafs = random.sample(range(min_value, max_value+1), pow(branch, depth))
    tree = leafs
    print('1. Depth and Branches ratio is '+str(depth)+":"+str(branch))
    print('2. Terminal States (leaf node values) are', str(leafs)[1:-1])

    damage = minimax(tree, branch, depth, -math.inf, math.inf, True)

    print("3. Left life(HP) of the defender after maximum damage caused by the attacker is", hp - damage)
    print('4. After Alpha-Beta Pruning Leaf Node Comparisons', count)


student_ID = input("Enter your student ID:")
min_value, max_value = map(int, input(
    "Minimum and Maximum value for the range of negative HP:").split())

alpha_beta_pruning(student_ID, min_value, max_value)
