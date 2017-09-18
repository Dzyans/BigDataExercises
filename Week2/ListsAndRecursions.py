def bitStr(numDig):

    ##Our list that will hold the bit-strings
    bit_list = []
    bits = []

    ##if 0 we return an empty list
    if numDig == 0:
        return []

    ##making all zeores list
    for x in range(0, numDig):
        bit_list.append(0)

    bits.append(bit_list)

    ##start recursion
    mix_it_up(bit_list, 0, bits)

    return bits

def mix_it_up(bit_list, start_index, final_list):
    if start_index >= len(bit_list):
        return

    new_bit_list = list(bit_list)

    if not (new_bit_list[start_index] == 1):
        new_bit_list[start_index] = 1
        final_list.append(list(new_bit_list))
        mix_it_up(new_bit_list, start_index+1, final_list)


    if not(new_bit_list[start_index] == 0):
        new_bit_list[start_index] = 0
        mix_it_up(new_bit_list, start_index+1, final_list)

hej = bitStr(3)
print(len(hej))
print(hej)