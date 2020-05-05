from collections import defaultdict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_to_marks = defaultdict(list)

        for item in items:
            student_to_marks[item[0]].append(item[1])

        answer = []
        for st_id, marks in student_to_marks.items():
            marks.sort()
            answer.append([st_id, sum(marks[max(len(marks) - 5, 0):]) // 5])

        return answer

# 91, 92, 60, 65, 87, 100
# 495