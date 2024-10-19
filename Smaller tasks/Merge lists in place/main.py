B = [3, 3, 4]
A = [1, 2, 4, 5, 8, *([0] * len(B))]

pt_merged = len(A) - 1
pt_a = len(A) - len(B) - 1
pt_b = len(B) - 1

while pt_b >= 0:
    if B[pt_b] > A[pt_a]:
        A[pt_merged] = B[pt_b]
        pt_b -= 1
    else:
        A[pt_merged] = A[pt_a]
        pt_a -= 1
    pt_merged -= 1

print(A)
