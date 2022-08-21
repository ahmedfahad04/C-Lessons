import pprint

sbox = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16

]

inv_sbox = [
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
]


# key expansion should be performed

# key = [
#     [
#         0x73, 0x73, 0x69, 0x72,
#         0x61, 0x68, 0x73, 0x69,
#         0x74, 0x63, 0x62, 0x6e,
#         0x69, 0x6a, 0x6f, 0x67
#     ]
# ]

# key = [
#     [
#         0x0f, 0x47, 0x0c, 0xaf,
#         0x15, 0xd9, 0xb7, 0x7f,
#         0x71, 0xe8, 0xad, 0x67,
#         0xc9, 0x59, 0xd6, 0x98
#     ]
# ]

key = [
    [
        0x54, 0x73, 0x20, 0x67,
        0x68, 0x20, 0x4b, 0x20,
        0x61, 0x6d, 0x75, 0x46,
        0x74, 0x79, 0x6e, 0x75
    ]
]


table = [
    [
        2, 3, 1, 1,
        1, 2, 3, 1,
        1, 1, 2, 3,
        3, 1, 1, 2
    ]
]


d_table = [     # table for decryption
    [
        0xe, 0xb, 0xd, 0x9, 
        0x9, 0xe, 0xb, 0xd,
        0xd, 0x9, 0xe, 0xb,
        0xb, 0xd, 0x9, 0xe
    ]
]


Rcon = (
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
)

# round_key = []

def swap(x, y):
    t = x
    x = y
    y = t

    return x, y


def g(word, round_no):

    # print("\nINSIDE: ", word)

    # rotword   -   circular shift
    for i in range(1, 4):
        a = word[i-1]
        b = word[i]

        word[i-1], word[i] = swap(a, b)

    # print("ROTWORD: ", word)

    # sub-word  -   substitute each value using s-box
    for i in range(4):
        char_value = str(bin(int(format(word[i], '02x'), 16)))[2:]
        char_value = char_value.rjust(8, '0')

        # retrieving the row and col valus from the INPUT MATRIX
        nrow = int(char_value[0:4], 2)
        ncol = int(char_value[4:8], 2)

        # access the following row and col value in S-box
        new_cell_value = hex(sbox[(nrow) * 16 + (ncol)])
        word[i] = new_cell_value

    # print("SUB-WORD: ", word)

    # xor   -   xor with the round constant
    for row in range(4):
        # print("RCON: ",  Rcon[row*10+round_no])
        word[row] = hex(int(word[row], 16) ^ Rcon[row*10+round_no])

    return word


def key_expansion():
    round_key = [0]*176
    
    for word_no in range(40):
        # if word_no%4 == 0: print("ROUND:",    (word_no//4)+1)
        
        if word_no%4 == 0:
            for row in range(4):
                for col in range(4):
                        round_key[row*44+col] = (key[0][row*4+col])
                    
            # CONTINUE
            
            x = g([round_key[(r*44+word_no)+3] for r in range(4)], word_no//4)
            # print("SPECTITAL")
            for row in range(4):
                round_key[(row*44+word_no)+4] = int(x[row], 16) ^ round_key[row*44+word_no]
                # print( '[', (row*44+word_no)+4, ']', "=", hex(round_key[(row*44+word_no)+4]), end=', ')
        else:

            for row in range(4):
                round_key[(row*44+word_no)+4] = round_key[row*44+word_no] ^ round_key[(row*44+word_no)+3]
                # print( '[', (row*44+word_no)+4, ']', "=", hex(round_key[(row*44+word_no)+4]), end=', ')
        # print()
        
                        
                
            
    # print("1.")
    # pprint.pprint(round_key)
    # print(len(round_key))
    
    
    # for i in range(176):
    #     print(hex(round_key[i]))
        # if i %3 == 0: print(end=' ')
        # if i%43 == 0 and i > 43: print()
   
    return round_key


def text_to_matrix_conversin(data):

    input_matrix = [[]]
    matrix = []

    letter = 0
    initial_value = 0
    temp = 0
    for i in range(0, len(data), 16):
        for row in range(0, 4, 1):
            cell = []
            inital_value = i    # helps to create the 2nd list of the matrix
            temp = i            # helps to insert element coloumn wise

            for col in range(0, 4, 1):

                if i < len(data):
                    cell.append(hex(ord(data[i])))
                else:
                    cell.append(hex(ord('0')))
                i += 4

                # print('[', row, ']', '[', col, '] = ', chr(int(cell[col],16)))

            matrix.append(cell)
            temp += 1
            i = temp

        input_matrix.append(matrix)
        matrix = []

        i = inital_value

    return input_matrix


def add_round_key(input_matrix, round_no, round_key):

    matrix = []
    final_matrix = [[]]

    letter = 0
    initial_value = 0
    k = 1
    for i in range(0, (len(input_matrix)-1)*16, 16):
        for row in range(0, 4, 1):
            cell = []
            # helps to create the 2nd list of the matrix (repressents a single blocks of 16bits)
            inital_value = i

            for col in range(0, 4, 1):

                value = int(input_matrix[k][row][col][2:], 16) ^ round_key[(col+44*row)+4*round_no]
                # print((int(input_matrix[k][row][col][2:], 16)), "XOR", (round_key[(col+44*row)+4*round_no]), "=", value)
                cell.append(hex(value))
                i += 4

            matrix.append(cell)
            # print()

        final_matrix.append(matrix)
        matrix = []
        k += 1
        i = inital_value
        # print()

    return final_matrix


def substitution_bytes(input_matrix, mode):
    matrix = []
    state_matrix = [[]]

    # calculate the final state matrix
    k = 1
    for i in range(0, (len(input_matrix)-1)*16, 16):
        for row in range(0, 4, 1):
            cell = []
            inital_value = i    # helps to create the 2nd list of the matrix
            temp = i            # helps to insert element coloumn wise

            for col in range(0, 4, 1):

                cell_value = input_matrix[k][row][col]

                char_value = str(bin(int(cell_value, 16)))[2:]
                char_value = char_value.rjust(8, '0')

                # retrieving the row and col valus from the INPUT MATRIX
                nrow = int(char_value[0:4], 2)

                ncol = int(char_value[4:8], 2)

                # access the following row and col value in S-box
                if mode == 'e':
                    new_cell_value = hex(sbox[(nrow) * 16 + (ncol)])
                else:
                    new_cell_value = hex(inv_sbox[(nrow) * 16 + (ncol)])
                    
                # now adding the calculated value in state matrix, this is the 1st list
                cell.append(new_cell_value)

                i += 4

            # this is 2nd list
            matrix.append(cell)
            temp += 1
            i = temp

        # this is the 3rd and final list
        state_matrix.append(matrix)
        matrix = []
        i = inital_value
        k += 1

    return state_matrix


def shift_rows(state_matrix, mode):

    for i in range(1, len(state_matrix)):
        for row in range(0, 4, 1):
            for col in range(0, 3, 1):

                if (row == 1 and mode == 'e') or (row == 3 and mode == 'd'): 
                    a = state_matrix[i][row][col]
                    b = state_matrix[i][row][col+1]
                    state_matrix[i][row][col], state_matrix[i][row][col +1] = swap(a, b)

                elif row == 2 and col < 2:
                    a = state_matrix[i][row][col]
                    b = state_matrix[i][row][col+2]
                    state_matrix[i][row][col], state_matrix[i][row][col +2] = swap(a, b)

                elif (row == 3 and mode == 'e') or (row == 1 and mode == 'd'):
                    a = state_matrix[i][row][col]
                    b = state_matrix[i][row][3]
                    state_matrix[i][row][col], state_matrix[i][row][3] = swap(a, b)

    return state_matrix


def threesMul(value):
        
    # print(value, type(format(0x2f, '02x')))
    value = towsMul(value) ^ value
    # print(int(format(towsMul, '02x'),16), '^' ,int(format(0x2f, '02x'),16), '=', value)
    
    return value


def towsMul(value):
    
    if value & 128:        # if the most significant bit is 1
        value = ((value << 1) ^ 0x1b) & 0xff    # check the size if 8 bit or not. if longer then & with ff with reduce the length to 8 bit
    else:
        value = value << 1
        
    return value 


def eMul(value):
    # mulitplication by 14
    return  towsMul((towsMul((towsMul(value) ^ value)) ^ value))


def dMul(value):
    # multiplication by 13
    return towsMul(towsMul(towsMul(value) ^ value)) ^ value 


def bMul(value):
    # multiplication by 11
    return towsMul((towsMul(towsMul(value)) ^ value)) ^ value


def ninesMul(value):
    #multiplication by 9    
    return towsMul(towsMul(towsMul(value))) ^ value


def calculate_mix_col_value(matrix, r, c, mode):
    
    ans = list()
    for i in range(4):

        # ERROR: "unsupported format string passed to list.__format_" ==> means a is returning a list so we changed to matrix[1][i][c]
        a = matrix[i][c]
        a = int(a, 16)
        # print(a, "-------", type(a))
        
        if mode == 'e': 
            b = table[0][r*4+i]
        else: 
            b = d_table[0][r*4+i]
            
        
        if b == 2:
            temp = towsMul(a)
            
        elif b == 3:
            temp = threesMul(a)
            
        elif b == 9:
            temp = ninesMul(a)
            
        elif b == 0xb:
            temp = bMul(a)
            
        elif b == 0xd:
            temp = dMul(a)
            
        elif b == 0xe:
            temp = eMul(a)
                        
        else:
            temp = a
            
        # print(temp, "-", type(temp))

        ans.append(temp)
        
    result = ans[0]^ans[1]^ans[2]^ans[3] 

    return hex(result)

# TODO: matrix to text converter, refactor code and fix bugs of executing multiple blocks

def mix_column(matrix, mode):

    final_matrix = [[]]

    for i in range(1, len(matrix)):
        temp_matrix = []
        
        for row in range(4):
            # print("ROW...", row)
            cell = []

            for col in range(4):
                # print("COL..", col)
                cell_value = calculate_mix_col_value(matrix[i], row, col, mode)
                cell.append(cell_value)
                # print(cell_value, end=' ')
            temp_matrix.append(cell)
            # print(temp_matrix)
            # print()
        final_matrix.append(temp_matrix)
        # print()

    return final_matrix


def encryption():
    
    # list/array initialization
    st_matrix = [[]]
    initial_matrix = [[]]
    round_key = key_expansion()
    

    # plain text input
    # text = "Thats my kung Fu"
    # text = "Two One Nine Two Three"
    text = "Two One Nine Two Sifat"
    print("\nDATA: ", text, end='\n\n')

    # hex version of plain text
    initial_matrix = text_to_matrix_conversin(text)
    print("INITIAL MATRIX....")
    pprint.pprint(initial_matrix)
    
    # add round key with round no 0
    st_matrix = add_round_key(initial_matrix,0,round_key)
    print("\nADD ROUND KEY....")
    pprint.pprint(st_matrix)
    
    for i in range(1, 10):
        
        print("ROUND#", i)
        # substitution bytes with round no N
        st_matrix = substitution_bytes(st_matrix, 'e')
        print("\nSUBSTITUTION BYTES....")
        pprint.pprint(st_matrix)

        # shift rows with round no N
        st_matrix = shift_rows(st_matrix, 'e')
        print("\nSHIFT ROWS....")
        pprint.pprint(st_matrix)

        # mix column with round no N
        st_matrix = mix_column(st_matrix, 'e')
        print("\nMIX COLUMN....")
        pprint.pprint(st_matrix)

        # add round key with round no N
        st_matrix = add_round_key(st_matrix,i,round_key)
        print("\nROUND KEY....")
        pprint.pprint(st_matrix)
        
    # substitution bytes with round no N
    st_matrix = substitution_bytes(st_matrix, 'e')
    print("\nSUBSTITUTION BYTES....")
    pprint.pprint(st_matrix)

    # shift rows with round no N
    st_matrix = shift_rows(st_matrix, 'e')
    print("\nSHIFT ROWS....")
    pprint.pprint(st_matrix)

    # add round key with round no N
    st_matrix = add_round_key(st_matrix,10,round_key)
    
    
    print("\nCIPHER TEXT ==========================")
    pprint.pprint(st_matrix)
    
    return st_matrix


def decryption(cipherText):
    
    round_key = key_expansion()
        
    st_matrix = add_round_key(cipherText,10,round_key)
    print("\nROUND KEY....")
    pprint.pprint(st_matrix)
    
    
    for i in range(9, 0, -1):
        st_matrix = shift_rows(st_matrix, 'd')
        print("\nSHIFT ROWS....")
        pprint.pprint(st_matrix) 
        
        st_matrix = substitution_bytes(st_matrix, 'd')
        print("\nSUBSTITUTION BYTES....")
        pprint.pprint(st_matrix) 
               
        st_matrix = add_round_key(st_matrix,i,round_key)
        print("\nROUND KEY....")
        pprint.pprint(st_matrix)
        
        st_matrix = mix_column(st_matrix, 'd')
        print("\nMIX COLUMN....")
        pprint.pprint(st_matrix)
                
        
    st_matrix = shift_rows(st_matrix, 'd')
    st_matrix = substitution_bytes(st_matrix, 'd')
    plain_text_matrix = add_round_key(st_matrix,0,round_key)
    
    print("\nPLAIN TEXT =========================")
    pprint.pprint(plain_text_matrix)

if __name__ == '__main__':

    cipherText = encryption()
    decryption(cipherText)