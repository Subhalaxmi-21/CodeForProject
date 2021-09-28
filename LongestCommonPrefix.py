# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string ""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
#       Initiated common as empty
        comm=""
        for i,j in enumerate(zip(*strs)):
#       Here *strs opened the list into string separated by space
#       zip basically combines individual together
#       Similarly here zip combined each element of string with other element of string returns an object
# enumerate is used for numering purpose
            if j.count(j[0])==len(strs):
                comm+=j[0]
            else:
                break
        return comm 
