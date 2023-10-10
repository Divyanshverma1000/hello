import PIL.Image
from PIL import Image
# from termcolor import colored
# import sys

# ASCII_CHAR = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
ASCII_CHAR = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '8', 'O', 'M', 'W', 'B', '@', '$', 'X', 'H', 'G', 'A']
# ASCII_CHAR.reverse()
def graify(image):
    # gray_img  = image.convert('L')
    gray_img = image.convert("L")
    return(gray_img)

def resize_img(image,new_width=80):
    width,height = image.size
    ratio = height/width
    new_height = int(new_width*ratio)
    resized_image = image.resize((new_width,new_height))
    return(resized_image)
def pixel_to_ascii(image):
    pixels = image.getdata()
    # pixels = Image.Image.getdata(image) 
    characters = "".join(ASCII_CHAR[pixel//28]for pixel in pixels)
    return(characters)

####
 
# def pixel_to_ascii(image):
#     pixels = Image.Image.getdata(image)
#     ascii_characters = []

#     for pixel in pixels:
#         # Extract RGB values
#         r, g, b = pixel[:3]

#         # Determine the closest ASCII character based on color intensity
#         intensity = (r + g + b) // 3  # Average intensity
#         ascii_index = (intensity * (len(ASCII_CHAR) - 1)) // 255
#         ascii_character = ASCII_CHAR[ascii_index]

#         # Detect and apply color escape codes
#         color_name = None
#         if r > 200 and g < 100 and b < 100:  # Red
#             color_name = "red"
#         elif r < 100 and g > 200 and b < 100:  # Green
#             color_name = "green"
#         elif r < 100 and g < 100 and b > 200:  # Blue
#             color_name = "blue"

#         if color_name:
#             ascii_character = colored(ascii_character, color_name)

#         ascii_characters.append(ascii_character)

#     return "".join(ascii_characters)
    

####


def main(new_width=80):
    path = input("Enter a valid path to image\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path," is an Invalid path")
    new_image = pixel_to_ascii(graify(resize_img(image)))
    pixelcount = len(new_image)
    ascii_img = "\n".join(new_image[i:(i+new_width)]for i in range(0,pixelcount,new_width))

    # print(ascii_img)
    output_filename = input("Enter a name for the output file (e.g., ascii_art.txt): ")

    with open(output_filename,'w') as f:
        f.write(ascii_img)


main() 
    
# def h():
#      ascii_img= input("enter ere")
#      with open("asc.txt",'w') as f:
#         f.write(ascii_img)

# h()
