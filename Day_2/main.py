f = open("input.txt", "r")
data_A = f.read().split("\n")



def parse(line):
    at_least = line[0]
    max = line[2]
    character = line[4]

    to_check = line[7:len(line)]

    print(str(at_least) + str(to_check))
    return

def check(line):
    min = ""
    minSet = False
    max = ""
    maxSet = False
    character = ""
    data_A = ""
    status = 0
    for i in range(len(line)-1):
            if minSet == False:
                if line[i] != "-":
                    if line[i].isnumeric() == True:
                        min += line[i]
                else:
                    minSet = True
            else:
                if maxSet == False:
                    if line[i] != " ":
                        max += line[i]
                    else:
                        maxSet = True
                        status = i
    character = line[status+1]
    data = line[status+3:len(line)]
    if (data[int(min)] == character and data[int(max)] != character) or (data[int(min)] != character and data[int(max)] == character):
        return True
    return False

count = 0
for i in range(len(data_A)-1):
    if check(data_A[i]) == True:
        count += 1

print(count)