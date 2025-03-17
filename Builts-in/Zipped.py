# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())    # number of students, number of subjects

marks = []
for i in range(x):
    subject_marks = list(map(float, input().split()))
    marks = marks + [subject_marks]
    
print(marks)

for item in zip(*marks):
    print(sum(item)/x)