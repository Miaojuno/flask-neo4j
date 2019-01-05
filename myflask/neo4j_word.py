#自然语言处理

from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:11006", auth=("neo4j", "123"))

def case_or_people(str):
    if len(str)<=4:#   输入人名
        # cy = 'match (p:people_lable{fist_name:\'' + str + '\'} ) return p'
        cy = 'match (p:people_lable{fist_name:\'' + str + '\'} ) return p.fist_name,p.gender,p.birth_day,' \
                                                          'p.birth_province,p.birth_city,p.nation,p.education,' \
                                                          'p.career,p.householdreg,p.residence,p.c_id'
        #   姓名,性别,出生年月,省份,城市,民族,文化程度,职业,户籍地,居住地,案号
        with driver.session() as session:
            result = session.run(cy)
            str = ''
            ll = ['姓名', '性别', '出生年月', '省份', '城市', '民族', '文化程度', '职业', '户籍地', '居住地', '案号']
            for records in result:
                for i, record in enumerate(records):
                    str += ll[i] + ':' + record + '\n'
        return str
    if str[-1]=='号':#   输入案件名
        #cy = 'match (p:case_lable{c_id:\'' + str + '\'} ) return p'
        cy='match (p:case_lable{c_id:\''+str+'\'} ) return p.c_id,p.f_name,p.p_number,p.fist_name,p.crime,p.c_kind,' \
                                             'p.time,p.cm_kind,p.c_money,p.contact,p.payment,p.trade,p.transport'
        #  案号,法院名称,一案人数,第一被告人,罪名,刑罚种类,刑期,财产刑种类,财产刑金额,联系方式,支付方式,交易方式,运输方式
        with driver.session() as session:
            result = session.run(cy)
            str = ''
            ll=['案号','法院名称','一案人数','第一被告人','罪名','刑罚种类','刑期','财产刑种类','财产刑金额','联系方式','支付方式','交易方式','运输方式']
            for records in result:
                for i,record in enumerate(records):
                    str+=ll[i]+':'+record+'\n'
        return str

def word2cypher(str):

    if str[-3:]=='检察院':#   输入法院
        cy='match (p:case_lable{f_name:\''+str+'\'} ) return p.c_id'
        return cy
    if str[-1]=='号':#   输入案件名
        cy='match(p:case_lable{c_id:\"'+str+'\"})--(n:people_lable)  return p,n'
        return 'special'
    if len(str)<=4:#   输入人名
        cy = 'match(p:peple_lable{c_id:\"' + str + '\"})--(n:case_lable)  return p,n'
        return 'special'
    if str[:5] == '一案人数为' and str[-3:] =='的案件':#   一案人数为xx的案件
        count=str[5:-3]
        cy = 'match (p:case_lable{p_number:\'' + count + '\'} ) return p.c_id'
        return cy
    if str[-5:] == '的有关案件':# xx的有关案件(某人有关案件)
        cy = 'match (p:people_lable{fist_name:\'' + str[:-5] + '\'} ) return p.c_id'
        return cy
    if str[-4:] == '年的案件':  # xxx年的案件(指定年的案件)
        cy = 'match (p:case_lable) where p.c_id contains \'' + str[:4] + '\'  return p.c_id'

        return cy
    else:
        return 'hard'


def easycy(cy):
    with driver.session() as session:
        result = session.run(cy)
        r_list = []
        for records in result:
            r_line = []
            for record in records:
                r_line.append(record)
            r_list.append(r_line)
    return r_list
re_ls_ls=[]
def hardcy(str):
    if str=='重点关注人员':
        result = easycy('match (p:people_lable) return p.fist_name')
        dict = {}
        for name in result:
            if name[0] not in dict:
                dict[name[0]] = 1
            else:
                dict[name[0]] += 1
        ls = []
        for key in dict:
            if dict[key] != 1:
                ls.append(key)
                ls.append(chage(dict[key]))
        lss=[]
        for name in ls:
            cy = 'match (p:case_lable) where p.fist_name = \'' + name + '\'  return p.fist_name,p.time,p.c_id,p.p_number'
            with driver.session() as session:
                result = session.run(cy)
                for records in result:
                    if '年' in records[1] and  '月' not in records[1]:
                        if  '十' in records[1] :
                            if eval(records[3])>=3:
                                lss.append([records[0],records[2]])
        return lss


    # xx罪的平均罚款
    if str[-5:] == '的平均罚款':
        ls='零一二三四五六七八九十'
        result = easycy('match (p:case_lable) where p.crime contains \'' + str[:-5] + '\' return p.c_money')
        count = 0
        sum = 0
        for number in result:
            if number[0]!='无' and '十' not in number[0]:
                try:
                    count += 1
                    num=number[0]
                    if num.isdigit():
                        sum+=eval(num)
                    elif '万' in num and '千' in num:
                        sum += ls.index(num[0]) * 10000+ls.index(num[2]) * 1000
                    elif '万' in num:
                        sum+=ls.index(num[0])*10000
                    elif '千' in num:
                        sum+=ls.index(num[0])*1000
                except:
                    pass
        avg = sum / count
        return avg

    # xx的犯罪关系
    elif str[-5:] == '的犯罪关系':
        name=str[:-5]
        findcontact('', [name])
        return re_ls_ls

    elif str=='多次犯罪的人':
        result = easycy('match (p:people_lable) return p.fist_name')
        dict={}
        for name in result:
            if name[0] not in dict:
                dict[name[0]]=1
            else:
                dict[name[0]]+=1
        ls=[]
        for key in dict:
            if dict[key]!=1:
                ls.append(key)
                ls.append(chage(dict[key]))
                # ls.append(chage(' '+key+':'+chage(dict[key])))
        return ls

    elif str[-3:]=='次的人':#犯罪n次的人
        result = easycy('match (p:people_lable) return p.fist_name')
        dict={}
        for name in result:
            if name[0] not in dict:
                dict[name[0]]=1
            else:
                dict[name[0]]+=1
        ls=[]
        for key in dict:
            if dict[key]==eval(str[2:-3]):
                ls.append(key)
        return ls

    else:
        return '错误'

def chage(dk):
    return str(dk)

def findcontact(c_id1,names):
    for name_ in names:
        result = easycy('match (p:people_lable{fist_name:\'' + name_ + '\'}) return p.c_id')
        for id in result:
            if id[0]!=c_id1:
                result2 = easycy('match (p:people_lable{c_id:\'' + id[0] + '\'}) return p.fist_name')
                re_ls = []
                for i in result2:
                    re_ls.append(i[0])
                if re_ls!=[]:
                    re_ls_ls.append(re_ls)
                    findcontact(id[0], re_ls)
