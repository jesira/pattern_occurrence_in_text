'''The algorithom i will be using to solve problem 2 is called 'KMP matching algorithm'that uses degenerating property
(pattern having same sub-patterns appearing more than once in the pattern) of the
pattern and improves the worst case complexity to O(n), which if i use nested loop only would be O(m*n).
The working process is provided with comments below '''



def KMPSearch(pat, txt): 
    occur = 0
    pattern_length = len(pat) 
    text_length = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*pattern_length
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, pattern_length, lps)
  
    i = 0 # index for txt[]
    while i < text_length:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == pattern_length:
            occur += 1
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < text_length and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return occur
  
def computeLPSArray(pat, pattern_length , lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < pattern_length:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
  
txt = input("Enter the text: ")
pat = input("Enter the pattern: ")
print(pat, "occurs in", txt, KMPSearch(pat, txt),"times.")