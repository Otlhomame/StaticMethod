class Student:
  def __init__(self, scores=[]):
    self.scores = scores

  def avg(self):
    return round(sum(self.scores) /len(self.scores))
  
  @staticmethod
  def notice():
    return "Exams Next Week!"

Kingsley= Student(scores= [3,4,5,6,8])

print(Kingsley.notice())
print(Student.notice())

