from PIL import Image
import numpy
from numpy import asarray
import ImageManipulation as ImMan


def encoder(text):
    text_to_binary = []
    binary_key = []
    for x in text:
        value = ImMan.ToBinary(x)
        length = len(value)
        binary_key.append(length)
        for y in value:
            text_to_binary.append(y)
    size_of_text = len(text_to_binary)
    count = 0
    shape_of_original_array = numpy.shape(array1)
    list_of_pixels = list(array1.flatten())
    for position, i in enumerate(list_of_pixels):
        if count < size_of_text:
            color_binary = ImMan.ToBinary(i)
            binary_value = ImMan.Message_Embed(color_binary, int(text_to_binary[count]))
            ascii_value = ImMan.ToChar(binary_value)
            ascii_value = numpy.uint8(ascii_value)
            list_of_pixels[position] = ascii_value
        else:
            break
        count += 1
    array2 = asarray(list_of_pixels)
    array3 = numpy.reshape(array2, shape_of_original_array)
    return array3, binary_key


if __name__ == "__main__":
    image_location = input("Enter the location of the Image: ")
    message = input("Enter Message: ")
    img = Image.open(image_location)
    array1 = asarray(img)
    array_of_image, binary_key = encoder(message)
    im = Image.fromarray(array_of_image)
    new_image_name = input("Enter Name of New Image: ")
    im.save(new_image_name+".png")
    string_of_key = ''.join([str(x) for x in binary_key])
    print("Binary Key: ", string_of_key)
    print("Image Encoding Complete")

