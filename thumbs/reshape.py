
from PIL import Image
import os
 
def cut_image(file, outpath):
    """
    图片压缩尺寸到400*225大小以内，生成到outpath下
    """
    img = Image.open(file)
    print(img.size)
    (image_x,image_y) = img.size
    if not (image_x <= 120 and image_y <= 100):
        if (image_x/image_y) > (120/100):
            new_image_x = 120
            new_image_y = 120 * image_y // image_x
        else:
            new_image_y = 100
            new_image_x = 100 * image_x // image_y
    else:
        new_image_x = image_x
        new_image_y = image_y
        
    new_image_size = (new_image_x,new_image_y)
    print(new_image_size)
        
    new_img = img.resize(new_image_size,Image.ANTIALIAS)
    new_img.save(outpath+file)
    
 
 
if __name__ == "__main__":
    # 当前路径下的所有文件
    path = 'Z:\\New folder'
    files  = os.listdir(path)
    
    # 生成当以下文件夹下
    outpath = 'Z:\\New folder'
    isExists=os.path.exists(outpath)
    if not isExists:
        os.makedirs(outpath)
  
    # 对图片文件逐一处理
    for file in files:
        filename,filetype = os.path.splitext(file)
    #    print(filename,filetype)
        if filetype == '.jpeg' or filetype == '.jpg' or filetype == '.png':
            print(file)
            cut_image(file, outpath)
    
    # exe生成完后，控制台暂停下
    os.system('pause')