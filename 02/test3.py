with open('input.txt', 'r') as f:
    n = int(f.readline())
    inputs = []
    for i in range(n):
        inputs.append(f.readline()[:-1])
    print(inputs)
