class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count=0
        i=0
        while students:
            # print(students[0],sandwiches[0])
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)  
                count=0
                # print(students,sandwiches)
            else:
                students.append(students.pop(0))
                count+=1
            if count==len(students):
                break
        if students:
            return len(students)
        else:
            return 0
