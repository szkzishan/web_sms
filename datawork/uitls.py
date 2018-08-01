#coding:utf-8
import requests

# 政府项目 痕迹工作法
# 短信测试

class Sms(object):
    '''
    Stirng[] SendMessageData(string strMobile, string messageContent, string sendKey,
            string orgCode,string checkCode,string sendName, string sendGUID, string sendIP, string sendMobile)
        1、  strMobile:要发送的手机号，如果有多个手机号用英文；分割【发送号码不能大于100个】
        2、  messageContent:要发送的信息内容
        3、  sendKey:(20612)，
        4、  orgCode:（348）
        5、  checkCode:（8520611）
        6、  sendName:（李沧区计算机中心 ）
        7、  sendGUID:（可为空）
        8、  sendIP:（35.1.212.253）
        9、sendMobile:（可为空）
        返回发送给每一个人的反馈代码
    '''
    url = "http://35.1.212.253/lcmesage/WebService/Sms.asmx"
    params = {
        "strMobile":"15552290166",
        "messageContent":"qinglong test",
        "sendKey":"20612",
        "orgCode":"348",
        "checkCode":"8520611",
        "sendName":u"李沧区计算机中心",
        "sendGUID":"",
        "sendIP":"35.1.212.253",
        "sendMobile":"",
    }
    def send_sms(self):
        response = requests.post(self.url,self.params)
        print response

# 数据库测试
from peewee_mssql import MssqlDatabase
import peewee
mssql_db = MssqlDatabase('zhengfu', host='192.168.1.111', user='sa', password='qingLong2018')
from peewee import *

mysql_db = MySQLDatabase('zhengfu', **{'host': '192.168.1.111', 'password': 'ql2018', 'port': 3306, 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = mysql_db


class Documentcontent(BaseModel):
    contentid = IntegerField(db_column='ContentID', null=True)
    documentcontent = TextField(db_column='DocumentContent', null=True)
    documentguid = BigIntegerField(db_column='DocumentGuid', null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    creator = CharField(null=True)
    creatorid = CharField(db_column='creatorID', index=True, null=True)
    guid = BigIntegerField(primary_key=True)
    import_ = CharField(db_column='import', null=True)
    jfzprojectguid = CharField(null=True)
    opinionnum = IntegerField(db_column='opinionNum', index=True, null=True)
    parentwordid = CharField(db_column='parentWordID', null=True)
    projectnum = IntegerField(db_column='projectNum', null=True)
    wordid = CharField(db_column='wordID', index=True, null=True)
    wordname = CharField(db_column='wordName', null=True)
    workdate = DateTimeField(db_column='workDate', null=True)
    ysguid = BigIntegerField(null=True)

    class Meta:
        db_table = 'DocumentContent'

class Documentinfo(BaseModel):
    guid = BigIntegerField(db_column='GUID', primary_key=True)
    authtype = CharField(db_column='authType', null=True)
    content = TextField(null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    creator = CharField(null=True)
    creatorid = CharField(db_column='creatorID', index=True, null=True)
    departguid = BigIntegerField(db_column='departGuid', null=True)
    departname = CharField(db_column='departName', null=True)
    departtype = CharField(db_column='departType', null=True)
    departordernum = IntegerField(db_column='departorderNum', null=True)
    doctype = CharField(db_column='docType', null=True)
    flowstatus = IntegerField(db_column='flowStatus', null=True)
    opinionnum = IntegerField(db_column='opinionNum', null=True)
    ordernum = IntegerField(db_column='orderNum', null=True)
    projectnum = IntegerField(db_column='projectNum', null=True)
    remark = TextField(null=True)
    samplestatus = IntegerField(db_column='sampleStatus', null=True)
    status = IntegerField(index=True, null=True)
    title = CharField(null=True)
    weekfeeling = TextField(db_column='weekFeeling', null=True)
    workdate = DateTimeField(db_column='workDate', index=True, null=True)

    class Meta:
        db_table = 'DocumentInfo'

class Mykeywords(BaseModel):
    guid = BigIntegerField(db_column='GUID', primary_key=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    creator = CharField(null=True)
    creatorid = CharField(db_column='creatorID', null=True)
    isshowtype = CharField(db_column='isShowType', null=True)
    ordernum = IntegerField(db_column='orderNum', null=True)
    parentguid = BigIntegerField(db_column='parentGuid', index=True, null=True)
    status = IntegerField(null=True)
    word = CharField(null=True)

    class Meta:
        db_table = 'MyKeywords'

# pymssql
def mssql():
    import pymssql

    conn = pymssql.connect("192.168.1.111", "sa", "qingLong2018", "zhengfu")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM DocumentContent')
    row = cursor.fetchone()
    while row:
        print("ID=%d, Name=%s" % (row[0], row[1]))
        row = cursor.fetchone()

    conn.close()



if __name__ == '__main__':
    # db.connect()
    import codecs
    user = set()
    departname = set()
    for document_content in Documentcontent.select():
        user.add(document_content.creator)
    for document_info in Documentinfo.select():
        user.add(document_info.creator)
        departname.add(document_info.departname)

    for my_key_words in Mykeywords.select():
        user.add(my_key_words.creator)
    user.remove(None)
    departname.remove(None)
    with codecs.open("tongji.txt","w","utf-8") as tong_ji:
        tong_ji.write(u"人员：\n")
        tong_ji.write(",".join(user))
        tong_ji.write("\n")
        tong_ji.write(u"部门：\n")
        tong_ji.write(",".join(departname))
    tong_ji.close()

