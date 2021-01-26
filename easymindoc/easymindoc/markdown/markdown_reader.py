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



'''
# request header
POST /api/upload HTTP/1.1
Host: 172.16.0.55
Connection: keep-alive
Content-Length: 416360051
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75
DNT: 1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryO6BEElB7lQszPtyu
Accept: */*
Origin: http://172.16.0.55
Referer: http://172.16.0.55/api/file_management_system/edit/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5
Cookie: _xsrf=YXZ0SXh3UndwV0k0SVY1dzJpNjFkMmcwMlh4MDdXZzY=|1611033865206224907|af719543aa64e5db350a1cbf3fdfdf082386afbc; login=P_-NAwEBDkNvb2tpZVJlbWVtYmVyAf-OAAEDAQhNZW1iZXJJZAEEAAEHQWNjb3VudAEMAAEEVGltZQH_hgAAABD_hQUBAQRUaW1lAf-GAAAAHv-OARoBBnU3MjI3OQEPAQAAAA7XmGQdJDuH8gHgAA==|1611033885607959027|bb598fe9cbdf0c3cc07e4265a9bb34f24f5dbe32; mindoc_id=31d8b81186631f1f15e0567fc1b6b7ea

# form data

------WebKitFormBoundaryO6BEElB7lQszPtyu
Content-Disposition: form-data; name="identify"

file_management_system
------WebKitFormBoundaryO6BEElB7lQszPtyu
Content-Disposition: form-data; name="doc_id"

392
------WebKitFormBoundaryO6BEElB7lQszPtyu
Content-Disposition: form-data; name="id"

WU_FILE_1
------WebKitFormBoundaryO6BEElB7lQszPtyu
Content-Disposition: form-data; name="name"

01_Alfresco简介.mp4
------WebKitFormBoundaryO6BEElB7lQszPtyu
Content-Disposition: form-data; name="type"

video/mp4
------WebKitFormBoundaryO6BEElB7lQszPtyu
Content-Disposition: form-data; name="lastModifiedDate"

Thu Jan 21 2021 12:24:50 GMT+0800 (中国标准时间)
------WebKitFormBoundaryO6BEElB7lQszPtyu
Content-Disposition: form-data; name="size"

416359063
------WebKitFormBoundaryO6BEElB7lQszPtyu
Content-Disposition: form-data; name="editormd-file-file"; filename="01_Alfresco简介.mp4"
Content-Type: video/mp4


------WebKitFormBoundaryO6BEElB7lQszPtyu--

# response
{
  "alt": "01_Alfresco简介.mp4",
  "attach": {
    "attachment_id": 833,
    "book_id": 27,
    "doc_id": 392,
    "file_name": "01_Alfresco简介.mp4",
    "file_path": "/uploads/file_management_system/files/m_2f26422c2277440a94cdb7e83a96396f_r.mp4",
    "file_size": 416359063,
    "http_path": "/attach_files/file_management_system/833",
    "file_ext": ".mp4",
    "create_time": "2021-01-22T11:00:17.401109989+08:00",
    "create_at": 13
  },
  "errcode": 0,
  "is_attach": true,
  "message": "ok",
  "success": 1,
  "url": "/attach_files/file_management_system/833"
}
'''