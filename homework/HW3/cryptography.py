def encrypt_message(message, key):
    #Your codes here




    return encrypted_message


def decrypt_message(message, key):
    #Your codes here





    return decrypted_message


def search_key(message):
    #Your codes here



    return possible_results_list


def encrypt_letter(file_name, key):
    #Your codes here



    return None


def decrypt_letter(file_name, key):
    #Your codes here



    return None



if __name__ == '__main__':

    input_s = "Hello Zoe!"
    test_key = 2
    encrypted_s = "Jgnnq Bqg!"
    print("Input:", input_s)
    print("Your encrypted string:", encrypt_message(input_s,test_key))
    print("Expected encrypted string:", encrypted_s)

    print("Input:", encrypted_s)
    print("Your decrypted string:", decrypt_message(encrypted_s,test_key))
    print("Expected decrypted string:", input_s)


