import configparser
import os

user_home = os.environ['HOME']
cfg_file_path = user_home + '\\.easy_mindoc\\config.ini'
if not os.path.exists(cfg_file_path):
    cfg_path = cfg_file_path[:cfg_file_path.rindex('\\')]
    os.makedirs(cfg_path)
conf = configparser.ConfigParser()
conf.read(cfg_file_path, encoding='utf-8')

def load_cfg():
    sections = conf.sections()
    res = {}
    for s in sections:
        res[s] = dict(conf.items(s))
    return res

def write_config(data):
    for sec, val in data.items():
        for k, v in val.items():
            conf.set(sec, k, str(v))
    conf.write(open(cfg_file_path, 'w', encoding='utf-8'))
