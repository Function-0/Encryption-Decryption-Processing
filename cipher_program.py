"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message-decrypted.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    """
    # Open deck file handle
    message_file_handle = open(MSG_FILENAME, 'r')
    # Open message file handle
    deck_file_handle = open(DECK_FILENAME, 'r')
    # Retrieve the data from the message file handle
    messages_to_process = cipher_functions.read_messages(message_file_handle)
    # Retrieve the data from the deck file handle
    card_deck = cipher_functions.read_deck(deck_file_handle)
    # Close deck file handle
    message_file_handle.close()
    # Close message file handle
    deck_file_handle.close()
    # Process the messages retrieved
    processed_messages = (
        cipher_functions.process_messages(card_deck, messages_to_process, MODE)
        )
    # Go through each processed message
    for new_message in processed_messages:
        # Outputs the processed message
        print(new_message)

main()
