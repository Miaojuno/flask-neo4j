
from neo4j.v1 import GraphDatabase
import os
from tkinter.messagebox import showinfo
import shutil
import os

def loadcsv(dirpath):

    # driver = GraphDatabase.driver("bolt://localhost:11006", auth=("neo4j", "123"))
    # path_all = r'G:\new4j\data\neo4jDatabases\database-1f587c22-a684-4bb5-b830-b588d3b391c5\installation-3.4.9\import'
    # name_all = []
    #
    # for root, dirs, files in os.walk(path_all):
    #     name_all.append(files)  # 当前路径下所有非目录子文件
    #     break
    print(dirpath)
    if os.path.exists(dirpath)==False:
        return 'error'
    driver = GraphDatabase.driver("bolt://localhost:11006", auth=("neo4j", "123"))

    dirr = r'F:\idea\Regex\resources\new'
    while 1:
        try:
            shutil.copytree(dirpath, dirr)
            break
        except:
            dirr += '1'
    os.system('java -jar F:/idea/Regex/out/artifacts/Regex_jar2/Regex.jar')
    # for path in name_all[0]:
    with driver.session() as session:
        session.run('LOAD CSV WITH HEADERS  FROM \"file:///Case.csv\" AS line MERGE (j1:case_lable{c_id:line.案号,'
                    'f_name:line.法院名称,p_number:line.一案人数,fist_name:line.第一被告人,crime:line.罪名,'
                    'c_kind:line.刑罚种类,time:line.刑期,cm_kind:line.财产刑种类,c_money:line.财产刑金额,'
                    'contact:line.联系方式,payment:line.支付方式,trade:line.交易方式,transport:line.运输方式}) ')

        session.run('LOAD CSV WITH HEADERS  FROM "file:///People.csv" AS line WITH line where line.职业 is not null '
                    'MERGE (j2:people_lable{fist_name:line.姓名,gender:line.性别,birth_day:line.出生年月,'
                    'birth_province:line.省份,birth_city:line.城市,nation:line.民族,education:line.文化程度,'
                    'career:line.职业,householdreg:line.户籍地,residence:line.居住地,c_id:line.案号})')

        session.run('MATCH (p:people_lable),(c:case_lable)  '
                    'WHERE p.c_id=c.c_id  '
                    'CREATE (p)-[r:犯案]->(c)  ')

    return 'ok'