def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_count, t _count = {}, {}

    for i in range(len(s)):
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        t_count[t[i]] = t_count.get(t[i], 0) + 1
    return s_count == t_count