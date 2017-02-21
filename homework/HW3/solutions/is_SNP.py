def check_insert(s1,s2):
    for i in range(len(s1)):
        if s1[:i]+s1[i+1:] == s2:
            return True
    return False
    
def check_mutation(s1,s2):
    status = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if status == False:
                status = True
            else:
                return False
    return status
        

def is_SNP(s1,s2):
    #Your codes here
    if len(s1) == 0 or len(s2) == 0:
        return len(s1) == 1 or len(s2) == 1

    if len(s1) == 0 and len(s2) == 0:
        return False

    result = False

    #checking for deletion
    if len(s1)>len(s2):
        result = check_insert(s1,s2)
    
    #checking for insertion
    elif len(s2)>len(s1):
        result = check_insert(s2,s1)
    
    #checking for mutation
    else:
        result = check_mutation(s1,s2)
    
    return result



if __name__ == '__main__':

    DNA1 = "AGATCTA"
    DNA2 = "AGATCGA"
    print("Input:", DNA1, "and", DNA2)
    print("Your result:", is_SNP(DNA1,DNA2))
    print("Expected result:", True)

    DNA1 = "AGATCTA"
    DNA2 = "CCCCCCC"
    print("Input:", DNA1, "and", DNA2)
    print("Your result:", is_SNP(DNA1,DNA2))
    print("Expected result:", False)

    DNA1 = "A"
    DNA2 = "AC"
    print("Input:", DNA1, "and", DNA2)
    print("Your result:", is_SNP(DNA1,DNA2))
    print("Expected result:", True)




