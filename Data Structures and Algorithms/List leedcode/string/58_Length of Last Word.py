class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        space = False
        for i in range(len(s)):
            if s[i] == ' ':
                space = True
            elif s[i] != ' ' and space:
                count = 1
                space = False
            else:
                count += 1
        return count
name = 'shakil, shomon, shohel'
# Test the function
solution = Solution()
print(solution.lengthOfLastWord(name))


class Solution(object):
    def wordCount(self, s):
        count = 0
        space = True  # Start with space=True to handle cases where the string starts with a word
        for i in range(len(s)):
            if s[i] == ' ':
                space = True
            elif s[i] != ' ' and space:
                count += 1
                space = False
        return count

# Test the function
solution = Solution()
name = 'shakil, shomon, shohel'
print(solution.wordCount(name))  # Output should be 3



class Solution(object):
    def wordCount(self, s):
        words = s.split()  # Split the string into words based on spaces
        return len(words)  # Return the count of words

    def lengthOfLastWord(self, s):
        words = s.split()  # Split the string into words based on spaces
        if len(words) == 0:  # If there are no words, return 0
            return 0
        else:
            return len(words[-1])  # Return the length of the last word

# Test the functions
solution = Solution()
name = 'shakil, shomon, shohel'
print("Number of words:", solution.wordCount(name))  # Output should be 3
print("Length of last word:", solution.lengthOfLastWord(name))  # Output should be 6
