from tkinter import filedialog as tkFileDialog
import os
import sys
 
 
# 获取文件夹路径
def get_directory_path():
    default_dir = r"C"  # 设置默认打开目录
    # fname = tkFileDialog.askopenfilename(title=u"选择文件",
    #                                      initialdir=(os.path.expanduser(default_dir)))
    d_name = tkFileDialog.askdirectory(title=u"选择文件夹",
                                      initialdir=(os.path.expanduser(default_dir)))
 
    print(d_name)
    return d_name
    
# 新建一个用于保存合并后的文件的文件夹，默认在桌面上，默认名为“合并”
# 在“合并”文件夹下又新建了一个文件夹“batFile”用于保存批处理文件
# 返回结果是两个文件夹的路径
def create_dir():
    default_path = r"C:/Users/lizhi/Desktop"
    default_dir_name = "合并"
    father_folder_name = default_path + "/" + default_dir_name
    is_created = os.path.exists(father_folder_name)
    if not is_created:
        os.mkdir(father_folder_name)
 
    son_folder_name = father_folder_name + "/batFile"
    is_created = os.path.exists(son_folder_name)
    if not is_created:
        os.mkdir(son_folder_name)
 
    return father_folder_name, son_folder_name
 
 
# 新建一个batFile文件，文件名为  选中的文件夹的名字
def create_bat_file(aim_dir_name):
    batch = '''
    @echo off&setlocal enabledelayedexpansion
    cd /d "{0}"
    for /f "delims=" %%a in ('dir /a-d/b *') do set /a Num+=1
    for /l %%a in (1,1,%Num%) do (
    set file="%%a"
    set list=!list!+!file!
    )
    copy /b %list:~1% "{1}"
    '''                              # 字符串内定义了占位符{0},{1}
 
    store_dir_name = create_dir()
    file_name = store_dir_name[0] + "/" + aim_dir_name.split('/')[-1]
    batch = batch.format(aim_dir_name, file_name)
 
    bat_file = store_dir_name[1] + "/" + aim_dir_name.split('/')[-1] + ".bat"
    f = open(bat_file, 'w')
    f.write(batch)
    f.close()
    return bat_file


def execute_bat_file():
    bat_file = create_bat_file(get_directory_path())
    os.system(bat_file)


if __name__ == '__main__':
    execute_bat_file()
    
    