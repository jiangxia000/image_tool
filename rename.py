import os

"""
批量重复名
"""
class ImageRename():
    def __init__(self):
        self.path = 'img'  # 需要将图片命名的文件夹路径

    def rename(self):
        #
        filelist = os.listdir(self.path)
        totalnum = len(filelist)

        i = 000

        for item in filelist:
            if item.endswith('.jpg'):
                # os.path.abspath(self.path)   返回self.path的绝对路径
                # os.path.join  把目录和文件名合成一个路径
                src = os.path.join(os.path.abspath(self.path), item)
                # format(str(i), '0>4s') --> 还没有搞懂
                #  0>3s 表示是 三位数字
                dst = os.path.join(os.path.abspath(self.path), format(str(i), '0>3s') + '.jpg')
                os.rename(src, dst)
                i = i + 1


if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()