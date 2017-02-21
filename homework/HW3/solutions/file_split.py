def file_split(f):
    #Your codes here
    file = open(f+'.txt','r')
    even_file = open(f+'_even.txt','w')
    odd_file = open(f+'_odd.txt','w')

    lines = file.readlines()

    if len(lines)==0:
        return None
    if len(lines)==1:
        even_file.writelines(lines)
        return None
    even_file.writelines(lines[::2])
    odd_file.writelines(lines[1::2])
    
    file.close()
    even_file.close()
    odd_file.close()
    
    return None

file_split('abc')