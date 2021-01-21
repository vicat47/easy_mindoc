from mindoc import MinDoc
from markdown import Markdown
import sys, getopt

doc = MinDoc({'mindoc_id':'1989c3d786ee8bab56f9447c9d543533',
'_xsrf':'YXZ0SXh3UndwV0k0SVY1dzJpNjFkMmcwMlh4MDdXZzY=|1611033865206224907|af719543aa64e5db350a1cbf3fdfdf082386afbc',
'login':'P_-NAwEBDkNvb2tpZVJlbWVtYmVyAf-OAAEDAQhNZW1iZXJJZAEEAAEHQWNjb3VudAEMAAEEVGltZQH_hgAAABD_hQUBAQRUaW1lAf-GAAAAHv-OARoBBnU3MjI3OQEPAQAAAA7XmGQdJDuH8gHgAA==|1611033885607959027|bb598fe9cbdf0c3cc07e4265a9bb34f24f5dbe32'
},
'file_management_system', '1611203604543')

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print('easy_mindoc.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('easy_mindoc.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    md = Markdown(inputfile)
    res = doc.upload_images(md.read_img())
    md.create_sync_file(images=res)

if __name__ == "__main__":
    main(sys.argv[1:])
