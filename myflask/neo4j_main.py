# import pandas as pd
import neo4j_word


def maintest(str):
    cy = neo4j_word.word2cypher(str)
    if cy=='special':
        result= neo4j_word.case_or_people(str)
    elif cy!='hard' :
        result= neo4j_word.easycy(cy)
    else:
        result = neo4j_word.hardcy(str)
    return result

# print(maintest('多次犯罪的人'))
# print(maintest('犯罪2次的人'))
# print(maintest('李军'))
# print(maintest('（2016）浙0205刑初367号'))
# print(maintest('贩卖毒品罪的平均罚款'))
# print(maintest('李军的有关案件'))
# print(maintest('2017年的案件'))
# print(maintest('丽水市莲都区人民检察院'))
# print(maintest('一案人数为5的案件'))
# print(maintest('龚毅的犯罪关系'))
# print(maintest('重点关注人员'))
