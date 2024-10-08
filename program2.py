class Solution(object):
    def romanToInt(self, s):
        
        # Mapping of Roman numerals to their integer values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Initialize the total sum
        total = 0
        
        # Iterate over the string, checking each numeral
        for i in range(len(s)):
            # If the current numeral is smaller than the next one, subtract it
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, add it
                total += roman_map[s[i]]
        
        return total
    pass


