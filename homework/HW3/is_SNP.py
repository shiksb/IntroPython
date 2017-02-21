def is_SNP(s1,s2):
    #Your codes here








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




