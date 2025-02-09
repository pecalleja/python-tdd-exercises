def reverse_list(elements: list[int]) -> list[int]:
    """
    Reverses order of elements in list l.
    """
    return elements[::-1]


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


# ------------------------------------------------------------------------------


def reverse_string(characters: str) -> str:
    """
    Reverses order of characters in string s.
    """
    return characters[::-1]


def test_reverse_string():
    assert reverse_string("foobar") == "raboof"


# ------------------------------------------------------------------------------
english_vowel = ["a", "e", "i", "o", "u", "y"]


def is_english_vowel(character: str) -> bool:
    """
    Returns True if c is an english vowel
    and False otherwise.
    """
    if character.lower() in english_vowel:
        return True
    else:
        return False


def test_is_english_vowel():
    assert is_english_vowel("a")
    assert is_english_vowel("e")
    assert is_english_vowel("i")
    assert is_english_vowel("o")
    assert is_english_vowel("u")
    assert is_english_vowel("y")
    assert is_english_vowel("A")
    assert is_english_vowel("E")
    assert is_english_vowel("I")
    assert is_english_vowel("O")
    assert is_english_vowel("U")
    assert is_english_vowel("Y")
    assert not is_english_vowel("k")
    assert not is_english_vowel("z")
    assert not is_english_vowel("?")


# ------------------------------------------------------------------------------


def count_num_vowels(text: str) -> int:
    """
    Returns the number of vowels in a string s.
    """
    total = 0
    for char in text:
        if char.lower() in english_vowel:
            total += 1
    return total


def test_count_num_vowels():
    sentence = "hey ho let's go"
    assert count_num_vowels(sentence) == 5
    sentence = "HEY ho let's GO"
    assert count_num_vowels(sentence) == 5
    paragraph = """She told me her name was Billie Jean,
                   as she caused a scene
                   Then every head turned with eyes
                   that dreamed of being the one
                   Who will dance on the floor in the round"""
    assert count_num_vowels(paragraph) == 54


# ------------------------------------------------------------------------------


def histogram(integers: list[int]) -> str:
    """
    Converts a list of integers into a simple string histogram.
    """
    histogram_text = ""
    for integer in integers:
        histogram_text += "#" * integer + "\n"

    if histogram_text:
        return histogram_text[:-1]

    return histogram_text


def test_histogram():
    assert histogram([2, 5, 1]) == "##\n#####\n#"

    assert histogram([]) == ""


# ------------------------------------------------------------------------------


def get_word_lengths(text: str) -> list[int]:
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    words = text.split()
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


# ------------------------------------------------------------------------------


def find_longest_word(text: str) -> str:
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    words = text.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def test_find_longest_word():
    text = "Three tomatoes are walking down the street"
    assert find_longest_word(text) == "tomatoes"
    text = "foo foo1 foo2 foo3"
    assert find_longest_word(text) == "foo1"


# ------------------------------------------------------------------------------

dna_bases = {"a": "t", "c": "g", "t": "a", "g": "c"}


def validate_dna(dna: str) -> bool:
    """
    Return True if the DNA string only contains characters
    a, c, t, or g (lower or uppercase). False otherwise.
    """
    for element in dna:
        if element.lower() not in dna_bases:
            return False
    return True


def test_validate_dna():
    assert validate_dna("CCGGAAGAGCTTACTTAGccggaagagcttacttag")
    assert not validate_dna("xCCGGAAGAGCTTACTTAGccggaagagcttacttag")
    assert not validate_dna("CCxGGAAGAGCTTACTTAGccggaagagcttacttag")


# ------------------------------------------------------------------------------


def base_pair(element: str) -> str:
    """
    Return the corresponding character (lowercase)
    of the base pair. If the base is not recognized,
    return 'unknown'.
    """
    return dna_bases.get(element.lower(), "unknown")


def test_base_pair():
    assert base_pair("a") == "t"
    assert base_pair("t") == "a"
    assert base_pair("c") == "g"
    assert base_pair("g") == "c"
    assert base_pair("A") == "t"
    assert base_pair("T") == "a"
    assert base_pair("C") == "g"
    assert base_pair("G") == "c"
    assert base_pair("x") == "unknown"
    assert base_pair("foo") == "unknown"


# ------------------------------------------------------------------------------


def transcribe_dna_to_rna(adn: str) -> str:
    """
    Return string s with each letter T replaced by U.
    Result is always uppercase.
    """
    upper_dna = adn.upper()
    return upper_dna.replace("T", "U")


def test_transcribe_dna_to_rna():
    dna = "CCGGAAGAGCTTACTTAGccggaagagcttacttag"
    assert transcribe_dna_to_rna(dna) == "CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG"


# ------------------------------------------------------------------------------


def get_complement(adn: str) -> str:
    """
    Return the DNA complement in uppercase
    (A -> T, T-> A, C -> G, G-> C).
    """
    adn_complement = ""
    for element in adn:
        adn_complement += dna_bases.get(element.lower()).upper()
    return adn_complement


def test_get_complement():
    assert get_complement("CCGGAAGAGCTTACTTAG") == "GGCCTTCTCGAATGAATC"
    assert get_complement("ccggaagagcttacttag") == "GGCCTTCTCGAATGAATC"


# ------------------------------------------------------------------------------


def get_reverse_complement(adn: str) -> str:
    """
    Return the reverse complement of string s
    (complement reversed in order).
    """
    return get_complement(adn)[::-1]


def test_get_reverse_complement():
    assert get_reverse_complement("CCGGAAGAGCTTACTTAG") == "CTAAGTAAGCTCTTCCGG"
    assert get_reverse_complement("ccggaagagcttacttag") == "CTAAGTAAGCTCTTCCGG"


# ------------------------------------------------------------------------------


def remove_substring(substring: str, string: str) -> str:
    """
    Returns string with all occurrences of substring removed.
    """
    return string.replace(substring, "")


def test_remove_substring():
    assert remove_substring("GAA", "CCGGAAGAGCTTACTTAG") == "CCGGAGCTTACTTAG"
    assert remove_substring("CCG", "CCGGAAGAGCTTACTTAG") == "GAAGAGCTTACTTAG"
    assert remove_substring("TAG", "CCGGAAGAGCTTACTTAG") == "CCGGAAGAGCTTACT"
    assert remove_substring("GAA", "GAAGAAGAA") == ""


# ------------------------------------------------------------------------------


def get_position_indices(triplet: str, dna: str) -> list[int]:
    """
    Returns list of position indices for a specific triplet (3-mer)
    in a DNA sequence. We start counting from 0
    and jump by 3 characters from one position to the next.
    """
    index = 0
    positions = []
    while index <= len(dna):
        if dna[index : index + 3] == triplet:  # noqa
            positions.append(int(index / 3))
        index += 3
    return positions


def test_get_position_indices():
    assert get_position_indices("GAA", "CCGGAAGAGCTTACTTAG") == [1]
    assert get_position_indices("GAA", "CCGGAAGAGCTTACTTAGGAAGAA") == [1, 6, 7]


# ------------------------------------------------------------------------------


def get_3mer_usage_chart(dna: str) -> list[tuple]:
    """
    This routine implements a 'sliding window'
    and extracts all possible consecutive 3-mers.
    It counts how often they appear and returns
    a list of tuples with (name, occurrence).
    The list is alphabetically sorted by the name
    of the 3-mer.
    """
    index = 0
    result = {}
    while index <= len(dna) - 3:
        mers3 = dna[index : index + 3]  # noqa
        result[mers3] = result.get(mers3, 0) + 1
        index += 1
    sorted(result)
    return sorted([(key, value) for key, value in result.items()])


def test_get_3mer_usage_chart():
    result = []
    s = "CCGGAAGAGCTTACTTAGGAAGAA"
    result.append(("AAG", 2))
    result.append(("ACT", 1))
    result.append(("AGA", 2))
    result.append(("AGC", 1))
    result.append(("AGG", 1))
    result.append(("CCG", 1))
    result.append(("CGG", 1))
    result.append(("CTT", 2))
    result.append(("GAA", 3))
    result.append(("GAG", 1))
    result.append(("GCT", 1))
    result.append(("GGA", 2))
    result.append(("TAC", 1))
    result.append(("TAG", 1))
    result.append(("TTA", 2))
    assert get_3mer_usage_chart(s) == result

    s = "CCG"
    result = []  # noqa
    result.append(("CCG", 1))
    assert get_3mer_usage_chart(s) == result

    assert get_3mer_usage_chart("") == []


# ------------------------------------------------------------------------------


def read_column(file_name: str, column_number: int) -> list[float]:
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    elements = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            columns = line.split()
            elements.append(float(columns[column_number - 1]))
    return elements


def test_read_column():

    import tempfile
    import os

    text = """1   0.1  0.001
2   0.2  0.002
3   0.3  0.003
4   0.4  0.004
5   0.5  0.005
6   0.6  0.006"""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, "w") as f:
        f.write(text)

    # and now we pass the file name to the function which will read the column
    assert read_column(file_name, 2) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------


def character_statistics(file_name: str) -> tuple[str, str]:
    """
    Reads text from file file_name, then
    lowercases the text, and then returns
    a tuple (x, y), where x is the most abundant
    and y is the least abundant but present character found.
    Use the isalpha() method to figure out
    whether the character is in the alphabet.
    """
    from collections import Counter

    most_common = ""
    least_common = ""
    with open(file_name, "r") as f:
        data = f.read().replace("\n", "").lower()
        result = Counter(data)
        stats = result.most_common()
        for item in stats:
            if item[0].isalpha():
                most_common = item[0]
                break
        for item in stats[::-1]:
            if item[0].isalpha():
                least_common = item[0]
                break
    return most_common, least_common


def test_character_statistics():

    import tempfile
    import os

    text = """
To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscover'd country from whose bourn
No traveller returns, puzzzles the will
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all;
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry,
And lose the name of action.--Soft you now!
The fair Ophelia! Nymph, in thy orisons
Be all my sins remember'd."""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, "w") as f:
        f.write(text)

    # and now we pass the file name to the function which will get the stats
    (most_abundant, least_abundant) = character_statistics(file_name)
    assert (most_abundant, least_abundant) == ("e", "q")

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------


def pythagorean_triples(number: int) -> list[tuple]:
    """
    Returns list of all unique pythagorean triples
    (a, b, c) where a < b < c <= n.
    """
    result = []
    # loop over all a < b < c <= n
    for c in range(1, number + 1):
        for b in range(1, c):
            for a in range(1, b):
                if a * a + b * b == c * c:
                    result.append((a, b, c))
    return result


# ------------------------------------------------------------------------------


def test_pythagorean_triples():
    assert pythagorean_triples(5) == [(3, 4, 5)]
