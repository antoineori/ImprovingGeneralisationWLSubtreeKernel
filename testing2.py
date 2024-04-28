from parameter import parameter

l = []
with open(parameter.current_A_file, "r") as f:
    for line in f:
        l.append(line.strip())

print(l)
