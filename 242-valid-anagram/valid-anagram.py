class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count_letters_s = {}
        count_letters_t = {}

        for i in range(len(s)):
            count_letters_s[s[i]] = count_letters_s.get(s[i], 0) + 1
            count_letters_t[t[i]] = count_letters_t.get(t[i], 0) + 1

        return count_letters_s == count_letters_t
