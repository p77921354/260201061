gpa = float(input("your gpa? "))
lecture_hours = int(input("how many hours of lectures did you take? "))

if gpa < 2.0 and lecture_hours < 47:
  print("not enough number of lectures and GPA")
elif gpa >= 2.0 and lecture_hours >= 47:
  print("GRADUATED!!!")
elif gpa >= 2.0 and lecture_hours < 47:
  print("not enough number of lectures")
elif gpa < 2.0 and lecture_hours >= 47:
  print("not enough GPA")