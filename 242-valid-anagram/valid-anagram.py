class Solution(object):
    def isAnagram(self, s, t):
        count_letters_s={}
        count_letters_t={}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                count_letters_s[s[i-1]] = s.count(s[i-1])
                count_letters_t[t[i-1]] = t.count(t[i-1])
        if count_letters_s == count_letters_t:
            return True
        else:
            return False