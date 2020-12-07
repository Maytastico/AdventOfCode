
f = open("input.txt", "r")
data_A = f.read().split("\n")

A = data_A
B = data_A
C = data_A



for i in range(len(A)-1):
    for j in range(len(B)-1):
        for y in range(len(C)-1):
            if (int(A[i]) + int(B[j]) + int(C[y])) == 2020:
                print(str(A[i]) + " + " + str(B[j]))
                print(str(int(A[i]) * int(B[j]) * int(C[y])))

