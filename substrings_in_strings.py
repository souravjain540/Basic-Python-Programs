from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permute string s1
        def permute(s: str) -> List[str]:
            # Base case
            if len(s) == 1:
                return [s]

            # Recursive case
            permutations = []
            for i in range(len(s)):
                # Generate all permutations by selecting a character as the first one
                # and permuting the remaining characters
                first_char = s[i]
                remaining_chars = s[:i] + s[i+1:]
                sub_permutations = permute(remaining_chars)

                # Append the first character to each permutation in the sub_permutations
                for perm in sub_permutations:
                    permutations.append(first_char + perm)

            return permutations


        # find the string in s2
        def search(s2: str, my_list: List[str]) -> bool:
            for perm in my_list:
                if perm in s2:
                    return True
            return False


        # Call permute function to generate all permutations of s1
        all_permutations = permute(s1)

        # Check if any permutation is present in s2 using the search function
        result = search(s2, all_permutations)

        return result