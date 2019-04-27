# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:
# ============================================================================
# Values of the two Joker Cards (Because I perfer pothole writing)
JOKER_1 = 27
JOKER_2 = 28

# Length of alphabet the custom Stream Cipher will operate on
LEN_ALPHABET = 26

# Holds all possible punctuation characters
STR_PUNCTUATION = """!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ """
# Holds all possible number characters
STR_DIGITS = """0123456789"""
# Holds all possible non-alphabetical characters
NON_ALPHABETICAL_CHARACTERS = STR_PUNCTUATION + STR_DIGITS

# Negates the ordinance value of capitalized letters to fit in the
# domain characterized by: A = 0; Z = 25
IGNORE_ORDINANCE = 65
# Example 1 (Translate a capitalized letter to a number):
# |ord('A') = 65| ---> |(ord('A') - IGNORE_ORDINANCE) = 0|
# Example 2 (Translate a number to a capitalized letter):
# |chr(0) = not a letter| ---> |chr(0 + IGNORE_ORDINANCE) = 'A'|


def clean_message(message_with_punctuation):
    '''(str) -> str
    Given a message_with_punctuation: Returns said message with no
    non-alphabetical characters present, and with all available letters
    within the given message capitalized.

    REQ: message_with_punctuation restricted to having no escape characters
    present

    >>> clean_message('')
    ''

    >>> clean_message(' ')
    ''

    >>> clean_message("     ")
    ''

    >>> clean_message("i'm lazy")
    'IMLAZY'

    >>> clean_message("I'M SERIOUS")
    'IMSERIOUS'

    >>> clean_message("!m I+=>gh^_t Y9")
    'MIGHTY'

    >>> clean_message("|-@3/[3)4>[]/9]")
    ''

    >>> clean_message("I'm standard?")
    'IMSTANDARD'

    >>> clean_message("coMbINatioN")
    'COMBINATION'
    '''
    # Holds the clean message; Start with the original message
    clean_message = message_with_punctuation
    # Fully capitalize the message
    clean_message = clean_message.upper()
    # Go through each non-alphabetical character
    for non_alpha_char in NON_ALPHABETICAL_CHARACTERS:
        # If a non-alphabetical character is present in the message
        if (non_alpha_char in clean_message):
            # Remove all instances of the non-alphabetical character from the
            # given string, and assign it to our clean message
            clean_message = clean_message.replace(non_alpha_char, '')
    # Returns the new message, fully capitalized and containing only letters
    return clean_message


# PERSONAL FUNCTION 1:
def generate_letter(letter_value):
    '''(int) -> str
    Given a letter_value: Returns the matching letter associated with said
    letter_value.

    REQ: None

    >>> generate_letter(120)
    'Q'

    >>> generate_letter(-90)
    'O'

    >>> generate_letter(5)
    'F'
    '''
    # Force the number to be between 0 — 25, to have a valid number to
    # translate to a new letter
    letter_id = letter_value % LEN_ALPHABET
    # Retrieve the letter associated with the valid number
    new_letter = chr(letter_id + IGNORE_ORDINANCE)
    # Returns the created letter
    return new_letter


def encrypt_letter(letter_to_encrypt, encryption_keystream_value):
    '''(str, int) -> str
    Given a letter_to_encrypt; and a encryption_keystream_value: Returns
    an encrypted capitalized letter based on the sum of the letter value
    of letter_to_encrypt, to the encryption_keystream_value.

    REQ: letter_to_encrypt restricted to single capitalized alphabetical
    letters

    >>> encrypt_letter('A', 1)
    'B'

    >>> encrypt_letter('Z', 26)
    'Z'

    >>> encrypt_letter('Z', 25)
    'Y'

    >>> encrypt_letter('A', 17)
    'R'

    >>> encrypt_letter('O', 19)
    'H'

    >>> encrypt_letter('P', 105)
    'Q'

    >>> encrypt_letter('C', -90)
    'Q'
    '''
    # Compute the sum of the given letter to the keystream value
    raw_sum = ((ord(letter_to_encrypt) - IGNORE_ORDINANCE) +
               encryption_keystream_value)
    # Helper function: Retrieve the letter associated with the sum
    encrypted_letter = generate_letter(raw_sum)
    # Returns the created encrypted letter
    return encrypted_letter


def decrypt_letter(letter_to_decrypt, decryption_keystream_value):
    '''(str, int) -> str
    Given a letter_to_decrypt; and a decryption_keystream_value: Returns
    a decrypted capitalized letter based on the difference of the letter
    value of letter_to_decrypt, to the decryption_keystream_value.

    REQ: letter_to_decrypt restricted to single capitalized alphabetical
    letters

    >>> decrypt_letter('B', 1)
    'A'

    >>> decrypt_letter('Z', 26)
    'Z'

    >>> decrypt_letter('Y', 25)
    'Z'

    >>> decrypt_letter('R', 17)
    'A'

    >>> decrypt_letter('H', 19)
    'O'

    >>> decrypt_letter('Q', 105)
    'P'

    >>> decrypt_letter('Q', -90)
    'C'
    '''
    # Compute the difference of the given letter to the keystream value
    raw_difference = ((ord(letter_to_decrypt) - IGNORE_ORDINANCE) -
                      decryption_keystream_value)
    # Helper function: Retrieve the letter associated with the difference
    decrypted_letter = generate_letter(raw_difference)
    # Returns the created decrypted letter
    return decrypted_letter


def swap_cards(card_deck, position_to_swap):
    '''(list of int, int) -> NoneType
    Given a card_deck; and a position_to_swap within said card_deck: Mutates
    the card_deck list to force the card located at index position_to_swap to
    exchange places with the proceeding card in said list.

    Note: If position_to_swap points to the last index of the list, swap with
    the first card in card_deck instead.

    REQ: position_to_swap restricted to valid index values in card_deck

    >>> test_card_deck = [1, 2, 3, 4, 5]
    >>> swap_cards(test_card_deck, 0)
    >>> test_card_deck == [2, 1, 3, 4, 5]
    True

    >>> test_card_deck = [1, 2, 3, 4, 5]
    >>> swap_cards(test_card_deck, -1)
    >>> test_card_deck == [5, 2, 3, 4, 1]
    True

    >>> test_card_deck = [1, 2, 3, 4, 5]
    >>> swap_cards(test_card_deck, 4)
    >>> test_card_deck == [5, 2, 3, 4, 1]
    True

    >>> test_card_deck = [1, 2, 3, 4, 5]
    >>> swap_cards(test_card_deck, -5)
    >>> test_card_deck == [2, 1, 3, 4, 5]
    True

    >>> test_card_deck = [1, 2, 3, 4, 5]
    >>> swap_cards(test_card_deck, 2)
    >>> test_card_deck == [1, 2, 4, 3, 5]
    True

    >>> test_card_deck = [1, 2, 3, 4, 5]
    >>> swap_cards(test_card_deck, -3)
    >>> test_card_deck == [1, 2, 4, 3, 5]
    True
    '''
    # Obtain the total number of cards found in the card deck
    total_cards = len(card_deck)
    # Obtain the index-position of the proceeding card to swap with
    next_card = position_to_swap + 1
    # Swap the two cards within the deck with eachother
    (card_deck[position_to_swap], card_deck[next_card % total_cards]) = (
        (card_deck[next_card % total_cards], card_deck[position_to_swap]))
    # NOTE: We used |modulus(number of cards in card deck)| for the proceeding
    # card's index-position to factor in that we are treating this list with a
    # circular property.
    # Therefore, if position_to_swap points to the last index-position of the
    # given list, the proceeding card to follow is forced to be the one at the
    # start of the list.


# STEP ONE OF CUSTOM STREAM CIPHER ALGORITHM
def move_joker_1(card_deck):
    '''(list of int) -> NoneType
    Given a card_deck: Mutates the card_deck list to force the card
    that equals 27 (Joker Card 1) to exchange places with the proceeding
    card in said list.

    Note: If Joker Card 1 is the last element of the list, swap with
    the first card in card_deck instead.

    REQ: card_deck element (Joker Card 1 = 27) required to be within list

    >>> JOKER_1 = 27
    >>> test_card_deck = [1, 2, 3, 4, JOKER_1]
    >>> move_joker_1(test_card_deck)
    >>> test_card_deck == [JOKER_1, 2, 3, 4, 1]
    True

    >>> JOKER_1 = 27
    >>> test_card_deck = [JOKER_1, 2, 3, 4, 5]
    >>> move_joker_1(test_card_deck)
    >>> test_card_deck == [2, JOKER_1, 3, 4, 5]
    True

    >>> JOKER_1 = 27
    >>> test_card_deck = [1, 2, JOKER_1, 4, 5]
    >>> move_joker_1(test_card_deck)
    >>> test_card_deck == [1, 2, 4, JOKER_1, 5]
    True
    '''
    # Obtain the index-position number of Joker Card 1
    joker_card_1_position = card_deck.index(JOKER_1)
    # Helper function: Swaps Joker Card 1 once with the proceeding card
    swap_cards(card_deck, joker_card_1_position)


# STEP TWO OF CUSTOM STREAM CIPHER ALGORITHM
def move_joker_2(card_deck):
    '''(list of int) -> NoneType
    Given a card_deck: Mutates the card_deck list to force the card
    that equals 28 (Joker Card 2) to exchange places with the proceeding
    card in said list. The aforementioned process occurs twice.

    Note: If Joker Card 2 becomes the last element of the list during one of
    the processes, swap with the first card in card_deck instead during said
    process.

    REQ: card_deck element (Joker Card 2 = 28) required to be within list

    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 2, 3, 4, JOKER_2]
    >>> move_joker_2(test_card_deck)
    >>> test_card_deck == [2, JOKER_2, 3, 4, 1]
    True

    >>> JOKER_2 = 28
    >>> test_card_deck = [JOKER_2, 2, 3, 4, 5]
    >>> move_joker_2(test_card_deck)
    >>> test_card_deck == [2, 3, JOKER_2, 4, 5]
    True

    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 2, JOKER_2, 4, 5]
    >>> move_joker_2(test_card_deck)
    >>> test_card_deck == [1, 2, 4, 5, JOKER_2]
    True
    '''
    # Move Joker Card 2 twice
    for swap_num in range(2):
        # Obtain the index-position number of Joker Card 2
        joker_card_2_position = card_deck.index(JOKER_2)
        # Helper function: Swaps Joker Card 2 once with the proceeding card
        swap_cards(card_deck, joker_card_2_position)


# STEP THREE OF CUSTOM STREAM CIPHER ALGORITHM
def triple_cut(card_deck):
    '''(list of int) -> NoneType
    Given a card_deck: Mutates the card_deck list to force the group of cards
    preceeding the lowest index-positioned card equalling
    27 or 28 (Joker Card 1 or Joker Card 2) to exchange places with the
    group of cards proceeding the highest index-positioned Joker
    Card inside said list.

    REQ: card_deck elements (Joker Card 1 = 27), (Joker Card 2 = 28)
         required to be within list

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 2, JOKER_1, JOKER_2, 5]
    >>> triple_cut(test_card_deck)
    >>> test_card_deck == [5, JOKER_1, JOKER_2, 1, 2]
    True

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 2, JOKER_2, JOKER_1, 5]
    >>> triple_cut(test_card_deck)
    >>> test_card_deck == [5, JOKER_2, JOKER_1, 1, 2]
    True

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [JOKER_1, 2, 3, 4, JOKER_2]
    >>> triple_cut(test_card_deck)
    >>> test_card_deck == [JOKER_1, 2, 3, 4, JOKER_2]
    True

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [JOKER_2, 2, 3, 4, JOKER_1]
    >>> triple_cut(test_card_deck)
    >>> test_card_deck == [JOKER_2, 2, 3, 4, JOKER_1]
    True

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, JOKER_1, JOKER_2, 4, 5]
    >>> triple_cut(test_card_deck)
    >>> test_card_deck == [4, 5, JOKER_1, JOKER_2, 1]
    True

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, JOKER_2, JOKER_1, 4, 5]
    >>> triple_cut(test_card_deck)
    >>> test_card_deck == [4, 5, JOKER_2, JOKER_1, 1]
    True

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, JOKER_1, 3, JOKER_2, 5]
    >>> triple_cut(test_card_deck)
    >>> test_card_deck == [5, JOKER_1, 3, JOKER_2, 1]
    True

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, JOKER_2, 3, JOKER_1, 5]
    >>> triple_cut(test_card_deck)
    >>> test_card_deck == [5, JOKER_2, 3, JOKER_1, 1]
    True
    '''
    # Obtain the index-positions of Joker Card 1 and Joker Card 2
    joker_card_positions = [
        card_deck.index(JOKER_1),
        card_deck.index(JOKER_2)]
    # Sort the list to know which Joker Card has higher precidence in the card
    # deck
    joker_card_positions.sort()
    # Place the index-positions of the Joker Cards in their respected variables
    (FIRST_JOKER_CARD, LAST_JOKER_CARD) = (
        joker_card_positions[0], joker_card_positions[1])
    # Perform Splice 1: The group of cards preceeding the lowest
    # index-positioned Joker Card
    splice_1 = card_deck[:FIRST_JOKER_CARD]
    # Perform Splice 2: The group of cards proceeding the highest
    # index-positioned Joker Card
    splice_2 = card_deck[LAST_JOKER_CARD + 1:]
    # Perform Splice 3: The group of cards between both Joker Cards
    # (including said Joker Cards)
    splice_3 = card_deck[
        FIRST_JOKER_CARD: LAST_JOKER_CARD + 1]
    # Combine the 3 splices together appropriately to form the new card deck
    triple_cutted_deck = splice_2 + splice_3 + splice_1
    # Clear the contents of the given card deck...
    card_deck.clear()
    # And extend our altered list to the original list variable, thereby
    # forcing list mutation
    card_deck.extend(triple_cutted_deck)


# STEP FOUR OF CUSTOM STREAM CIPHER ALGORITHM
def insert_top_to_bottom(card_deck):
    '''(list of int) -> NoneType
    Given a card_deck: Mutates the card_deck list to force a specific group
    amount of cards from the beginning of the list to preceed the
    last card in said list. The number of cards to be transferred is
    determined by the last card's integer value in the list.

    Note: If the last card's integer value is equal to 28 (Joker Card 2), the
    number of cards to be transferred will instead be 27 (Joker Card 1).

    REQ: len(card_deck) = largest card value in list
    REQ: card_deck elements contain no duplicate cards
    REQ: card_deck lowest card value = 1
    REQ: card_deck elements (Joker Card 1 = 27), (Joker Card 2 = 28)
         required to be within list

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    ... 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_1, JOKER_2]
    >>> insert_top_to_bottom(test_card_deck)
    >>> test_card_deck == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    ... 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_1, JOKER_2]
    True

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    ... 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_2, JOKER_1]
    >>> insert_top_to_bottom(test_card_deck)
    >>> test_card_deck == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    ... 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_2, JOKER_1]
    True

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    ... 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_1, JOKER_2, 1]
    >>> insert_top_to_bottom(test_card_deck)
    >>> test_card_deck == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    ... 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_1, JOKER_2, 2, 1]
    True

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15,
    ... 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_1, JOKER_2, 14]
    >>> insert_top_to_bottom(test_card_deck)
    >>> test_card_deck == [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_1,
    ... JOKER_2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14]
    True
    '''
    # Obtain the last card's integer value in the list
    num_of_cards_to_transfer = card_deck[-1]
    # If the last card's integer value is equal to 28
    if (num_of_cards_to_transfer == JOKER_2):
        # Set the value to 27 instead
        num_of_cards_to_transfer = JOKER_1
    # Perform Splice 1: The group of cards starting from the beginning of
    # the list (specified by the the last card's integer value)
    splice_1 = card_deck[: num_of_cards_to_transfer]
    # Perform Splice 2: The group of cards after Splice 1, up to the second
    # last card in the list
    splice_2 = card_deck[num_of_cards_to_transfer: -1]
    # Perform Splice 3: Retrive the last card in the list
    splice_3 = [card_deck[-1]]
    # Combine the 3 splices together appropriately to form the new card deck
    transferred_card_deck = splice_2 + splice_1 + splice_3
    # Clear the contents of the given card deck...
    card_deck.clear()
    # And extend our altered list to the original list variable, thereby
    # forcing list mutation
    card_deck.extend(transferred_card_deck)


# STEP FIVE OF CUSTOM STREAM CIPHER ALGORITHM
def get_card_at_top_index(card_deck):
    '''(list of int) -> int
    Given a card_deck: Returns the value of the card found at a
    specific index-position in the card_deck list. The index-position is
    determined by the first card's integer value in said list.

    Note: If the first card's integer value is equal to 28 (Joker Card 2), the
    index-position number will instead be 27 (Joker Card 1).

    REQ: len(card_deck) = largest card value in list
    REQ: card_deck elements contain no duplicate cards
    REQ: card_deck lowest card value = 1
    REQ: card_deck elements (Joker Card 1 = 27), (Joker Card 2 = 28)
         required to be within list

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [JOKER_2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    ... 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_1, 1]
    >>> get_card_at_top_index(test_card_deck)
    1

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [JOKER_1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    ... 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 1, JOKER_2]
    >>> get_card_at_top_index(test_card_deck)
    28

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    ... 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_1, JOKER_2]
    >>> get_card_at_top_index(test_card_deck)
    2

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 15,
    ... 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, JOKER_1, JOKER_2]
    >>> get_card_at_top_index(test_card_deck)
    15
    '''
    # Obtain the first card's integer value
    top_card_value = card_deck[0]
    # If the first card's integer value is equal to 28
    if (top_card_value == JOKER_2):
        # Set the value to 27 instead
        top_card_value = JOKER_1
    # Retrieve the card at the index-position number specified by the
    # first card's integer value
    card_at_top_card_value_index = card_deck[top_card_value]
    # Returns the card retrieved from said position
    return card_at_top_card_value_index


# ALL 5 STEPS OF THE CUSTOM STREAM CIPHER ALGORITHM
def get_next_value(card_deck):
    '''(list of int) -> int
    Given a card_deck: Returns a possible valid keystream value generated by
    one complete round of the custom Stream Cipher Algorithm.

    REQ: len(card_deck) = largest card value in list
    REQ: card_deck elements contain no duplicate cards
    REQ: card_deck lowest card value = 1
    REQ: card_deck highest card value = 28
    REQ: card_deck elements (Joker Card 1 = 27), (Joker Card 2 = 28)
         required to be within list

    ===========================================================================
    In this example: The 1st round of the custom Stream Cipher
    Algorithm ends with this list: [15, JOKER_2, 22, 19, 13, 4, 1, 2, 14, 17,
    3, 25, 18, 20, 12, 5, 9, 6, 24, 8, 7, 10, JOKER_1, 26, 23, 16, 21, 11]
    ---> Which produces a valid keystream value of 5
    (15th index-position in the list).
    We keep this value as a result.
    ---------------------------------------------------------------------------
    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [22, 19, 13, 4, 1, 2, 14, 17, 3, 25, 18, 20, 12, 5,
    ... JOKER_1, 11, 26, 23, 16, JOKER_2, 21, 15, 9, 6, 24, 8, 7, 10]
    >>> get_next_value(test_card_deck)
    5

    ===========================================================================
    In this example: The 1st round of the custom Stream Cipher
    Algorithm ends with this list: [19, 14, 7, 13, 26, 16, JOKER_2, 1, 12, 24,
    4, 21, 2, 9, 10, 11, 6, 17, 3, 22, 18, 8, 15, 23, JOKER_1, 25, 20, 5]
    ---> Which produces a valid keystream value of 22
    (19th index-position in the list).
    We keep this value as a result.
    ---------------------------------------------------------------------------
    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 12, 24, 4, 21, 2, 9, 10, 11, 6, 17, 3, 22, 18,
    ... 8, JOKER_1, 5, 25, 20, 19, 14, 7, 13, JOKER_2, 26, 16, 15, 23]
    >>> get_next_value(test_card_deck)
    22

    ===========================================================================
    In this example: The 1st round of the custom Stream Cipher
    Algorithm ends with this list: [6, 5, 19, 23, 17, 10, 8, 7, 12, 25, 9, 11,
    14, 2, 4, JOKER_1, 3, 16, 20, 26, 15, JOKER_2, 13, 1, 24, 21, 22, 18]
    ---> Which produces a valid keystream value of 8
    (6th index-position in the list).
    We keep this value as a result.
    ---------------------------------------------------------------------------
    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [13, 1, 24, 21, 22, 6, 5, 19, 23, 17, 10, 8, 7, 12,
    ... JOKER_1, 18, 3, 16, 20, JOKER_2, 26, 15, 25, 9, 11, 14, 2, 4]
    >>> get_next_value(test_card_deck)
    8
    '''
    # Helper function: Swaps Joker Card 1 and the proceeding card's position
    # in the card deck
    move_joker_1(card_deck)
    # Helper function: Swaps Joker Card 2 and the proceeding card's position in
    # the card deck. This process is repeated TWICE
    move_joker_2(card_deck)
    # Helper function: Performs a Triple-Cut Card Shuffle on the card deck
    triple_cut(card_deck)
    # Helper function: Transfers a group of cards at the beginning of the
    # card deck to reside right before the last card in said card deck
    insert_top_to_bottom(card_deck)
    # Helper function: Based on the value of the first card in the deck;
    # retrieves the value of the card at the index-position of the first
    # card's integer value in said card deck.
    # Therefore, we retrieve a possible valid keystream value generated by
    # the custom Stream Algorithm
    generated_number = get_card_at_top_index(card_deck)
    # Returns a possible valid keystream value
    return generated_number


def get_next_keystream_value(card_deck):
    '''(list of int) -> int
    Given a card_deck: Returns a valid keystream value generated by the custom
    Stream Cipher Algorithm. We run multiple rounds of the Algorithm until
    the value returned by said Algorithm is: |1 <= value returned <= 26|

    REQ: len(card_deck) = largest card value in list
    REQ: card_deck elements contain no duplicate cards
    REQ: card_deck lowest card value = 1
    REQ: card_deck highest card value = 28
    REQ: card_deck elements (Joker Card 1 = 27), (Joker Card 2 = 28)
         required to be within list

    ==========================================================================
    In this example: The 1st round of the custom Stream Cipher
    Algorithm ends with this list: [15, JOKER_2, 22, 19, 13, 4, 1, 2, 14, 17,
    3, 25, 18, 20, 12, 5, 9, 6, 24, 8, 7, 10, JOKER_1, 26, 23, 16, 21, 11]
    ---> Which produces a valid keystream value of 5
    (15th index-position in the list).
    We keep this value as a result.
    --------------------------------------------------------------------------
    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [22, 19, 13, 4, 1, 2, 14, 17, 3, 25, 18, 20, 12, 5,
    ... JOKER_1, 11, 26, 23, 16, JOKER_2, 21, 15, 9, 6, 24, 8, 7, 10]
    >>> get_next_keystream_value(test_card_deck)
    5

    ==========================================================================
    In this example: The 1st round of the custom Stream Cipher
    Algorithm ends with this list: [19, 14, 7, 13, 26, 16, JOKER_2, 1, 12, 24,
    4, 21, 2, 9, 10, 11, 6, 17, 3, 22, 18, 8, 15, 23, JOKER_1, 25, 20, 5]
    ---> Which produces a valid keystream value of 22
    (19th index-position in the list).
    We keep this value as a result.
    --------------------------------------------------------------------------
    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 12, 24, 4, 21, 2, 9, 10, 11, 6, 17, 3, 22, 18,
    ... 8, JOKER_1, 5, 25, 20, 19, 14, 7, 13, JOKER_2, 26, 16, 15, 23]
    >>> get_next_keystream_value(test_card_deck)
    22

    ==========================================================================
    In this example: The 1st round of the custom Stream Cipher
    Algorithm ends with this list: [6, 5, 19, 23, 17, 10, 8, 7, 12, 25, 9, 11,
    14, 2, 4, JOKER_1, 3, 16, 20, 26, 15, JOKER_2, 13, 1, 24, 21, 22, 18]
    ---> Which produces a valid keystream value of 8
    (6th index-position in the list).
    We keep this value as a result.
    --------------------------------------------------------------------------
    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [13, 1, 24, 21, 22, 6, 5, 19, 23, 17, 10, 8, 7, 12,
    ... JOKER_1, 18, 3, 16, 20, JOKER_2, 26, 15, 25, 9, 11, 14, 2, 4]
    >>> get_next_keystream_value(test_card_deck)
    8

    ==========================================================================
    In this example: The 1st round of the custom Stream Cipher
    Algorithm ends with this list: [15, 10, 11, 4, 16, 5, 17, 3, 18, 23, 9, 6,
    7, 1, JOKER_1, JOKER_2, 22, 24, 20, 12, 19, 8, 21, 13, 2, 25, 26, 14]
    ---> Which produces an invalid keystream value of JOKER_2
    (15th index-position in the list).
    We run the algorithm again as a result and end with this list:
    [20, 12, 19, 8, 21, 13, 2, 25, 26, 14, JOKER_1, 22, JOKER_2, 15, 10, 11,
    4, 16, 5, 17, 3, 18, 23, 9, 6, 7, 24, 1]
    ---> Which produces a valid keystream value of 3
    (20th index-position in the list).
    We keep this value as a result.
    --------------------------------------------------------------------------
    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [22, 24, 20, 12, 19, 8, 21, 13, 2, 25, 26, 15, 10, 11,
    ... 4, 16, 5, 17, 3, 18, 23, 9, 6, 7, JOKER_2, JOKER_1, 14, 1]
    >>> get_next_keystream_value(test_card_deck)
    3

    ==========================================================================
    In this example: The 1st round of the custom Stream Cipher
    Algorithm ends with this list: [9, 11, 20, 14, 5, 18, 10, 13, 2, JOKER_1,
    3, 25, 7, 22, 1, 8, 21, 15, 16, 4, 26, 17, 19, 6, JOKER_2, 24, 23, 12]
    ---> Which produces an invalid keystream value of JOKER_1
    (9th index-position in the list).
    We run the algorithm again as a result and end with this list:
    [7, 22, 1, 8, 21, 15, 16, 4, 26, 17, 19, 6, 24, 23, JOKER_2, 9, 11, 20,
    14, 5, 18, 10, 13, 2, 12, JOKER_1, 25, 3]
    ---> Which produces a valid keystream value of 4
    (7th index-position in the list).
    We keep this value as a result.
    --------------------------------------------------------------------------
    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [3, 25, 7, 22, JOKER_2, 1, 12, 24, 23, 9, 11, 20, 14,
    ... 5, 18, 10, 13, JOKER_1, 2, 8, 21, 15, 16, 4, 26, 17, 19, 6]
    >>> get_next_keystream_value(test_card_deck)
    4
    '''
    # Holds the valid keystream value
    valid_keystream_value = 0
    # Exit when a valid keystream value has be recovered
    is_valid_keystream_value = False
    # Go through rounds of the custom Stream Algorithm
    while (not is_valid_keystream_value):
        # Helper function: Retrieves a possible valid keystream value
        valid_keystream_value = get_next_value(card_deck)
        # If we recovered a valid keystream value
        if (valid_keystream_value in range(1, 27)):
            # Exit loop
            is_valid_keystream_value = True
    # Returns the generated valid keystream value
    return valid_keystream_value


def process_message(card_deck, one_line_message, mode):
    '''(list of int, str, str) -> str
    Given a card_deck; a one_line_message; and a desired mode of operation:
    Returns either an encrypted or decrypted version of one_line_message
    depending on what mode was specified. The process will be based off of
    a custom Stream Cipher Algorithm.

    REQ: len(card_deck) = largest card value in list
    REQ: card_deck elements contain no duplicate cards
    REQ: card_deck lowest card value = 1
    REQ: card_deck highest card value = 28
    REQ: card_deck elements (Joker Card 1 = 27), (Joker Card 2 = 28)
         required to be within list
    REQ: mode restricted to the following elements:
        |'e' ---> To encrypt one_line_message|
        |'d' ---> To decrypt one_line_message|

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "Welcome to CSCA08"
    >>> test_mode = 'e'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'HNIJYLPEVKBNL'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "HNIJYLPEVKBNL"
    >>> test_mode = 'd'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'WELCOMETOCSCA'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "THISLOOKSLIKEAJOBFORTHEDEBUGGER"
    >>> test_mode = 'e'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'EQFZVNZVZTRVPAHTKZFJCXXANYSASXQ'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "EQFZVNZVZTRVPAHTKZFJCXXANYSASXQ"
    >>> test_mode = 'd'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'THISLOOKSLIKEAJOBFORTHEDEBUGGER'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "HOUSTONWEHAVEAPROBLEM"
    >>> test_mode = 'e'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'SXRZDNYHLPJGPANWXVCWV'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "SXRZDNYHLPJGPANWXVCWV"
    >>> test_mode = 'd'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'HOUSTONWEHAVEAPROBLEM'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "WINTERISCOMING"
    >>> test_mode = 'e'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'HRKAOQTDJWVTYG'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "HRKAOQTDJWVTYG"
    >>> test_mode = 'd'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'WINTERISCOMING'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "THECAKEISALIE "
    >>> test_mode = 'e'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'EQBJKJPTZIUTP'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "EQBJKJPTZIUTP "
    >>> test_mode = 'd'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'THECAKEISALIE'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "DOABARRELROLL"
    >>> test_mode = 'e'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'OXXIKQCPSZXWW'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "OXXIKQCPSZXWW"
    >>> test_mode = 'd'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'DOABARRELROLL'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "PEACE"
    >>> test_mode = 'e'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'ANXJO'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "ANXJO"
    >>> test_mode = 'd'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'PEACE'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "GOODLUCK!"
    >>> test_mode = 'e'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'RXLKVTNV'

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_one_line_message = "RXLKVTNV!"
    >>> test_mode = 'd'
    >>> process_message(test_card_deck, test_one_line_message, test_mode)
    'GOODLUCK'
    '''
    # Holds the Helper function that will be used based on selected mode
    helper_function = None
    # Holds either the encrypted or decrypted message
    processed_message = str()
    # If it was specified to encrypt the message
    if (mode == 'e'):
        # Helper function |encrypt_letter| will be used
        helper_function = encrypt_letter
    # Else, we must have been specified to decrypt the message
    else:
        # Therefore, Helper function |decrypt_letter| will be used
        helper_function = decrypt_letter
    # Helper function: Remove all non-alphabetical characters from the given
    # message
    formatted_message = clean_message(one_line_message)
    # Go through each letter in the formatted plaintext
    for letter in formatted_message:
        # Retrieve a valid keystream value for encryption or decryption
        keystream_value = get_next_keystream_value(card_deck)
        # Enact the proper Helper function to either produce an encrypted
        # or decrypted letter...
        processed_letter = helper_function(letter, keystream_value)
        # And add said letter to the message that we are creating
        processed_message += processed_letter
    # Return either an encrypted or decrypted message, based on the
    # specified mode
    return processed_message


def process_messages(card_deck, multi_line_message, mode):
    '''(list of int, list of str, str) -> list of str
    Given a card_deck; a multi_line_message; and a desired mode of operation:
    Returns either an encrypted or decrypted version of all messages in
    multi_line_message depending on what mode was specified. The process will
    be based off of a custom Stream Cipher Algorithm.

    REQ: len(card_deck) = largest card value in list
    REQ: card_deck elements contain no duplicate cards
    REQ: card_deck lowest card value = 1
    REQ: card_deck highest card value = 28
    REQ: card_deck elements (Joker Card 1 = 27), (Joker Card 2 = 28)
         required to be within list
    REQ: mode restricted to the following elements:
        |'e' ---> To encrypt all messages in multi_line_message|
        |'d' ---> To decrypt all messages in multi_line_message|

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_multi_line_message = [
    ... "IFOUNDSOMEMONEYINTHESTREETANDIBOUGHTTWOBARSOFCHOCOLATE",
    ... "ANDTHESECONDONEHADTHEGOLDENTICKET",
    ... "ANDTHEREWERECROWDSOFPEOPLEALLAROUNDMEWANTINGTOSEEIT",
    ... "ANDTHESHOPKEEPERRESCUEDME",
    ... "ANDIRANALLTHEWAYHOMEANDHEREIAM"
    ... ]
    >>> test_mode = 'e'
    >>> process_messages(test_card_deck, test_multi_line_message, test_mode)
    ['TOLBXCDZTMVZYEWNWNYWBJKBNQYHPBAOKYJHAUGNMSXELEJKULXKLE\
', 'CDMARWJNUZPBAIUSKSWYIZDOLYLJHSVGP\
', 'VPZSRVAPSYQHKZZDTTKIJYGZFVXBPBCEBVGAXXJSKLQIELQRWKI\
', 'HDOEDDWJYYSUSXWPDAYAKQTGJ', 'UMXDUTDTKZGFRVMKICXURZPUKUOQFK']

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_multi_line_message = [
    ... "TOLBXCDZTMVZYEWNWNYWBJKBNQYHPBAOKYJHAUGNMSXELEJKULXKLE",
    ... "CDMARWJNUZPBAIUSKSWYIZDOLYLJHSVGP",
    ... "VPZSRVAPSYQHKZZDTTKIJYGZFVXBPBCEBVGAXXJSKLQIELQRWKI",
    ... "HDOEDDWJYYSUSXWPDAYAKQTGJ",
    ... "UMXDUTDTKZGFRVMKICXURZPUKUOQFK"
    ... ]
    >>> test_mode = 'd'
    >>> process_messages(test_card_deck, test_multi_line_message, test_mode)
    ['IFOUNDSOMEMONEYINTHESTREETANDIBOUGHTTWOBARSOFCHOCOLATE\
', 'ANDTHESECONDONEHADTHEGOLDENTICKET\
', 'ANDTHEREWERECROWDSOFPEOPLEALLAROUNDMEWANTINGTOSEEIT\
', 'ANDTHESHOPKEEPERRESCUEDME', 'ANDIRANALLTHEWAYHOMEANDHEREIAM']

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_multi_line_message = [
    ... "PRAISELIKEGOLDDIAMONDSOWESITSVALUETOITSSCARCITY",
    ... "INTEGRITYWITHOUTKNOWLEDGEISWEAKANDUSELESSANDKNOWLEDGEWITHOUT\
    ... INTEGRITYISDANGEROUSANDDREADFUL", "FEWTHINGSARESOLIBERALLYBESTOWED\
    ... ORSQUANDEREDWITHSOLITTLEEFFECTASGOODADVICE", "EVILISUNCERTAININTHE\
    ... SAMEDEGREEASGOODANDFORTHEREASONTHATWEOUGHTNOTTOHOPETOOSECURELYWEOUGHT\
    ... NOTTOFEARWITHTOOMUCHDEJECTION"
    ... ]
    >>> test_mode = 'e'
    >>> process_messages(test_card_deck, test_multi_line_message, test_mode)
    ['AAXPCDWTRMPZWDBNJGFFMIHTNPGNEOZLKWVCPRKEOBWSOVA\
', 'EFQQQJIVOFPDZFDLVPMIGUOQTLJAXPNIHBKRUWGONCJCUEXHHYCJMETAXPQWCHLOAIFJCJD\
THVJSKPDXRQGFCBYQXWA', 'MUHEDHRICJZUGWDGNAXYBXOVJMSIRHWEKREHYACQDFRHYKTEBRL\
DBQCERVAGLQSFOEXKRUJKQ', 'EQUVNSCWHFSCFDNPOUAFJRPMRNMSPUMCAJJTWDEYAXHGYMLOY\
CFTRWGPXNISJMXCPEEVHGXOKRXNJUUVJODQGUZMRKNEOJORZRSFJJGRHZQXXBKVQHWKVG']

    >>> JOKER_1 = 27
    >>> JOKER_2 = 28
    >>> test_card_deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER_2, 3, 6, 9,
    ... 12, 15, 18, 21, 24, JOKER_1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> test_multi_line_message = [
    ... "AAXPCDWTRMPZWDBNJGFFMIHTNPGNEOZLKWVCPRKEOBWSOVA",
    ... "EFQQQJIVOFPDZFDLVPMIGUOQTLJAXPNIHBKRUWGONCJCUEXHHYCJMETAXPQWCHLOAIFJC\
    ... JDTHVJSKPDXRQGFCBYQXWA", "MUHEDHRICJZUGWDGNAXYBXOVJMSIRHWEKREHYACQDFRH\
    ... YKTEBRLDBQCERVAGLQSFOEXKRUJKQ", "EQUVNSCWHFSCFDNPOUAFJRPMRNMSPUMCAJJTW\
    ... DEYAXHGYMLOYCFTRWGPXNISJMXCPEEVHGXOKRXNJUUVJODQGUZMRKNEOJORZRSFJJGRHZQ\
    ... XXBKVQHWKVG"
    ... ]
    >>> test_mode = 'd'
    >>> process_messages(test_card_deck, test_multi_line_message, test_mode)
    ['PRAISELIKEGOLDDIAMONDSOWESITSVALUETOITSSCARCITY',\
 'INTEGRITYWITHOUTKNOWLEDGEISWEAKANDUSELESSANDKNOWLEDGEWITHOUTINTEGRITYIS\
DANGEROUSANDDREADFUL', 'FEWTHINGSARESOLIBERALLYBESTOWEDORSQUANDEREDWITHS\
OLITTLEEFFECTASGOODADVICE', 'EVILISUNCERTAININTHESAMEDEGREEASGOODANDFORT\
HEREASONTHATWEOUGHTNOTTOHOPETOOSECURELYWEOUGHTNOTTOFEARWITHTOOMUCHDEJECT\
ION']
    '''
    # Holds either the encrypted or decrypted messages
    list_of_messages = list()
    # Go through each message in the list of messages
    for message in multi_line_message:
        # Helper function: Retrive either the encrypted or decrypted message
        processed_message = process_message(card_deck, message, mode)
        # Then append it to our list of completed messages
        list_of_messages.append(processed_message)
    # Returns either a list of encrypted or decrypted messages, based on the
    # specified mode
    return list_of_messages


def read_messages(message_file_handle):
    '''(io.TextIOWrapper in read mode) -> list of str
    Given a message_file_handle: Returns a list containing every line found
    in the file, having the whitespace surrounding each line stripped.

    REQ: None
    '''
    # List comprehension: Retrieve each line from the file, with said line
    # stripped of bordering whitespace
    formatted_messages = [
        line.strip() for line in message_file_handle.readlines()]
    # Returns the retrieved messages formatted with no bordering whitespace
    return formatted_messages


def read_deck(card_deck_file_handle):
    '''(io.TextIOWrapper in read mode) -> list of int
    Given a card_deck_file_handle: Returns a list containing every integer
    found in the file.

    The following refers the 'contents' of the card_deck_file_handle:
    REQ: content amount of card elements = largest card value in file
    REQ: content elements contain no duplicate cards
    REQ: content lowest card value = 1
    REQ: content highest card value = 28
    REQ: content elements (Joker Card 1 = 27), (Joker Card 2 = 28)
         required to be within file
    '''
    # Helper function: Retrieve the lines of the card deck file formatted with
    # no bordering whitespace
    formatted_deck = read_messages(card_deck_file_handle)
    # Join the lines back together into one string
    formatted_deck = ' '.join(formatted_deck)
    # Then split them to remove all interspaced whitespace
    formatted_deck = formatted_deck.split()
    # List comprehension: Retrieve the cards within the card deck converted
    # to data type integer
    cards_in_deck = [
        int(card) for card in formatted_deck]
    # Returns the list of integers (cards of the card deck)
    return cards_in_deck
