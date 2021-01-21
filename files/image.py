import re
img_parttern = r'\!\[.*\]\((.*)\)'
class Image:
    def __init__(self):
        pass
    
    def read_uri(self, line):
        img = re.search(img_parttern, line)
        if img != None:
            return img.group(1)

