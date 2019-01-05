# import csv
#
# csvHand = open(r'G:\new4j\data\neo4jDatabases\database-4d1f8241-eae8-40b5-965b-8e42349e0f11\installation-3.4.9\import\嘉兴11.csv', "r",encoding='utf-8')
# readcsv = csv.reader(csvHand)
# list=[]
# flag=0
# rows=[]
# ll=[]
# for row in readcsv:
#     if flag==0:
#         flag=1
#         for i,w in enumerate(row):
#             ll.append(w)
#             if w=='毒品种类和数量或单位' or w=='毒品单价':
#                 list.append(i)
#     for i,w in enumerate(row):
#         if w=='':
#             ll.append('无')
#         else :
#             ll.append(w)
#     rows.append(ll)
#     ll=[]
# print(rows)
# csvHand = open(r'G:\new4j\data\neo4jDatabases\database-4d1f8241-eae8-40b5-965b-8e42349e0f11\installation-3.4.9\import\嘉兴111.csv', "w+",encoding='utf-8')
# writer=csv.writer(csvHand)
# writer.writerows(rows)


ls=[['王海滨'], ['董良辉'], ['舒金军'], ['黄贵'], ['梁洪江'], ['丁小彬'], ['王帅杰'], ['密林军'], ['张巍巍'], ['陈赛峰']]
re_ls=[]
for i in ls:
    re_ls.append(i[0])
print(re_ls)
del re_ls[re_ls.index('王海滨')]
print(re_ls)