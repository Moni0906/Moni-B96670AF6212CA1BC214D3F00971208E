






class Student:

  def                                    __init__(self,name,roll_number,chpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = chpa


def sort_students(Student_list):

  sorted_student =                       sorted(student_list,
   key = lambda student: Student.cgpa,
    reverse = True)

  return sorted_students   



  students = [
  student ("Hari","A123",7.8),
  student ("Srikanth","A124",8.9),
  student ("Saumya","A125",9.1),
  student ("Mathindhar","A126",9.9)
  ]
  

  sorted_student =                       sort_students(students)



  for student in sorted_students:
    print ("Name:{},Roll Number:       {},CGPA:{}".format ( student.name,
    student.name,
    student.cgpa))
    
