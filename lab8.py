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

    for line in fin: #iterate through each line in fin
        # increment num_lines
    fin.close()
    #modify statement below to return reduce result
    return 0
