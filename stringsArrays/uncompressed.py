def uncompressed(s):
    res = ""
    j = 0
    num = ""
    while j < len(s):
        if not s[j].isalpha():
            num += s[j]
        else:
            if not num:
                num = "1"
            res += s[j] * int(num)
            num = ""
        j += 1


    return res

print(uncompressed("127y"))
print(len("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
