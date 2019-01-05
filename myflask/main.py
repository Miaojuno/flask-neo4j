from flask import Flask,render_template,request
from flask_nav import Nav
from flask_nav.elements import *

from load_data import loadcsv
import trypy
from neo4j_main import maintest
app = Flask(__name__)

nav=Nav()
nav.register_element('top',Navbar(u'Flask入门',
                                    View(u'查询','index'),
                                    Subgroup(u'结果',
                                             View(u'犯罪人员基本信息统计','result1'),
                                             # Separator(),
                                             View(u'毒资支付方式统计', 'result2'),
                                             View(u'毒品交易方式统计', 'result3'),
                                             View(u'贩毒联系方式统计', 'result4'),
                                             View(u'新数据导入', 'add1'),
                                    # View(u'结果','success'),
                                    # ),

)))
nav.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query')
def query():
    return render_template('query.html')

@app.route('/Result',methods=['POST'])
def success():
    if request.method=='POST':
        # anwser
        answer=request.form['an']
        answer=maintest(answer)
        # ----------------------------------------------------------------------------------------
        return render_template('result.html',anwser=answer,mode=3)
    else:
        # return render_template('result.html')
        pass

@app.route('/result1')
def result1():
    return render_template('pe10.html')

@app.route('/result2')
def result2():
    return render_template('result2.html')

@app.route('/result3')
def result3():
    return render_template('result3.html')

@app.route('/result4')
def result4():
    return render_template('result4.html')

@app.route('/add1')
def add1():
    return render_template('add1.html')

@app.route('/Resultadd',methods=['POST'])
def successadd():
    if request.method=='POST':
        strstr=request.form['an2']
        answer='加载完成'
        if loadcsv(strstr)=='error':
            answer='路径错误'
        #----------------------------------------------------------------------------------------
        return render_template('resultadd.html',anwser=answer,mode=3)
    else:
        # return render_template('result.html')
        pass



if __name__ == '__main__':
    nav.init_app(app)
    app.run(debug=True)