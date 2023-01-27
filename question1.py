# Write a Python program that finds the longest common substring between two strings.

str1 = "hello"
str2 = "vaibhav"

m =len(str1)
n = len(str2)

counter = [[0 for x in range(n+1)] for y in range(m+1)]
# print(counter)

longest = 0
# set1 = set()
for i in range (m+1):
    for j in range(n+1):
        if (i == 0 or j == 0):
            counter[i][j] = 0
        elif (str1[i-1] == str2[j-1]):
            counter[i][j] = counter[i-1][j-1]+1
            longest = max(longest, counter[i][j])
            
        else:
            counter[i][j] = 0
            
print(longest)
                
                
# print(set1)