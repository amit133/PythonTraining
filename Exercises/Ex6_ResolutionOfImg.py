def find_img_resolution(jpegFile):
    #open image in binary read mode
    with open(jpegFile, 'rb') as img:
        #height of image (in 2 bytes) is at 164th position
        img.seek(163)

        # read the two bytes
        h = img.read(2)

        print(h)

        #calculate height
        height = (h[0] << 8) + h[1]

        # read next bytes for image width
        w = img.read(2)

        #calculate width
        width = (w[0] << 8) + w[1]

        print("Resolution of the image is: {} x {}".format(height, width))

if __name__ == "__main__":
    print("Find the resolution of a jpeg image")
    find_img_resolution('img.jpg')
