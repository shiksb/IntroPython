def compress_string(s):
    #Your codes here
    if s == "":
        return ""
    prevString = s[0]
    currCount = 1
    compressed_string = ""

    for i in range(1, len(s)):

        if s[i] == prevString:
            currCount += 1

        else:
            compressed_string += str(currCount) + prevString
            prevString = s[i]
            currCount = 1

    compressed_string += str(currCount) + prevString

    return compressed_string

def decompress_string(s):
    #Your codes here
    decompressed_string = ""
    num = ''

    for c in s:

        if c.isdigit():
            num += c

        else:
            new_string = c*int(num)
            decompressed_string += new_string
            num=''

    return decompressed_string



if __name__ == '__main__':

    input_s = "aaabccaaadaccbbb"
    compressed_s = "3a1b2c3a1d1a2c3b"
    print("Input:", input_s)
    print("Your compressed string result:", compress_string(input_s))
    print("Expected compressed string:", compressed_s)
    compressed_s = '10s10b'
    print("Input:",compressed_s)
    print("Your decompressed string result:",
    	   decompress_string(compressed_s))
    print("Expected decompressed string:", input_s)
