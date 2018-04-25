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
            if word ==list_of_words[0]:
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

    file = open('testfile.txt','w')
    file.write('Hello World')

    x = source.split(',')
    for word in source:
        print(word)

def count_at_end(word, source):
    """
    counts lines with word at the
    end of each line in the file
    source.
    word- str
    source: string - name of the file"""
    count = 0
    fin = open(source)
    for line in fin:
        list_of_words = line.split()
        if list_of_words:
            if list_of_words[-1] == word:
                count += 1
    return count

def letter_count(source, letter_list):
    """counts how many times letters from
    letter_list appear in file source
    source: stri -name of file
    letter_list: list of characters"""



def remove_word_from_file(word, source,target):
    """counts occurences of word at the start
    of the line and remove word from the file
    word: string - to be counted and removed
    source: string - name of input file
    target: string - name of output afile
    returns: int - number of removed words"""

    count = 0
    fin = open(source)
    fout = open(target, 'w')
    for line in fin:
        if line.startswith(word):
            count += 1
            new_line = line.replace(word, '')
        else:
            fout.write(new_line)

    fin.close()
    fout.close()
    return count
