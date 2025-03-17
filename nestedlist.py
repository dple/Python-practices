# Return the second element in a list record
def getScore(record):
    return record[1]


# Get the list of students with the second-lowest score
if __name__ == '__main__':
    # Nested list of students, each record contains with a student name and a grade
    records = []

    for _ in range(int(input())):
        name = input()
        grade = float(input())
        records.append([name, grade])

    # Sort the student list by their grade
    records.sort(key=getScore)
    nameList = []

    # Get the lowest score
    m = records[0][1]

    for i in range(1, len(records)):
        if records[i][1] > m:   # Get the second-lowest grade in the student list
            # Another way to get the second-lowest grade in a list is to convert the list to
            # set (containing only unrepeated elements), sort it, then select the second element
            nameList.append(records[i][0])
            for j in range(i + 1, len(records)):
                if records[j][1] == records[i][1]:
                    nameList.append(records[j][0])
                else:
                    break
            break

    nameList.sort()
    for name in nameList:
        print(name)
