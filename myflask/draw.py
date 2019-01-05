from neo4j.v1 import GraphDatabase
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
year_list=[2016,2017,2018]
driver = GraphDatabase.driver("bolt://localhost:11006", auth=("neo4j", "123"))


# cy = 'match (p:case_lable) return p.p_number'
# dict_p_number = {}
# with driver.session() as session:
#     result = session.run(cy)
#     for records in result:
#         for record in records:
#             if record == '未知':
#                 continue
#             if record not in dict_p_number:
#                 dict_p_number[record] = 1
#             else:
#                 dict_p_number[record] += 1
# labels = list(dict_p_number.keys())
# fracs = list(dict_p_number.values())
# print(labels)
# print(fracs)
#
# plt.bar(range(len(fracs)), fracs,color='rgb',tick_label=labels)
# plt.savefig(r'C:\Users\lenovo\Desktop\p_number.jpg')
# plt.show()

def career():
    cy = 'match (p:people_lable) return p.career'
    dict_contact = {}
    with driver.session() as session:
        result = session.run(cy)
        for records in result:
            for record in records:
                if record == '未知' or record == '无':
                    continue
                if record == '务工' or record == '务工人员' or record == '农民工' or record == '打工' or record == '劳务人员':
                    record = '务工'
                if record != '务工' and record != '经商' and record != '无业' and record != '居民' and record != '农民':
                    record = '其他'
                if record not in dict_contact:
                    dict_contact[record] = 1
                else:
                    dict_contact[record] += 1
    labels = list(dict_contact.keys())
    fracs = list(dict_contact.values())
    print(labels)
    print(fracs)
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    # autopct ，show percet
    plt.pie(x=fracs, labels=labels, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
    plt.title('职业')
    plt.savefig(r'F:\Date\neo4j\img\career.jpg')
    plt.show()

def education():
    cy = 'match (p:people_lable) return p.education'
    dict_contact = {}
    with driver.session() as session:
        result = session.run(cy)
        for records in result:
            for record in records:
                if record == '未知' or record == '无':
                    continue
                if record == '职业技术':
                    record = '专科'
                if record == '文盲' or record == '半文盲':
                    record = '文盲/半文盲'
                if record == '大学' or record == '研究生' or record == '本科':
                    record = '本科/研究生'
                if record not in dict_contact:
                    dict_contact[record] = 1
                else:
                    dict_contact[record] += 1
    labels = list(dict_contact.keys())
    fracs = list(dict_contact.values())
    print(labels)
    print(fracs)
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    # autopct ，show percet
    plt.pie(x=fracs, labels=labels, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=180, pctdistance=0.6)
    plt.title('文化程度')
    plt.savefig(r'F:\Date\neo4j\img\education.jpg')
    plt.show()

def gender_draw():
    cy = 'match (p:people_lable) return p.gender'
    dict_contact = {}
    with driver.session() as session:
        result = session.run(cy)
        for records in result:
            for record in records:
                if record == '未知' or record == '无':
                    continue
                if record not in dict_contact:
                    dict_contact[record] = 1
                else:
                    dict_contact[record] += 1
    labels = list(dict_contact.keys())
    fracs = list(dict_contact.values())
    print(labels)
    print(fracs)
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    # autopct ，show percet
    plt.pie(x=fracs, labels=labels, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=180, pctdistance=0.6)
    plt.title('性别')
    plt.savefig(r'F:\Date\neo4j\img\gender.jpg')
    plt.show()

def contact_draw():
    for i in year_list:
        cy = 'match (p:case_lable) where p.c_id contains \'' + str(i) + '\' return p.contact'
        dict_contact = {}
        with driver.session() as session:
            result = session.run(cy)
            for records in result:
                for record in records:
                    if record == '未知':
                        continue
                    if record not in dict_contact:
                        dict_contact[record] = 1
                    else:
                        dict_contact[record] += 1
        labels = list(dict_contact.keys())
        fracs = list(dict_contact.values())
        print(labels)
        print(fracs)
        plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
        # autopct ，show percet
        plt.pie(x=fracs, labels=labels, autopct='%3.1f %%',
                shadow=True, labeldistance=1.1, startangle=180, pctdistance=0.6)
        plt.title('联系方式'+str(i))
        plt.savefig(r'F:\Date\neo4j\img\contact'+str(i)+'.jpg')
        plt.show()

def payment_draw():
    for i in year_list:
        cy = 'match (p:case_lable) where p.c_id contains \'' + str(i) + '\' return p.payment'
        dict_payment = {}
        with driver.session() as session:
            result = session.run(cy)
            for records in result:
                for record in records:
                    if record == '未知':
                        continue
                    if record not in dict_payment:
                        dict_payment[record] = 1
                    else:
                        dict_payment[record] += 1
        labels = list(dict_payment.keys())
        fracs = list(dict_payment.values())
        print(labels)
        print(fracs)
        explode = [0, 0, 0.1, 0, 0]  # 0.1 凸出这部分，
        plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
        # autopct ，show percet
        plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
                shadow=True, labeldistance=1.1, startangle=180, pctdistance=0.6)
        plt.title('交易方式' + str(i))
        plt.savefig(r'F:\Date\neo4j\img\payment'+str(i)+'.jpg')
        plt.show()

def trade_draw():
    for i in year_list:
        cy = 'match (p:case_lable) where p.c_id contains \'' + str(i) + '\' return p.trade'
        dict_trade = {}
        with driver.session() as session:
            result = session.run(cy)
            for records in result:
                for record in records:
                    if record == '未知':
                        continue
                    if record not in dict_trade:
                        dict_trade[record] = 1
                    else:
                        dict_trade[record] += 1
        labels = list(dict_trade.keys())
        fracs = list(dict_trade.values())
        print(labels)
        print(fracs)
        plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
        # autopct ，show percet
        plt.pie(x=fracs, labels=labels, autopct='%3.1f %%',
                shadow=True, labeldistance=1.1, startangle=180, pctdistance=0.6)
        plt.title('交易方式' + str(i))
        plt.savefig(r'F:\Date\neo4j\img\trade'+str(i)+'.jpg')
        plt.show()
