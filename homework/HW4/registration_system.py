def count_all_enrolled_students(d):
    #Your codes here


    return total


def find_invalid_registrations(d, course_code, lab_code):
    #Your codes here



    return invalid

def notify_exam_conflict(d, course_codes):
    #Your codes here



    return conflicts

def hold_workshop(d):
    #Your codes here



    return workshop

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
["Ben","Kelsey","Caro","Yanlin"])

    print("Your exam conflicts:", notify_exam_conflict(d, \
["COMS W3157","ENGI E1006"]))
    print("Expected exam conflicts:", ["Kelsey","Caro"])

    print("Your workshop participants:", hold_workshop(d))
    print("Expected workshop participants:", ["Ben","Yanlin"])
