"""
和文件相关的类定义
"""
import json

from data_define import Record
#先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件数据，读到的每一条数据都转换为Reader,将他们封装到list返回即可"""
        pass
class TextFileReader(FileReader):
    def __init__(self,path):#定义成员变量记录文件的路径
        self.path = path  #定义路径

        # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list:list[Record] = []
        for line in f.readlines():
            line = line.strip()#消除换行
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)
        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self,path):#定义成员变量记录文件的路径
        self.path = path  #定义路径
    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list:list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line) #将字符串转变为内部数据结构格式
            record = Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list




if __name__ == '__main__':
    text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("D:/2011年二月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)






