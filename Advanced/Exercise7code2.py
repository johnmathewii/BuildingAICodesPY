import numpy as np


def generate(p1):
    seq = np.random.choice([0, 1], p=[1-p1, p1], size=10000)
    return seq

# Generates Pairs instead of the usual sequence
# # def count(seq):
#     outerCount = 0
#     i = -1
#     while (i < len(seq)-1):
#         innerCount = 5
#         i = i + 1
#         while (seq[i] == 1):
#             innerCount = innerCount - 1
#             if innerCount == 0:
#                 outerCount = outerCount + 1
#                 break
#             else:
#                 i = i + 1
#                 if i == len(seq):
#                     break
#                 continue
#     return outerCount

def count(seq):
    outerCount = 0
    for i in range(0, len(seq)-1):
        innerCount = 5
        while (seq[i] == 1):
            innerCount = innerCount - 1
            if innerCount == 0:
                outerCount = outerCount + 1
                break
            else:
                i = i + 1
                if i == len(seq):
                    break
                continue
    return outerCount


def main(p1):
    seq = generate(p1)
    return count(seq)


print(main(2/3))
