# MY APPROACH
# def uncompressed(s):
#     res = ""
#     j = 0
#     num = ""
#     while j < len(s):
#         if not s[j].isalpha():
#             num += s[j]
#         else:
#             if not num:
#                 num = "1"
#             res += s[j] * int(num)
#             num = ""
#         j += 1

#     return res

#STRUCTY APPRAOCH
# COMPLEXITY ANALYSIS
"""
let n =  number if groups
    m = max number for any group

    The time complexity would be O(n*m)
    The space complxity is also the same

    NB
    The time complexity for string concatenation
"""

def uncompressed(s):
    i = 0
    j = 0
    res = []
     
    while j < len(s):
        if not s[j].isalpha():
            j += 1
        else:
            if not s[i:j]:
                res.append(s[j])
            else:
                res.append(s[j] * int(s[i:j]))
            j += 1
            i = j
    return "".join(res)

print(uncompressed("e3ff"))
        
