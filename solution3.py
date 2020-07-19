  
import sys

codes = {}

#determining different frequencies of the characters
def frequency (data):
    char_freq = {}#dictionary to store frequencies
    for char in data:
        char_freq[char] = char_freq.get(char,0) + 1
        #print(char_freq)
    return char_freq

#building and sorting list of tuples in increasing order of frequencies
def sort_freq (char_freq):
    characters = char_freq.keys()
    freq_tuples = []#list of tupels
    for char in characters:
        freq_tuples.append((char_freq[char],char))
    freq_tuples.sort()
    return freq_tuples

#building huffman tree
def huffman_tree(freq_tuples):
    if len(freq_tuples) == 1:
        return freq_tuples
    else:
        while len(freq_tuples) > 1:
            two_lowest_freq = tuple(freq_tuples[0:2])                  #two least frequencies
            freq_left  = freq_tuples[2:]                          #other freq except the least two
            sum_of_least_two = two_lowest_freq[0][0] + two_lowest_freq[1][0]     #sum of least two
            freq_tuples   = freq_left + [(sum_of_least_two,two_lowest_freq)]     # adding sum back to the frequency tuple
            freq_tuples.sort(key = lambda x: x[0])                                  #sorting the frequencies
        return freq_tuples[0]            # Return the single huffman tree from the list of tuples

#trimming the huffman tree
def trim_tree (tree):
    if len(tree) == 1:
        freq_count=tree[0][1]
        #print("returning tree[0][1]")
        #print(freq_count)
        return freq_count
    else:   
        #removing freq from previously built tree
        freq_count = tree[1]    
        if type(freq_count) is str:#the noded is a leaf so return it
            #print(freq_count)
            return freq_count   
        else:
            return (trim_tree(freq_count[0]), trim_tree(freq_count[1])) # trimming left child then right child, then recombining it

#assigning binary codes
def assign_bin_codes (node, binary_str=""):
    global codes
    
    if type(node) is str:
        codes[node] = binary_str #the node is a leaf node
        #print(codes[node])
    else:                              #intermediate node
        assign_bin_codes(node[0], binary_str+"0")    # assign value to left subtree
        assign_bin_codes(node[1], binary_str+"1")    # assign value to right subtree

#encoding data
def huffman_encoding(data):
    global codes
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]
    return encoded_data

#decoding data
def huffman_decoding(data,tree):
    decoded_data = ""
    encoded_tree = tree
    for bit in data :
        if bit == '0':
            encoded_tree = encoded_tree[0]  #left subtree (0 means left)
        else:
            encoded_tree = encoded_tree[1]  #right subtree(1 means right)
        if type(encoded_tree) is str:
            decoded_data += encoded_tree    #leaf is reached so a character is found, so added to the output
            encoded_tree = tree             # go to the base and restart for next character
    return decoded_data



    
def main():
    #test case 1
    a_great_sent = "This is Awesome"

    if not a_great_sent:
        print("enter a non-empty string")
    else:
        char_freq = frequency(a_great_sent)
        freq_tuples = sort_freq(char_freq)

        tree = huffman_tree(freq_tuples)

        tree = trim_tree(tree)

        if len(tree) == 1:
            codes[tree]="0"
         
        else:
            assign_bin_codes(tree)
    

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sent)))
        print ("The content of the data is: {}\n".format(a_great_sent))

        encoded_data = huffman_encoding(a_great_sent)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))


    #test case2
    print(" ")
    a_great_sent = "you are awesome"

    if not a_great_sent:
        print("enter a non-empty string")
    else:
        char_freq = frequency(a_great_sent)
        freq_tuples = sort_freq(char_freq)

        tree = huffman_tree(freq_tuples)

        tree = trim_tree(tree)
    
        if len(tree) == 1:
            codes[tree]="0"
         
        else:
            assign_bin_codes(tree)

    

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sent)))
        print ("The content of the data is: {}\n".format(a_great_sent))

        encoded_data = huffman_encoding(a_great_sent)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))


    #test case3
    print(" ")
    a_great_sentence = "nnnnnnnnnnnnnnnn"

    if not a_great_sent:
        print("enter a non-empty string")
    else:
        char_freq = frequency(a_great_sentence)
        freq_tuples = sort_freq(char_freq)

        tree = huffman_tree(freq_tuples)

        tree = trim_tree(tree)

        if len(tree) == 1:
            codes[tree]="0"
         
        else:
            assign_bin_codes(tree)
    

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sent)))
        print ("The content of the data is: {}\n".format(a_great_sent))

        encoded_data = huffman_encoding(a_great_sent)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
    
   
    #test case 4
    print(" ")
    a_great_sent = ""

    if not a_great_sentence:
        print("enter a non-empty string")
    else:
        char_freq = frequency(a_great_sent)
        freq_tuples = sort_freq(char_freq)

        tree = huffman_tree(freq_tuples)

        tree = trim_tree(tree)

        if len(tree) == 1:
            codes[tree]="0"
         
        else:
            assign_bin_codes(tree)
    

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sent)))
        print ("The content of the data is: {}\n".format(a_great_sent))

        encoded_data = huffman_encoding(a_great_sent)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

        #answer
        #enter a non-empty string
    

if __name__ == "__main__":
    main()
        
