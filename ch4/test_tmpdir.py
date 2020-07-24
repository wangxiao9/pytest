__author__ = 'wangxiao'

import pytest
"""
内置tmpdir tmpdir_factory
    - 运行前创建临时文件目录，测试结束后删除
    - tmpdir 作用于函数
    - tmpdir_factory 作用于会话级
"""

def test_tmpdir(tmpdir):
    dir = tmpdir
    print(dir)
    # 创建一个file
    file = dir.join('testcase.py')
    print(file)
    # 创建文件夹
    directory = dir.mkdir('testcase')
    print(directory)
    # 往testcase.py 写入内容
    file.write('create testcase')
    # 读取内容
    print(file.read())

def test_tmpdir_factory(tmpdir_factory):
    # 创建一个目录
    my_dir = tmpdir_factory.mktemp('mydir')
    # 返回当前临时目录
    base_temp = tmpdir_factory.getbasetemp()
    print(my_dir)
    print(base_temp)



if __name__ == '__main__':
    pytest.main(["-s", "-v"])