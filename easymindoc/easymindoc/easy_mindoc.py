from easymindoc.mindoc import MinDoc
from easymindoc.markdown import Markdown
from easymindoc.my_config import load_cfg, write_config
# import sys, getopt, os

from pathlib import Path
import typer

app = typer.Typer()

@app.command()
def config(user: str = typer.Option(None), cookies: str = typer.Argument('')):
    typer.echo("正在设置用户和cookies")
    user_data = load_cfg().get('user', {})
    print(user_data)
    cookie = {}
    c = cookies.split('; ')
    for item in c:
        res = item.split('=', 1)
        cookie[res[0]] = res[1]
    user_data['cookies'] = cookie
    if user != None:
        print(user)
        user_data['user']= user
    print(user_data)
    user_data = {'user' : user_data}
    write_config(user_data)

@app.command()
def upload(path: Path = typer.Argument(
    Path.cwd(),
    exists=True,
    readable=True
), project: str = typer.Option(None)):
    user = load_cfg().get('user', {})
    print(path)
    if not user:
        typer.echo("请先设置用户和Cookies, Useage: easy_mindoc config [user_id] [cookies]")
        return
    user['cookies'] = eval(user.get('cookies', {}))
    if path.is_file():
        if project == None:
            typer.echo("请提供project name, Useage: easy_mindoc upload [file_path] --project [project name]")
            return
        upload_file(user, str(path), project)
        return
    elif path.is_dir():
        upload_dir(user, str(path))
        return
    

def upload_file(user: dict, path: Path, project: str):
    doc = MinDoc(user.get('cookies'), project, user.get('user'))
    print(user)
    md = Markdown(str(path))
    'TODO: 监测重定向'
    res = doc.upload_images(md.read_img())
    md.create_sync_file(images=res)
    file_path = md.file[:-3] + '-target.md'
    typer.echo(f"上传成功！ 生成的文件路径为 {file_path}")

def upload_dir(user: dict, path: Path(
    exists=True,
    file_okay=False,
    dir_okay=True,
    writable=False,
    readable=True,
    resolve_path=True,
)):
    'TODO: 文件夹读取'
    pass

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
