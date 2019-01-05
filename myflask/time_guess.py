from neo4j.v1 import GraphDatabase

from neo4j_word import hardcy


class Guess:

    def __init__(self,num):
        x,y1,y2,data=self.loadrawdata()
        print(x)
        print(y1)
        print(y2)
        f=open(r'C:\Users\lenovo\Desktop\x.txt','w')
        for line in x:
            f.write(str(line)+'\n')
        f.close
        f = open(r'C:\Users\lenovo\Desktop\y1.txt', 'w')
        for line in y1:
            f.write(str(line)+'\n')
        f.close
        f = open(r'C:\Users\lenovo\Desktop\y2.txt', 'w')
        for line in y2:
            f.write(str(line)+'\n')
        f.close
        f = open(r'C:\Users\lenovo\Desktop\data.txt', 'w')
        for line in data:
            f.write(str(line)[1:-1]+'\n')
        f.close








    def loadrawdata(self):
        driver = GraphDatabase.driver("bolt://localhost:11006", auth=("neo4j", "123"))
        cy = 'match (p:people_lable) where p.crime contains \'' + '贩卖毒品罪' + '\'  return p.c_kind,p.time,p.cm_kind,p.c_money,p.c_id'
        with driver.session() as session:
            result = session.run(cy)
        self.r_list = []
        for records in result:
            r_line = []
            for record in records:
                r_line.append(record)
            self.r_list.append(r_line)
        self.c_money()
        self.c_kind_chage()
        self.time_chage()
        self.cm_kind_chage()
        self.money_chage()
        x=[]
        y1 = []
        y2 = []
        data=[]
        for line in self.r_list:
            if line[-1]>0:
                l1 = []
                l2 = []
                x.append(line[-1])
                l1.append(line[0])
                l1.append(line[2])
                l2.append(line[1])
                l2.append(line[3])
                y1.append(l1)
                y2.append(l2)
                data.append(line)
        return x,y1,y2,data

    #犯罪金额
    def c_money(self):
        for k, line in enumerate(self.r_list):
            num=hardcy(line[4]+'的贩毒金额是多少')
            self.r_list[k][4] = num

    # 刑伐种类处理
    def c_kind_chage(self):
        for k, line in enumerate(self.r_list):
            if line[0]=='有期徒刑':
                self.r_list[k][0] = 0
            elif line[0]=='拘役':
                self.r_list[k][0] = 1

    # 刑期处理
    def time_chage(self):#刑期处理
        for k,line in enumerate(self.r_list):
            time_str=line[1]
            index_year=-1
            index_month=-1
            if '年' in time_str:
                index_year=time_str.index('年')
            if '月' in time_str:
                index_month=time_str.index('月')
            if index_year==-1 and index_month!=-1:#x月 xx月
                if len(time_str[:index_month])==2:
                    time=self.numchage(time_str[index_month-2])/12
                else :
                    time = self.numchage(time_str[index_month-2]) / 12 +10/12
            elif index_year != -1 and index_month == -1:#x年
                time = self.numchage(time_str[:index_year])
            else:#x年x月
                time = self.numchage(time_str[:index_year])
                if len(time_str[index_year:index_month]) == 3:
                    time += self.numchage(time_str[index_month - 2]) / 12
                else:
                    time += self.numchage(time_str[index_month - 2]) / 12 + 10 / 12
            self.r_list[k][1]=time

    # 财产刑种类处理
    def cm_kind_chage(self):
        for k, line in enumerate(self.r_list):
            if '罚金' in line[2]:
                self.r_list[k][2] = 0
            elif '没收财产' in line[2]:
                self.r_list[k][2] = 1

    # 财产刑金额处理
    def money_chage(self):
        for k, line in enumerate(self.r_list):
            try:
                self.r_list[k][3] = eval(line[3])
            except:
                self.r_list[k][3]=10000


    #中文数字转int
    def numchage(self,str):
        ts = '零一二三四五六七八九'
        tsn='0123456789'
        ss=''
        for x in str:
            try:
                ss += tsn[ts.index(x)]
            except:
                ss+='1'
        return eval(ss)



Guess(num=123)