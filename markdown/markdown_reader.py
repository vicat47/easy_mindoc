import re

img_parttern = r'\!\[.*\]\((.*)\)'
ann_parttern = r'\[.*\]\(((?!http.*))\)'
vid_parttern = r''

class Markdown:
    def __init__(self, file):
        self.file = file
        self.images = []
        self.annexs = []
        self.videos = []
    def read_img(self):
        images = []
        with open(self.file, 'r', encoding='utf-8') as f:
            for line in f:
                img = re.search(img_parttern, line)
                if img != None:
                    images.append(img.group(1))
        return images
    
    def read_ann(self):
        annexs = []
        with open(self.file, 'r', encoding='utf-8') as f:
            for line in f:
                ann = re.search(ann_parttern, line)
                if ann != None:
                    annexs.append(ann.group(1))
        return annexs

    def read_vid(self):
        videos = []
        with open(self.file, 'r', encoding='utf-8') as f:
            for line in f:
                vid = re.search(vid_parttern, line)
                if vid != None:
                    videos.append(vid.group(1))
        return videos

    def create_sync_file(self, images=[], annexs=[], videos=[]):
        with open(self.file, 'r', encoding='utf-8') as source:
            with open(self.file[:-3] + '-target.md', 'w+', encoding='utf-8') as target:
                for source_line in source:
                    target.write(line_replace(source_line, images=images, annexs=annexs, videos=videos))
            

def line_replace(line, images=[], annexs=[], videos=[]):
    if re.search(img_parttern, line):
        for s, t in images:
            line = line.replace(s, t)
    if re.search(ann_parttern, line):
        for s, t in annexs:
            line = line.replace(s, t)
    if re.search(vid_parttern, line):
        for s,t in videos:
            line = line.replace(s, t)
    return line


if __name__ == '__main__':
    m = Markdown('01_Alfresco简介.md')
    print(m.create_sync_file(images=[(r'.\01_Alfresco简介.assets\image-20210121093313839.png', '牛逼')]))