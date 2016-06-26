import web
import json
from havenondemand.hodclient import *
from sklearn import linear_model
hodClient = HODClient("8748e797-7e1e-453f-ba14-aac4e5bc1de7", "v1")
paramArr = {}
hodApp = HODApps.ANALYZE_SENTIMENT
context = {}
context["hodapp"] = hodApp
def give_score(str):
    paramArr["text"] = str
    return (hodClient.post_request(paramArr,hodApp,async=False,**context))['aggregate']['score']
def dame_todo_chido(son):
    array=[]
    for i in json.loads(son):
        array.append(give_score(str(i['user']['message'])))
urls = (
    '/', 'index'
)
class index:
    def POST(self):
         try:
             i = json.loads(web.data())
             return LOL(i)
         except Exception as e:
             # return e
             return json.dumps({"status":"500","method":"post","Error":str(e)})
    def GET(self):
        try:
             i = web.input()
             return i
        except Exception as e:
             return json.dumps({"status":"500","method":"get","Error":str(e)})


def LOL(param):

    jsn=[]
    num=1
    x_train=[]
    y_train=[]
    for i in param:

        for y in i['chat']:

            jon={}
            entero=int(give_score(str(y['user']['message']))*10)
            jon["u"]=entero
            jon["date"]=str(y["user"]["message"])
            jon["value"]=entero
            jon["l"]=num
            x_train.append(str(num))
            y_train.append(str(entero))
            num+=1
            jsn.append(jon)
    return json.dumps(jsn)

app = web.application(urls, globals())
app = app.wsgifunc()
