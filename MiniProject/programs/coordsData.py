import getPixel

def getData(image_path):
    width, height = getPixel.GetImageDimensions(image_path)
    w,h = 50,50
    left,top=w,h
    right,bottom=300,330
    coordinates=[]
    l,u=0,1
    for j in range (1,6):
        #print(top,bottom)
        top=bottom+h
        bottom=bottom+330
        left,right=50,300
        for i in range(1,11):
            #print(left,right)
            coordinates.append(getPixel.get_black_pixels_in_portion(image_path, left, top, right, bottom))
            l,u=l+1,u+1
            left=right+w
            right=right+300
    return coordinates
