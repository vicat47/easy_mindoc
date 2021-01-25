from mindoc import MinDoc
from markdown import Markdown
from my_config import *
import sys, getopt, os

'当前工作路径'
os.getcwd()

def main():
    argv = sys.argv[1:]
    inputfile = ''

    user = load_cfg().get('user', default={})

    try:
        opts, args = getopt.getopt(argv,"huci:",["ifile=", "cookies=", "user"])
    except getopt.GetoptError:
        print('easy_mindoc.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('easy_mindoc.py -i <inputfile>')
            sys.exit()
        elif opt in ("-u", "--user"):
            '设置用户'
            user['user'] = arg
        elif opt in ("-c", "--cookies"):
            '设置cookies'
            'TODO: 格式化输入。。。。。'
            user['cookies'] = arg
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    
    
    if not user:
        print('请先配置用户信息！')
        sys.exit(2)

    
    doc = MinDoc(user.get('cookies'),
    'file_management_system',
    user.get('user'))

    md = Markdown(inputfile)
    res = doc.upload_images(md.read_img())
    md.create_sync_file(images=res)

if __name__ == "__main__":
    # main()
    print(load_cfg())
