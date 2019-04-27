import cipher_functions as test

## Opens and outputs message-decrypted.txt
#message_decrypted_file_handle = open("message-decrypted.txt", 'r')
#message_decrypted_copy = message_decrypted_file_handle.readlines()
#message_decrypted_file_handle.close()
#print(message_decrypted_copy)
## Opens and outputs message-encrypted.txt
#message_decrypted_file_handle = open("message-encrypted.txt", 'r')
#message_decrypted_copy = message_decrypted_file_handle.readlines()
#message_decrypted_file_handle.close()
#print(message_decrypted_copy)
## Opens and outputs deck1.txt
#message_decrypted_file_handle = open("deck1.txt", 'r')
#message_decrypted_copy = message_decrypted_file_handle.readlines()
#message_decrypted_file_handle.close()
#print(message_decrypted_copy)
## Opens and outputs deck2.txt
#message_decrypted_file_handle = open("deck2.txt", 'r')
#message_decrypted_copy = message_decrypted_file_handle.readlines()
#message_decrypted_file_handle.close()
#print(message_decrypted_copy)
# Indexed loop: Opens and outputs all secret files 1 through 8
for text_file in range(1, 9):
    text_file_handle = open("secret" + str(text_file) + ".txt", 'r')
    text_file_copy = text_file_handle.readlines()
    
    # print(text_file_copy)
    print(test.read_messages(text_file_handle), text_file)
    # text_file_handle.close()
    
message_file_handle = open("secret" + str(4) + ".txt", 'r')  
for line in message_file_handle.readlines():
    print(line.strip()) 