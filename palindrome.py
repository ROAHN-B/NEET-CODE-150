# s = "Madam, in Eden, I'm Adam"
# sc = ["?", "!", "#", "$", "%", "^", ",", "'"]
# t = s.lower()
# string = "".join(t.split())
# print(string)
# output = []
# for ele in string:
#     if ele not in sc:
#         output.append(ele)
# print(output)
# reverse = output[::-1]
# print(reverse)

# if output == reverse:
#     print("True")
# else:
#     print("False")

###############################TWO POINTER APPROACH########################################
s = "1001"
L, R = 0, len(s) - 1

is_palindrome = True


def alphanum(c):
    return (
        (ord("A") <= ord(c) <= ord("Z"))
        or (ord("a") <= ord(c) <= ord("z"))
        or (ord("0") <= ord(c) <= ord("9"))
    )


while L < R:
    while L < R and not alphanum(s[L]):
        L += 1
    while L > R and not alphanum(s[R]):
        R -= 1
    if s[L].lower() != s[R].lower():
        print(False)
        is_palindrome = False
        break
    L, R = L + 1, R - 1

if is_palindrome:
    print(True)
