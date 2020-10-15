
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
    #your going to need to hard code the binary key because I didn't have time to build in that functionality yet. 
    #binary_key = [7, 7, 7, 7, 7, 6, 6, 7, 7, 6, 7, 6, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 6] 
    decoder(array_of_image, binary_key)
