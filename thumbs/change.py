import os
import random
i=0
def rename(path):
    print("?")
    oldpath=path
    global i
    i+=1
    newpath="t_"+str(i)+".jpg"
    print("newpath"+str(i))
    os.rename(oldpath,newpath)  # 对文件进行重命名
    '''
    oldpath = path
    pos1 = path.find('_num_')
    pos2 = path.find('_',pos1+5)
    newpath = path[:pos1]+path[pos2:]
    os.rename(path,newpath)  # 对文件进行重命名
    '''

def find(stringin):
    print(stringin[len(stringin)-3:])
    return stringin[len(stringin)-3:]

def test(path):
    files = os.listdir(path)  # 获取当前目录的所有文件及文件夹
    for file in files:
        try:
            file_path = os.path.join(path, file)  # 获取绝对路径
            if os.path.isdir(file_path):  # 判断是否是文件夹
                test(file_path)  # 如果是文件夹，就递归调用自己
            else:
                #extension_name = os.path.splitext(file_path)  # 将文件的绝对路径中的后缀名分离出来
                #print(extension_name)
                if  find(file_path)== 'jpg':
                    rename(file_path)
        except:
            continue  # 可能会报错，所以用了try-except,如果要求比较严格，不需要报错，就删除异常处理，自己调试


test(r'Z:\\New folder')
print("success")
