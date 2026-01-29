def encode(self, input: list[str]) -> str:
    res = ""
    for s in input:
        res += str(len(s)) + "#" + s
    print(res)


def decode(self, input: str) -> list[str]:
    ret, i = [], 0
    while i < len(ret):
        j = i
        while input(j) != "#":
            j += 1
            length = int(input[i:j])
            ret.append(input[j + 1 : j + 1 + length])
            i = j + 1 + length
        print(ret)


encode(["Hello", "World"])
