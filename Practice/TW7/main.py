def crc_encoder(data, divisor) :
    data += '0' * (len(data)-1)
    data_list = list(data)

    for i in range(len(data) - len(divisor) + 1) :
        if data_list[i] == '1' :
            for j in range(len(divisor)) :
                data_list[i+j] = str((int(data_list[i + j]) + int(divisor[j]))%2)

    return ''.join(data_list[-len(divisor) + 1 :])

def crc_decoder(data, divisor) :
    data_list = list(data)

    for i in range(len(data) - len(divisor) + 1) :
        if data_list[i] == '1' :
            for j in range(len(divisor)) :
                data_list[i+j] = str((int(data_list[i + j]) + int(divisor[j]))%2)

    if all(bit == '0' for bit in data_list[-len(divisor) + 1 :]) :
        print("No error")
    else :
        print("Error")

if __name__ == "__main__" :
    dataword = '1001'
    divisor = '1011'
    codeword = dataword + crc_encoder(dataword, divisor)
    print(codeword)
    data = input("Enter data : ")
    crc_decoder(data, divisor)
