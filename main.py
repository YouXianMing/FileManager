from file_manager import *

# 给定文件夹路径
filesList = FileObjectManager(FileObject("/Users/YouXianMing/Desktop")).scan_with_depth(3).all_file_objects()

# 拼接路径数组
filesString = ""
for file in filesList:

    # 如果是文件,则打印
    if file.is_file:
        print(file.file_path)