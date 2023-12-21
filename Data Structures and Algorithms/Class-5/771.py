def numJewelsInStones(jewels, stones):
    count = 0

    for character in stones:
        if character in jewels:
            count += 1

    return count

print(numJewelsInStones("aADF", "aAAbbbbDF"))