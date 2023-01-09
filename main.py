from PIL import Image, ImageFont, ImageDraw
import qrcode

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#000000"

template = Image.open(r'cert-template.png')
WIDTH, HEIGHT = template.size

def make_certificates(name):
    '''Function to save certificates as a .png file'''


    image_source = Image.open(r'cert-template.png')
    draw = ImageDraw.Draw(image_source)

    basewidth = 114
    hsize=114

    # Finding the width and height of the text. 
    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)
    
    #Make QR Code Of file Path
    QR_img = qrcode.make('https://erp.indira.com/use_name/certificate/'+name+'.pdf')
    #wpercent = (basewidth / float(QR_img.size[0]))
    #hsize = int((float(QR_img.size[1]) * float(wpercent)))
    #print(hsize)
    QR_img = QR_img.resize((basewidth, hsize), Image.ANTIALIAS)
    #img.save('resized_image.jpg')

    #paste the QR_code on Our Image
    image_source.paste(QR_img,(50,1260))
    #save changed Image
    #img.save(r"C:\Users\ADMIN\Desktop\Certificates\\"+name+str(i)+".pdf", "PDF", resolution=100.0)
    

    # Saving the certificates in a different directory.
    image_source.save("./output/" + name +".png")
    print('Saving Certificate of:', name)        

if __name__ == "__main__":

    names = []

    
    with open('names.txt') as f:
        content = f.readlines()
        for item in content:
            names.append(item[:-1].title())

    for name in names:
        make_certificates(name)

    print(len(names), "certificates done.")
