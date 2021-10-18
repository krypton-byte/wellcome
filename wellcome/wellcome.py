import os
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from typing import Union

def circle(im:Image.Image)->Image.Image:
    if not im.mode == 'RGBA':
        im  = im.convert('RGBA')
    new = Image.new("L", im.size)
    draw = ImageDraw.Draw(new)
    draw.ellipse([(0,0), new.size], fill=255)
    im.putalpha(new)
    return im

class Wellcome:
    def __init__(self) -> None:
        self.image = Image.open(os.path.dirname(__file__)+'/T1.jpg').convert("RGBA")
        self.font = ImageFont.FreeTypeFont(os.path.dirname(__file__)+'/FreeSerifItalic.ttf', 200)

    def create(self, profile:Union[BytesIO, str], name: str)->Image.Image:
        created = circle(Image.open(profile)).resize((400, 400))
        self.image.paste(created, (760, 220), created.convert('RGBA'))
        text = self.cuttext(name)
        ImageDraw.Draw(self.image).text(((self.image.width/2)-(self.font.getsize(text)[0]/2), 610), text, font=self.font, stroke_width=7, stroke_fill=(0, 0, 0))
        return self.image

    def cuttext(self, text)->str:
        if self.font.getsize(text)[0] < 755:
            return text
        else:
            while(self.font.getsize(text)[0]>755):
                print(text)
                text = text[:-1]
            return text[:-1]+'..'