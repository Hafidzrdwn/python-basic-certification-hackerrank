def swapCase(s):
    str = s.split(" ")
    str = " ".join(reversed(str)).swapcase()
    return str


# test
print(swapCase("HeLlo woRLd"))
print(swapCase("IaM MAstEr Of EnginEERing"))
print(swapCase("DoiNG YoU aRe HOW"))
