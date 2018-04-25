"""more practice with data structures
Brooke
4/25/18
"""

from itertools import count

def count_empty_lines(source):
    """
    counts empty lines in text file named source
    source - string has namee of the text the text
    the textfile
    returns: int
    """
    num_lines = 0 # counts empty lines
    fin = open(source)

    for line in fin:
        if line == '\n':
            num_lines = num_lines + 1
    src.close()
    return num_lines



    """counter = source()
    with open(afile.txt, 'r') as f:
        for line in f.readlines():
            if not line.strip():
                source.next
        return source """

def count_at_start(word, source):
    """
    counts occurences of word at the start of lines
    in a file source
    """

    count = 0
    fin = open(source, 'r')
    for line in fin:
        list_of_words = line.split()
        if list_of_words:
            if word ==list_of_words(0):
                count = count + 1
    fin.close()
    return count

    """count = 0
    for word in source:
        if firstchar(word) == word:
            count = count + 1
    return count """

def split_fname(source):
    """
    puts a ',' between words in the file
    """

    file = with open(“testfile.txt”,”w”)
    file.write(“Hello World”)
    
    x = source.split(',')
    for word in source:
        print word
