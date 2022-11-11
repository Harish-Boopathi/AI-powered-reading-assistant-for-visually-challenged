img = Image.open("your_path/output.jpg")

# describes image format in the output 
print(img)

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)

# write text in a text file and save it to source path
with open('your_path/output.txt',mode ='w') as file:
    file.write(result)
