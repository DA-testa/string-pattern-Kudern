# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    input_type = input().strip().upper()
    pattern, text = '', ''
    if input_type == 'I':
        pattern = input().strip()
        text = input().strip()
    elif input_type == 'F':
        with open("tests/06") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    positions = []
    p_len = len(pattern)
    t_len = len(text)

    # calculate hash value of pattern and first substring of text of length p_len
    p_hash = sum(ord(pattern[i]) * pow(10, p_len - 1 - i) for i in range(p_len))
    t_hash = sum(ord(text[i]) * pow(10, p_len - 1 - i) for i in range(p_len))

    # slide the pattern over the text and check for hash match
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            positions.append(i)
        if i < t_len - p_len:
            # calculate the hash value of next substring of text using rolling hash
            t_hash = 10 * (t_hash - ord(text[i]) * pow(10, p_len - 1)) + ord(text[i + p_len])

    return positions


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

