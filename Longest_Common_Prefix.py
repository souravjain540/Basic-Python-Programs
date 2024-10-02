def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix)-1]
    return prefix

# Example Usage:
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"
