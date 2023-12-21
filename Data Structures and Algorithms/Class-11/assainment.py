def can_defeat_monster(T, test_cases):
    results = []
    for i in range(T):
        H, X, Y = test_cases[i]
        if X >= H:
            results.append(1)  # If damage is greater than or equal to health, monster is defeated
        elif X < H and X <= Y:
            results.append(0)  # If damage is less than health and less than or equal to health gain, not defeated
        else:
            results.append(1)  # If damage is less than health but more than health gain, defeated eventually
    return results

# Example usage:
T = 4
test_cases = [
    (3, 6, 2),
    (4, 6, 3),
    (7, 1, 2),
    (1, 1, 2)
]

results = can_defeat_monster(T, test_cases)
for result in results:
    print(result)