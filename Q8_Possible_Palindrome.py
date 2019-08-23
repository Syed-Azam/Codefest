# POSSIBLE PALINDROME
# whether it is possible to build a palindrome from the characters in a string.
def checking_palindrom(st) : 
    count = [0] * (256) 
    for i in range( 0, len(st)) : 
        count[ord(st[i])] = count[ord(st[i])] + 1
    odd = 0
    for i in range(0, 256 ) : 
        if (count[i] & 1) : 
            odd = odd + 1
        if (odd > 1) : 
            return False
    return True
print(checking_palindrom("acabbaa"))
print(checking_palindrom("aabcbaa"))
print(checking_palindrom("aacbdb"))
print(checking_palindrom("abacbb"))