import os
from dotenv import load_dotenv

# 定位 .env 文件路径
# 如果 .env 文件与 config.py 在同一目录，则:
# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))
# 如果 .env 文件在 backend 目录下 (即上一级目录，假设 config.py 在 backend/app/config.py)
# 则需要调整路径。当前我们的 .env 和 config.py 都在 backend 目录下。
load_dotenv() # 会自动查找当前目录或父目录的 .env 文件

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 可以添加其他配置
