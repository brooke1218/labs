def file2list(fname):
    """
        Transverses an input text file called fname and creates a list of lines in the file.
        fname: string - file name of the input text file
        Returns: list of lines in the input file
        """

    fin = open(fname, 'r')
        #use fin = open(fname, 'r', encoding = 'utf8') if you get encoding errors

    t = []

        # each time through the loop variable lines
        # gets the next line in the file2list

    for line in fin:
        line = line.strip()
        t.append(line)
        fin.close()
    return t

def count_lines(fname):
    """
    Counts the number of lines in a fname input text file.
    fname: string -file name of the input text file
    Returns: integer - number of lines in the input text file
    """
    fin = open(fname, 'r') # create file object fin for reading
    # define and initialize local variable num_lines to store result
    num_line = []

    for line in fin: #iterate through each line in fin
        # increment num_lines
        num_line = num_line+1
        pass
    fin.close()
    #modify statement below to return reduce result
    return 0

def count_word(word, fname):
    """
    Counts the number of times word appears in fname input text file
    word: string - desired word to count
    fname: string file name
    Returns: integer -number of times word appears in the input text file
    """

    #create file object fin for reading
    fin = open(fname, 'r')
    # create local variable nu,_words in which we count the occurrneces of word in the file
    num_words = 0

    for line in fin:
        list_of_words = line.split()

        if word in list_of_words:
            num_words= num_words +1 

    fin.close()
    return num_words
