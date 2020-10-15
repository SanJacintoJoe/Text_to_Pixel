
from PIL import Image
from numpy import asarray
import ImageManipulation as ImMan


def decoder(encod_val, key):
    pixel_list = encod_val.flatten()
    text_of_message = ''
    message = []
    for x in pixel_list:
        binary_rep = str(ImMan.ToBinary(x))
        bit_value = binary_rep[-1]
        message.append(bit_value)
    previous_value = 0
    for x in key:
        list_bit_value = message[previous_value:previous_value+int(x)]
        bit_value_of_letter = ''.join(list_bit_value)
        text_of_message = text_of_message + chr(int(bit_value_of_letter, 2))
        previous_value = previous_value + int(x)
    print(text_of_message)

if __name__ == "__main__":
    image_location = input("Enter the location of the Image: ")
    #binary_key = input("Enter Binary Key: ")

    img = Image.open(image_location)
    array_of_image = asarray(img)
    #binary_key = [7, 7, 7, 7, 7, 6, 6, 7, 7, 6, 7, 6, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 6] #[7, 7, 7, 6, 7, 7, 6, 7, 7, 7, 6, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 6, 7, 7, 6, 6, 6, 6, 6, 6, 7, 7, 7, 6, 7, 7, 6, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 6, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 6, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 6, 7, 7, 7, 6, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 7, 6, 6, 7, 7, 7, 6, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 6, 7, 7, 7, 6, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6]
    print(array_of_image[0])
    decoder(array_of_image, binary_key)




'''from PIL import Image
import numpy
from numpy import asarray
import matplotlib.pyplot as plt

def ToBinary(n):
    if type(n) == str:
        binary = bin(ord(n)).replace("0b", "")
    else:
        binary = bin(n).replace("0b", "")
    return binary

def ToChar(binary):
    Output = 0
    size = len(binary)-1
    for position, x in enumerate(binary):
        Output += int(x) * (2**(size-position))
    return Output

def Message_Embed(binary, value_past):
    if int(binary[-1]) != value_past:
        binary = binary[:-1] + str(value_past)
    else:
        pass
    return binary

def Message_Embed(binary, value_past):
    if int(binary[-1]) != value_past:
        binary = binary[:-1] + str(value_past)
    else:
        pass
    return binary

def split_message_into_char(message):
    chars = []
    for c in message:
        chars.append(c)
    return chars

def string2bits(s=''):
    string_bits = ''
    for x in s:
        string_bits = string_bits + bin(ord(x))[2:].zfill(8)
    return string_bits

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

text  = "All of the birds died in 1986 due to Reagan killing them and replacing them with spies that are now watching us. The birds work for the bourgeoisie."
#list_of_char = split_message_into_char(message)
img = Image.open('Squid.jpg')

array1 = asarray(img)
#tried with 'L' & 'RGB'

def encoder(text):
    text_to_binary = []
    binary_key = []
    for x in text:
        value = ToBinary(x)
        length = len(value)
        binary_key.append(length)
        for y in value:
            text_to_binary.append(y)
    size_of_text = len(text_to_binary)
    count = 0
    list_of_pixels = list(array1.flatten())
    print(len(list_of_pixels))
    for position, i in enumerate(list_of_pixels):
        if count < size_of_text:
            color_binary = ToBinary(i)
            binary_value = Message_Embed(color_binary, int(text_to_binary[count]))
            ascii_value = ToChar(binary_value)
            ascii_value = numpy.uint8(ascii_value)
            list_of_pixels[position] = ascii_value

        else:
            print("position at break= ", position)
            break
        count += 1
    print('value= ', type(list_of_pixels[2]))
    array2 = asarray(list_of_pixels)
    array3 = array2.reshape(668, 474, 3)
    print('After', len(list_of_pixels))
    im = Image.fromarray(array1)
    im.save("your_file.jpeg")
    return array3, binary_key




def decoder(encod_val, key):
    pixel_list = encod_val.flatten()
    text_of_message = ''
    message = []
    for x in pixel_list:
        binary_rep = str(ToBinary(x))
        bit_value = binary_rep[-1]
        message.append(bit_value)
    previous_value = 0
    for x in key:
        list_bit_value = message[previous_value:previous_value+int(x)]
        bit_value_of_letter = ''.join(list_bit_value)
        text_of_message = text_of_message + chr(int(bit_value_of_letter, 2))
        previous_value = previous_value + int(x)
    print(text_of_message)





def check(array_x):
    for p,  o in enumerate(array_x):
        if p == 3:
            break
        else:
            print(o)

# issue with encoder not the array flatting fault.
array_of_image, binary_key = encoder(text)

print(binary_key)
img = Image.fromarray(array_of_image, 'RGB')
img.show()
decoder(array_of_image, binary_key)'''