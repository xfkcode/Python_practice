import os.path

def get_files_recursion_from_dir(path):
    """
    从指定的文件夹递归方式获取全部文件
    :param path: 被判断的文件夹
    :return:list包含全部文件，如果目录不存在或无文件就返回一个空list
    """
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + '/' + f
            if os.path.isdir(new_path):
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}不存在")
        return []
    return file_list