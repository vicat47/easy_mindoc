from mindoc import MinDoc
from markdown import Markdown
from easy_mindoc import load_cfg, write_config
import sys, getopt, os

import typer

app = typer.Typer()

'当前工作路径'
os.getcwd()


@app.command()
def config(user: str, cookies: str):
    typer.echo("正在设置用户和cookies")
    user = load_cfg().get('user', {})
    user['user'], user['cookies'] = user, cookies

@app.command()
def upload(path: str):
    user = load_cfg().get('user', {})
    if not user:
        typer.echo("请先设置用户和Cookies, Useage: easy_mindoc config [user_id] [cookies]")
        return
    

@app.command()
def upload_f(path: str, project: str):
    user = load_cfg().get('user', {})
    if not user:
        typer.echo("请先设置用户和Cookies, Useage: easy_mindoc config [user_id] [cookies]")
        return
    doc = MinDoc(user.get('cookies'), project, user.get('user'))
    md = Markdown(path)
    res = doc.upload_images(md.read_img())
    md.create_sync_file(images=res)
    file_path = md.file[:-3] + '-target.md'
    typer.echo(f"上传成功！ 生成的文件路径为 {file_path}")

def main():
    app()

if __name__ == "__main__":
    main()

'''

def main():
    argv = sys.argv[1:]
    inputfile = ''

    user = load_cfg().get('user', {})

    try:
        opts = getopt.getopt(argv,"hu:c:i:",["ifile=", "cookies=", "user="])
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

'''

# if __name__ == "__main__":
#     main()
#     print(load_cfg())
