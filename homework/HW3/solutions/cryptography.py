def encrypt_message(message, key):
    #Your codes here
    encrypted_message = ''

    for c in message:

        if c.isalpha():

            if c.isupper():
                new_char = ord(c)+key
                if new_char > ord('Z'):
                    new_char -= 26
                encrypted_message = encrypted_message + chr(new_char)
            else:
                new_char = ord(c)+key
                if new_char > ord('z'):
                    new_char -= 26
                encrypted_message = encrypted_message + chr(new_char)

        else:
            encrypted_message = encrypted_message + c

    return encrypted_message


def decrypt_message(message, key):
    #Your codes here
    decrypted_message = ''
    
    for c in message:

        if c.isalpha():

            if c.isupper():
                new_char = (ord(c)-key)
                if new_char < ord('A'):
                    new_char += 26
                decrypted_message = decrypted_message + chr(new_char)
            else:
                new_char = (ord(c)-key)
                if new_char < ord('a'):
                    new_char += 26
                decrypted_message = decrypted_message + chr(new_char)

        else:
            decrypted_message = decrypted_message + c

    return decrypted_message


def search_key(message):
    #Your codes here
    possible_results_list = []
    for i in range(1,27):
        possible_results_list.append([i,decrypt_message(message,i)])

    return possible_results_list


def encrypt_letter(file_name, key):
    #Your codes here
    file = open(file_name+'.txt','r')
    output_file = open(file_name+'_encrypted.txt','w')

    for line in file:
        encrypted_line = encrypt_message(line,key)
        output_file.write(encrypted_line)
        output_file.write('\n')

    file.close()
    output_file.close()

    return None


def decrypt_letter(file_name, key):
    #Your codes here

    file = open(file_name+'_encrypted.txt','r')
    output_file = open(file_name+'_decrypted.txt','w')

    for line in file:
        decrypted_line = decrypt_message(line,key)
        output_file.write(decrypted_line)
        output_file.write('\n')

    file.close()
    output_file.close()

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

