def longestPalindrome(s):
    def isPalindrome(s):
        return s == s[::-1]
    def filter_odd(s,i,radius):
        left = i - radius
        right = i + 1 + radius
        if left < 0 or right > len(s):
            return False
        elif isPalindrome(s[left:right]):
            return True
        else:
            return False

    def filter_even(s,i,radius):
        left = i - radius
        right = i + 2 + radius
        if left < 0 or right > len(s):
            return False
        elif isPalindrome(s[left:right]):
            return True
        else:
            return False
    
    longest_odd = ''
    longest_even = ''

    center_odd = [i for i in range(len(s))] # index of center
    center_even = [i for i in range(len(s)-1) if isPalindrome(s[i:i+2])] # index of left center

    radius = 0 # around 1 letter for odd Palindrome and 2 letter for even Palindrome
    while radius <= len(s)//2:
        if len(center_odd) != 0:
            idx = center_odd[0]
            longest_odd = s[idx-radius:idx+1+radius]
        if len(center_even) != 0:
            idx = center_even[0]
            longest_even = s[idx-radius:idx+2+radius]
        radius += 1
        center_odd = [i for i in center_odd if filter_odd(s,i,radius)]
        center_even = [i for i in center_even if filter_even(s,i,radius)]

    if len(longest_odd) > len(longest_even):
        return longest_odd
    else:
        return longest_even


print(longestPalindrome('''abbabadadsdfsdfdasdfagsasfhkasdASDAFShfkashdkfhasksdhfk
asjdgaskgdhasdfjkasgdfasgdkfhaskdfGOGULPRASADDASARPLUGOG
haaaaaaaaaaaaaaaaaahasdfaskdhfkahsdkasgdaesfasghoahkgha
wuigtiuTQERAWsgdasdgasdfasdfasddfasdg
fahafhfdsfasdfasfsbasfdbfsfasfasasahgfasdfaagsfs'''))