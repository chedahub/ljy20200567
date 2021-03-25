import random

total_students = 30
total_teams = 10

students = range(total_students)
list_students = list(students)

#shuffle은 return이 있는 함수가 아니다. 원래의 list를 섞어준다.
random.shuffle(list_students)
#print(list_students)

#랜덤하게 5명씩 총 6개의 팀을 만들어보자
project_team = []
for i in range(6):
    # i = 0, 1, 2, 3, 4, 5 -> 0 5 10 15 20 25가 각 팀의 첫 번째 멤버 인덱스.
    num_of_members = int(total_students/total_teams)
    index = i * num_of_members
    #.append(): 리스트에 요소 추가
    project_team.append(list_students[index:index+num_of_members])

for i in project_team:
    print(i)