import requests, json

class MinDoc:
    PROJECT_URL = "http://172.16.0.55/api/upload?identify=%s&guid=%s"
    def __init__(self, cookies, identify, guid):
        '''
        一个文档创建一个MinDoc对象
        guid: 用户id
        cookies: cookie的内容，需要以字典形式传入
        identify: 项目id
        change: 修改记录，以元组数组形式记录。[(before, after),...]
        '''
        self.guid = guid
        self.cookies = cookies
        self.identify = identify
        self.change = []
    def upload_image(self, image_uri):
        url = MinDoc.PROJECT_URL % (self.identify, self.guid)
        data = None
        with open(image_uri, 'rb') as file:
            files = {'editormd-image-file':(image_uri.split('\\')[-1], file, 'image/png')}
            r = requests.post(url, data, files=files, cookies=self.cookies, allow_redirects=False)
            print(r.status_code)
            return json.loads(r.text)
    def upload_images(self, image_uri_arr):
        result = []
        for img in image_uri_arr:
            res = self.upload_image(img)
            if res.get('success') != 1:
                print('%s 上传失败' % (res.get('alt')))
            else:
                result.append((img, res.get('url')))
        return result

if __name__ == '__main__':
    doc = MinDoc({'mindoc_id':'1989c3d786ee8bab56f9447c9d543533',
    '_xsrf':'YXZ0SXh3UndwV0k0SVY1dzJpNjFkMmcwMlh4MDdXZzY=|1611033865206224907|af719543aa64e5db350a1cbf3fdfdf082386afbc',
    'login':'P_-NAwEBDkNvb2tpZVJlbWVtYmVyAf-OAAEDAQhNZW1iZXJJZAEEAAEHQWNjb3VudAEMAAEEVGltZQH_hgAAABD_hQUBAQRUaW1lAf-GAAAAHv-OARoBBnU3MjI3OQEPAQAAAA7XmGQdJDuH8gHgAA==|1611033885607959027|bb598fe9cbdf0c3cc07e4265a9bb34f24f5dbe32'
    },
    'file_management_system', '1611203604543')
    res = doc.upload_image(r'.\image-20210121095229812.png')
    print(res)
