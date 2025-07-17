class Solution(object):
    def wordPattern(self, pattern, s):
        def normalize(seq):
            mapping = {}
            normalized = []
            next_char = 'a'
            for item in seq:
                if item not in mapping:
                    mapping[item] = next_char
                    next_char = chr(ord(next_char) + 1)
                normalized.append(mapping[item])
            return normalized

        words = s.split()
        pattern_list = list(pattern)

        if len(words) != len(pattern_list):
            return False

        return normalize(words) == normalize(pattern_list)
