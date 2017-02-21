def compress_string(s):
    #Your codes here


    return compressed_string


def decompress_string(s):
    #Your codes here



    return decompressed_string



if __name__ == '__main__':

    input_s = "aaabccaaadaccbbb"
    compressed_s = "3a1b2c3a1d1a2c3b"
    print("Input:", input_s)
    print("Your compressed string result:", compress_string(input_s))
    print("Expected compressed string:", compressed_s)

    print("Input:",compressed_s)
    print("Your decompressed string result:",
    	   decompress_string(compressed_s))
    print("Expected decompressed string:", input_s)
