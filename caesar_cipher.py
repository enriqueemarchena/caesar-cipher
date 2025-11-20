import string
import os
from typing import Tuple, Optional

"""Simple Caesar cipher algorithm with encode/decode functions."""

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "common.txt")

alphabet: str = string.ascii_lowercase
words = {w.strip() for w in open(file_path, encoding="utf-8")}

def cypher(text: str, number: int) -> str:
    """Encode text with a simple Caesar algorithm step.

    Input:
        text: The lowercase string.
        number: How many positions to move each letter.
    Output:
        The encoded string.
    """
    new_text = ""
    for letter in text:
        if letter in alphabet:
            new_text += alphabet[(alphabet.index(letter) + number) % 26]
        else:
            new_text += letter
    return new_text


def decypher(text: str) -> Tuple[Optional[str], Optional[int]]:
    """Try all algorithm steps to decode the text.

    Input:
        text: The encoded string.
    Output:
        Decoded text and the algorithm step used, or (None, None).
    """
    for number in range(26):
        decyphered_sample = cypher(text, -number)
        if sum(1 for word in decyphered_sample.split() if word in words) > 2:
            return decyphered_sample, number
    return None, None


choice: str = input("Cypher or decypher? ").lower()
raw_text: str = input("Write the text: ").lower()

if choice == "cypher":
    cypher_number: int = int(input("Cyphing number: "))
    print(cypher(raw_text, cypher_number))
else:
    decyphered_text, decypher_number = decypher(raw_text)
    print(decyphered_text, decypher_number)
