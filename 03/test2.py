
print ("\n#####CSE-422-Lab3-Tamanna-Afroz-18301153#####\n")

import random as r
import math
def minimax(leaf_nodes, branches, depth, alpha, beta, isMaximizingPlayer=True):
    global itr_count
    if depth == 0:
        leaf_val = leaf_nodes[itr_count]
        itr_count+=1
        return leaf_val
    if isMaximizingPlayer == True:
        max_val = -math.inf
        for ind in range(branches):
            val = minimax(leaf_nodes, branches, depth-1, alpha, beta, False)
            max_val = max(max_val, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return max_val
    else:
        min_val = math.inf
        for ind in range(branches):
            val = minimax(leaf_nodes, branches, depth-1, alpha, beta, True)
            min_val = min(min_val, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return min_val

student_id = input("Enter your student id: ")
turns = int(student_id[0])*2
initial_HP = int(student_id[-2:][::-1])
branches = int(student_id[2])

mini,maxi = [int(x) for x in input("Minimum and Maximum value for the range of negative HP: ").split()]

x = 1
leaf_nodes = []
while x <= branches**turns:
    leaf_nodes.append(r.randrange(mini,maxi))
    x+=1
print(leaf_nodes)
itr_count = 0
damage = minimax(leaf_nodes,branches,turns,-math.inf,math.inf)

print("\nDepth and Branches ratio is", turns,":",branches)
print("Terminal States (leaf node values) are ",end='')
for i in leaf_nodes:
    if i != leaf_nodes[-1]:
        print(f"{i},",end='')
    else:
        print(f"{i}.")
print("Left life(HP) of the defender after maximum damage caused by the attacker is", initial_HP - damage)
print("After Alpha-Beta Pruning Leaf Node Comparisons", itr_count)