if __name__ == '__main__':
    # Dictionary of student marks, key = name, scores is a list
    student_marks = {}

    # Get the number of students
    n = int(input())

    for _ in range(n):
        # Here a single asterisk (*) is used to pass a variable-length list of scores
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    # Get a student name to list her average scores
    query_name = input()
    scores = student_marks[query_name]
    avg = sum(scores) / len(scores)

    # print using %-formatting
    print("%.2f" % avg)
    # print using str.format
    print("{:.2f}".format(avg))
    # print using f-strings format
    print(f"{avg:.2f}")

