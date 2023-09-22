students_grade = [90,45,64,9,17,29]
result = []
for A in students_grade :
    if A >= 71 :
        a = "A"
        result.append(a)
    elif A >= 41 :
        a = "B"
        result.append(a)
    elif A >= 11 :
         a = "C"
         result.append(a)
    else :
         a = "D"
         result.append(a)
print(result)
