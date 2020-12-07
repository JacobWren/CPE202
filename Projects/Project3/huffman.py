import time
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __lt__(self, other):
        # custom order, freq first
        return (self.freq, self.char) < (other.freq, other.char)


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    try:
        file_object = open(filename, "r", newline="")
    except:
        raise FileNotFoundError
    chars = file_object.read()
    file_object.close()

    #with open(filename, "r", newline="") as file_object:
        #chars = file_object.read().replace(' ', '')

    chars_list = list(chars) # create list of chars seperated by a ','
    l = [0] * 256
    for char in chars_list:
        l[ord(char)] += 1
    return l
#print(cnt_freq("file1.txt"))

def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    sorted_nodes = [HuffmanNode(index, freq) for index, freq in enumerate(char_freq)]
    sorted_nodes.sort()  # it knows how to sort based on '__lt__'
    sorted_nodes_clean = [node for node in sorted_nodes if not node.freq == 0] # ignore nodes that with 0 frequency

    while len(sorted_nodes_clean) > 1:
        char_min = min(sorted_nodes_clean[0].char, sorted_nodes_clean[1].char)
        parent_node = HuffmanNode(char_min, sorted_nodes_clean[0].freq + sorted_nodes_clean[1].freq)
        parent_node.left = sorted_nodes_clean.pop(0)
        parent_node.right = sorted_nodes_clean.pop(0)
        sorted_nodes_clean.append(parent_node)
        sorted_nodes_clean.sort()
    return sorted_nodes_clean[0]
#'''
#freqlist = cnt_freq("file2.txt")
#print(freqlist)
#hufftree = create_huff_tree(freqlist)

#create_code(hufftree)

#print(hufftree.freq)
#print(hufftree.char)
#'''




def create_code(root_node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    #if root_node == None:
        #return []
    j = ""
    p = ""
    q = [""] * 256
    return create_code_helper(root_node, j, p, q)

def create_code_helper(current_Node, j, p, q):
    # single node/char case
    #if current_Node.left == None and current_Node.right == None:
        #return q[current_Node.char] = 0
    if current_Node.left == None:
        return ""
    j = j + "0"
    create_code_helper(current_Node.left, j, p, q)
    if not(current_Node.left.left):
        if p != "":
            #q[current_Node.left.char] += p[0] + j[1:]
            q[current_Node.left.char] += j
        else:
            q[current_Node.left.char] += j
    #if current_Node.right == None:
        #return ""
    p = p + "1" # We're movin' right
    j = j[:-1] + p[-1]
    create_code_helper(current_Node.right, j, p, q)
    if not(current_Node.right.right):
        if j != "":
            if len(p) > 1:
                #q[current_Node.right.char] += p[1:] + j[(len(p)-1):-1] + p[0]
                q[current_Node.right.char] += j
            else:
                q[current_Node.right.char] += j[:-1] + p[0]
        #else:
            #q[current_Node.right.char] += p
    return q
#print(create_code(hufftree))

def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    l = ""
    for index, freq in enumerate(freqs):
        if freq != 0:
            l = l + " "
            l = l + str(index)
            l = l + " "
            l = l + str(freq)
    return l[1:]

def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    file_in = open(in_file, "r", newline="")
    chars = file_in.read()
    freqlist = cnt_freq(in_file)
    file_in.close()
    if chars != "":
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
    f = open(out_file, "w", newline = "") # write
    f.write(create_header(freqlist) + "\n")
    bit_string = ""
    if chars != "":
        if codes != "":
            for i in chars:
                bit_string += codes[ord(i)]
    f.write(bit_string)
    f.close()


#self.assertEqual(codes[ord('d')], '1')

#huffman_encode("file2.txt", "out_file.txt")

#print(create_header(freqlist))
#start_time = time.time()
#huffman_encode("zero.txt", "zero_out.txt")
#stop_time = time.time()
#print(stop_time - start_time)
'''
freqlist = cnt_freq("file3.txt")
hufftree = create_huff_tree(freqlist)
codes = create_code(hufftree)
'''
'''
print(codes[ord('T')])
print(codes[ord('h')])
print(codes[ord('i')])
print(codes[ord('s')])
print(codes[ord('a')])
print(codes[ord('n')])
print(codes[ord('e')])
print(codes[ord('x')])
print(codes[ord('m')])
print(codes[ord('p')])
print(codes[ord('l')])
print(codes[ord('o')])
print(codes[ord('f')])
print(codes[ord('u')])
print(codes[ord('t')])
print(codes[ord('w')])
print(codes[ord('.')])
print(codes[ord(' ')])
'''



'''
print(codes[ord('a')])
print(codes[ord('b')])
print(codes[ord('c')])
print(codes[ord('d')])
print(codes[ord(' ')])
'''


def huffman_decode(encoded_file, decode_file):
    '''that reads an encoded text file, encoded_file,
     and writes the decoded text into an output text file, decode_file,
     using the Huffman Tree produced by using the header information.'''
    try:
        file_object = open(encoded_file, "r", newline="")
    except:
        raise FileNotFoundError
    char_freq = file_object.readline().rstrip('\n') # first line
    if len(list(char_freq.split())) == 0:
        write_to = open(decode_file, "w", newline="")
        write_to.write("")
        write_to.close()
        file_object.close()
    elif len(list(char_freq.split())) <= 2:
        char_list = char_freq.split()
        single_char = chr(int(char_list[0])) * int(char_list[1])
        write_to = open(decode_file, "w", newline="")
        write_to.write(single_char)
        write_to.close()
        file_object.close()
    else:
        huffman_tree = create_huff_tree(parse_header(char_freq)) # recreate huffman tree!
        chars = list(file_object.read()) # ignores the header
        file_object.close()
        root_Node = huffman_tree
        decode = ""
        for i in chars:
            if i == '1':
                root_Node = root_Node.right
                if root_Node.left == None and root_Node.right == None:
                    decode += chr(root_Node.char)
                    root_Node = huffman_tree # restart at the root Node!
            elif i == '0':
                root_Node = root_Node.left
                if root_Node.left == None and root_Node.right == None:
                    decode += chr(root_Node.char)
                    root_Node = huffman_tree
        write_to = open(decode_file, "w", newline = "")
        write_to.write(decode)
        write_to.close()


def parse_header(header_string):
    '''takes a string input parameter (the first line of the input file)
     and returns a list of frequencies.'''
    chars_list = header_string.split()  # create list of freq's seperated by a ','
    l = [0] * 256
    for i in range(0, len(chars_list), 2):
        l[int(chars_list[i])] = int(chars_list[i + 1])
    return l

#huffman_decode("spam_out.txt", "spam_test.txt")

#huffman_encode("test.txt", "fv.txt")

freqlist = cnt_freq("fv.txt")
hufftree = create_huff_tree(freqlist)
huffman_encode("test.txt", "g.txt")