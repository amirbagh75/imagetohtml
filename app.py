from PIL import Image
import bs4
import time

with open("index.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt,"html.parser")


photo = Image.open('sample.jpg')
photo = photo.convert('RGB')

width = photo.size[0] 
height = photo.size[1]

for y in range(0, height):
    print (y)
    new_div_tag = bs4.BeautifulSoup('<div class="shit" style="width:auto; height:5px;" id="'+str(y)+'"></div>',"html.parser")
    soup.body.insert(len(soup.body.contents),new_div_tag)
    for x in range(0, width):
        RGB = photo.getpixel((x,y))
        R,G,B = RGB 
        new_div_tag = bs4.BeautifulSoup('<span class="fuck" style="background-color: rgb('+str(R)+','+str(G)+','+str(B)+')"></span>',"html.parser")
        soup.find(id=y).append(new_div_tag)
        # soup.body.insert(3,new_div_tag)

with open(int(time.time())+".html", "w") as outf:
    outf.write(str(soup.prettify()))

