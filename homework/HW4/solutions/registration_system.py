def get_all_students(d):
    all_students = set()
    for course_code in d:
        curr_class_set = set(d[course_code])
        all_students = all_students.union(curr_class_set)
    return all_students

def count_all_enrolled_students(d):
    all_students = get_all_students(d)
    total = len(all_students)
    return total

def find_invalid_registrations(d, course_code, lab_code):
    course_students = set(d[course_code])
    lab_students = set(d[lab_code])
    invalid = course_students.symmetric_difference(lab_students)
    return list(invalid)

def notify_exam_conflict(d, course_codes):
    conflicts = set()
    for course_code1 in course_codes:
        for course_code2 in course_codes:
            if course_code1 == course_code2:
                continue
            students_course1 = set(d[course_code1])
            students_course2 = set(d[course_code2])
            conflicting_students = students_course1.intersection(students_course2)
            conflicts = conflicts.union(conflicting_students)
    return list(conflicts)

def hold_workshop(d):
    best_coursecode = "ENGI E1006"
    all_students = get_all_students(d)
    if best_coursecode in d:
        best_students = set(d[best_coursecode])
    else:
        best_students = set()
    workshop = all_students.difference(best_students)
    return list(workshop)

if __name__ == '__main__':

    d = {}
    d["ENGI E1006"] = ["Shreyas","Vidya","Kelsey","Caro"]
    d["COMS W3157"] = ["Ben","Kelsey","Caro","Yanlin"]
    d["COMS W3158"] = []

    print("Input Dictionary:", d)
    print("Your number of students:", count_all_enrolled_students(d))
    print("Expected number of students:", 6)

    print("Your invalid registrations:", find_invalid_registrations(d,\
"COMS W3157","COMS W3158"))
    print("Expected invalid registrations:", \
set(["Ben","Kelsey","Caro","Yanlin"]))

    print("Your exam conflicts:", notify_exam_conflict(d, \
["COMS W3157","ENGI E1006"]))
    print("Expected exam conflicts:", set(["Kelsey","Caro"]))

    print("Your workshop participants:", hold_workshop(d))
    print("Expected workshop participants:", ["Ben","Yanlin"])
