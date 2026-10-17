
def reverse_from_center(word):
    """
    Given a string, return the string reversed from the center, both ways.
    If there is an odd number of characters, reverse from either side of the center character.
    """

    half_a = word[len(word) // 2 :: -1]
    half_b = word[len(word) : len(word) // 2 : -1]
    # print(half_a or None, half_b or None)
    # print(half_a + half_b)
    # FIXING
    return half_a+half_b

def main():
    print('reverse_from_center("hello"):', reverse_from_center("hello"))
    print('reverse_from_center("syntax"):', reverse_from_center("syntax"))
    print('reverse_from_center("paradoxical"):', reverse_from_center("paradoxical"))

if __name__ == "__main__":
    main()