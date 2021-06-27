# auto_tools_master(自动化办公工具)
---

### 创建环境

- 创建虚拟环境
pip install virtualenv

pip install virtualenvwrapper  这是对virtualenv的封装版本，一定要在virtualenv后安装 

mkvirtualenv -p python3 auto_tools_master

- 安装依赖包
进入虚拟环境文件
cd envname
进入相关的启动文件夹
cd Scripts

activate  启动虚拟环境
deactivate 退出虚拟环境

pip install -r requirements.txt

- 打包安装包
pip freeze > requirements.txt

