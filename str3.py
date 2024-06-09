def strlen(s):
    return len(s)
def strcpy(s):
    return s[:]
def strcat(s1,s2):
    return s1 + s2
def strstr(s, pattern):
    return s.find(pattern)
def strchr(s,c):
    return len(s) - s[::-1],find(c) - 1
string1 = "Hello"
string2 = "World"
print("Length of string:",strlen(string1))
print("Copy of string:",strcpy(string1))
print("Concatenated string:",strcat(string1,string2))
print("First occurnce of 'lo' in 'Hello':", strstr(string1, "lo"))
print("Last occurance of 'l' in 'Hello':",(string1,"l"))
