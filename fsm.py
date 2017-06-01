from transitions.extensions import GraphMachine
from bs4 import BeautifulSoup
from random import randint
import telegram
import urllib
import re



HSR_rDate = r'2017/(0[1-9]|1[012])/(0[1-9]|[12][0-9]|3[01])'
HSR_rStart=r'/([1-9]|1[012])'
HSR_rEnd=r'/([1-9]|1[012])'
HSR_rTime=r'([01][0-9]|2[01234]):([012345][0-9]|60)'



form_data = {
    "StartStation": "", 
    "EndStation": "",
    "SearchDate": "",
    "SearchTime": "",
    "SearchWay":"DepartureInMandarin",
    "RestTime":"",
    "EarlyOrLater":""
}

API_TOKEN = 'YOUR_API_TOKEN'
bot = telegram.Bot(token=API_TOKEN)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_start(self,update):
        text = update.message.text
        if text.lower()=='/start' or text.lower=='/help':
            return 1


    def is_going_to_Station(self, update):
        text = update.message.text
        return text.lower() == '/station'

    def is_going_to_s1(self, update):
        text = update.message.text
        return text =='/1'

    def is_going_to_s2(self, update):
        text = update.message.text
        return text =='/2'

    def is_going_to_s3(self, update):
        text = update.message.text
        return text =='/3'

    def is_going_to_s4(self, update):
        text = update.message.text
        return text =='/4'

    def is_going_to_s5(self, update):
        text = update.message.text
        return text =='/5'

    def is_going_to_s6(self, update):
        text = update.message.text
        return text =='/6'

    def is_going_to_s7(self, update):
        text = update.message.text
        return text =='/7'

    def is_going_to_s8(self, update):
        text = update.message.text
        return text =='/8'

    def is_going_to_s9(self, update):
        text = update.message.text
        return text =='/9'

    def is_going_to_s10(self, update):
        text = update.message.text
        return text =='/10'

    def is_going_to_s11(self, update):
        text = update.message.text
        return text =='/11'

    def is_going_to_s12(self, update):
        text = update.message.text
        return text =='/12'

    def is_going_to_Station2(self, update):
        text = update.message.text
        return text =='/1'

    def is_going_to_User2(self, update):
        text = update.message.text
        return text =='/2'

    def is_going_to_HSRailway(self, update):
        text = update.message.text
        return text.lower() == '/hsrailway'

    def is_going_to_HSRDate(self, update):
        return 1

    def is_going_to_HSRStart(self, update):
        return 1

    def is_going_to_HSREnd(self, update):
        return 1

    def is_going_to_HSRTime(self, update):
        return 1

    def is_going_to_HSRResult(self,update):
        return 1

    def is_going_to_HSRSearch(self,update):
        text = update.message.text
        return text.lower() == '/1'

    def is_going_to_UserState(self,update):
        text = update.message.text
        return text.lower() == '/2'
     
    def is_going_to_chat(self,update):
        return 1 


    #user
    def on_exit_user(self, update):
        print('Leaving stateuser')

    def on_enter_user(self, update):
        bot.send_message(chat_id=update.message.chat.id,text="你好，我是高鐵小幫手~\n想查詢`車站資訊`請點擊或輸入 /Station \n想查詢`高鐵時刻表`請點擊或輸入 /HSRailway \n", parse_mode=telegram.ParseMode.MARKDOWN)
    

    #railway
    def on_enter_Station(self, update):
        bot.send_message(chat_id=update.message.chat.id,text="請輸入`查詢車站`\n /1 南港站\n /2 台北站\n /3 板橋站\n /4 桃園站\n /5 新竹站\n /6 苗栗站\n /7 台中站\n /8 彰化站\n /9 雲林站\n /10 嘉義站\n /11 台南站\n /12 左營站\n",parse_mode=telegram.ParseMode.MARKDOWN)
    
    def on_enter_s1(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/1.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[台北市南港區南港路一段313號](https://goo.gl/maps/ciYcnPoiAaE2)\n營業時間：05:50 ~ 24:00\n售票時間：05:50 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)

    def on_enter_s2(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/2.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[台北市北平西路3號](https://goo.gl/maps/FvTivr4CUyt)\n營業時間：06:00 ~ 24:00\n售票時間：06:00 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)

    def on_enter_s3(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/3.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[新北市板橋區縣民大道二段7號](https://goo.gl/maps/Q3rgWp6npHt)\n營業時間：06:00 ~ 24:00\n售票時間：06:00 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)
        
    def on_enter_s4(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/4.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[桃園市中壢區高鐵北路一段6號](https://goo.gl/maps/mXZE95ZiJwJ2)\n營業時間：06:20 ~ 23:45\n售票時間：06:20 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)
        
    def on_enter_s5(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/5.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[新竹縣竹北市高鐵七路6號](https://goo.gl/maps/qcBME54VtUT2)\n營業時間：06:30 ~ 23:45\n售票時間：06:30 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)
        
    def on_enter_s6(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/6.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[苗栗縣後龍鎮高鐵三路268號](https://goo.gl/maps/4DfP4UoghJS2)\n營業時間：06:20 ~ 23:45\n售票時間：06:20 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)
        
    def on_enter_s7(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/7.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[台中市烏日區站區二路8號](https://goo.gl/maps/aeg9N4upfvq)\n營業時間：06:00  ~ 24:00\n售票時間：06:00  ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)
        
    def on_enter_s8(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/8.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[彰化縣田中鎮站區路二段99號](https://goo.gl/maps/C9JkyfCxhSt)\n營業時間：06:20 ~ 24:00\n售票時間：06:20 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)
        
    def on_enter_s9(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/9.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[雲林縣虎尾鎮站前東路301號](https://goo.gl/maps/ieQfesy6np32)\n營業時間：06:30 ~ 23:45\n售票時間：06:30 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)
        
    def on_enter_s10(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/10.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[嘉義縣太保市高鐵西路168號](https://goo.gl/maps/bVQjvozypoE2)\n營業時間：06:10 ~ 23:45\n售票時間：06:10 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)
        
    def on_enter_s11(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/11.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[台南市歸仁區歸仁大道100號](https://goo.gl/maps/chrAmdydwvT2)\n營業時間：05:50 ~ 24:00\n售票時間：05:50 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)
        
    def on_enter_s12(self, update):
        bot.send_photo(chat_id=update.message.chat.id,photo=open('img/12.jpg', 'rb'))
        bot.send_message(chat_id=update.message.chat.id,text="\n地址：[高雄市左營區高鐵路105號](https://goo.gl/maps/KzWT154CTVz)\n營業時間：05:30 ~ 24:00\n售票時間：05:30 ~ 末班車發車時間\n",parse_mode=telegram.ParseMode.MARKDOWN)      
        self.afterstation(update)
        
    def on_enter_afterstation(self, update):
        bot.send_message(chat_id=update.message.chat.id,text="請選擇\n /1 重新查詢\n /2 回到首頁\n")


        #PARSE


    #high_speed_railway 
    def on_enter_HSRailway(self, update):
        bot.send_message(chat_id=update.message.chat.id,text="請輸入`乘車日期`\n例:2017/06/01",parse_mode=telegram.ParseMode.MARKDOWN)
       

 

        

    def on_enter_HSRDate(self,update):
        text = update.message.text
        print(text)
        if re.match(HSR_rDate,text):
            form_data["SearchDate"]=text
            bot.send_message(chat_id=update.message.chat.id,text="請輸入`出發站`\n /1 南港站\n /2 台北站\n /3 板橋站\n /4 桃園站\n /5 新竹站\n /6 苗栗站\n /7 台中站\n /8 彰化站\n /9 雲林站\n /10 嘉義站\n /11 台南站\n /12 左營站\n",parse_mode=telegram.ParseMode.MARKDOWN)
            
        else:
            self.go_back(update)

    def on_enter_HSRStart(self,update):
        text = update.message.text
        if re.match(HSR_rStart,text):
            form_data["StartStation"]=text
            bot.send_message(chat_id=update.message.chat.id,text="請輸入`到達站`\n /1 南港站\n /2 台北站\n /3 板橋站\n /4 桃園站\n /5 新竹站\n /6 苗栗站\n /7 台中站\n /8 彰化站\n /9 雲林站\n /10 嘉義站\n /11 台南站\n /12 左營站\n",parse_mode=telegram.ParseMode.MARKDOWN)
            
        else:
            self.go_back(update)


    def on_enter_HSREnd(self,update):
        text = update.message.text
        if re.match(HSR_rStart,text):
            form_data["EndStation"]=text
            bot.send_message(chat_id=update.message.chat.id,text="請輸入`乘車時間`\n例: 18:00\n",parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            self.go_back(update)


    def on_enter_HSRTime(self,update):
        text = update.message.text
        if re.match(HSR_rTime,text) :
            form_data["SearchTime"]=text
            print(text)
            self.go_to_HSRCheck(update)
        else:
            self.go_back(update)

    def on_enter_HSRCheck(self,update):
        text=form_data["StartStation"]
        if text=='/1':
            station="南港站"
        if text=='/2':
           station="台北站"
        if text=='/3':
            station="板橋站"
        if text=='/4':
            station="桃園站"
        if text=='/5':
            station="新竹站"
        if text=='/6':
            station="苗栗站"
        if text=='/7':
            station="台中站"
        if text=='/8':
            station="彰化站"
        if text=='/9':
            station="雲林站"
        if text=='/10':
           station="嘉義站" 
        if text=='/11':
            station="台南站"
        if text=='/12':
           station="左營站"   

        text=form_data["EndStation"]
        if text=='/1':
            station1="南港站"
        if text=='/2':
            station1="台北站"
        if text=='/3':
            station1="板橋站"
        if text=='/4':
            station1="桃園站"
        if text=='/5':
            station1="新竹站"
        if text=='/6':
            station1="苗栗站"
        if text=='/7':
            station1="台中站"
        if text=='/8':
            station1="彰化站"
        if text=='/9':
            station1="雲林站"
        if text=='/10':
            station1="嘉義站" 
        if text=='/11':
            station1="台南站"
        if text=='/12':
            station1="左營站" 
        bot.send_message(chat_id=update.message.chat.id,text="乘車日期:"+form_data["SearchDate"]+"\n出發站:"+station+"\n抵達站:"+station1+"\n乘車時間:"+form_data["SearchTime"]+"\n\n/1 確認\n /2 取消\n")

    def on_enter_HSRResult(self,update):
        text=update.message.text
        if text=='/1':
            text=form_data["StartStation"]
            if text=='/1':
               station="2f940836-cedc-41ef-8e28-c2336ac8fe68"
            if text=='/2':
                station="977abb69-413a-4ccf-a109-0272c24fd490"
            if text=='/3':
                station="e6e26e66-7dc1-458f-b2f3-71ce65fdc95f"
            if text=='/4':
                station="fbd828d8-b1da-4b06-a3bd-680cdca4d2cd"
            if text=='/5':
                station="a7a04c89-900b-4798-95a3-c01c455622f4"
            if text=='/6':
                station="e8fc2123-2aaf-46ff-ad79-51d4002a1ef3"
            if text=='/7':
                station="3301e395-46b8-47aa-aa37-139e15708779"
            if text=='/8':
                station="38b8c40b-aef0-4d66-b257-da96ec51620e"
            if text=='/9':
                station="5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f"
            if text=='/10':
                station="60831846-f0e4-47f6-9b5b-46323ebdcef7" 
            if text=='/11':
                station="9c5ac6ca-ec89-48f8-aab0-41b738cb1814"
            if text=='/12':
                station="f2519629-5973-4d08-913b-479cce78a356"   
            form_data["StartStation"]=station

            text=form_data["EndStation"]
            if text=='/1':
               station="2f940836-cedc-41ef-8e28-c2336ac8fe68"
            if text=='/2':
                station="977abb69-413a-4ccf-a109-0272c24fd490"
            if text=='/3':
                station="e6e26e66-7dc1-458f-b2f3-71ce65fdc95f"
            if text=='/4':
                station="fbd828d8-b1da-4b06-a3bd-680cdca4d2cd"
            if text=='/5':
                station="a7a04c89-900b-4798-95a3-c01c455622f4"
            if text=='/6':
                station="e8fc2123-2aaf-46ff-ad79-51d4002a1ef3"
            if text=='/7':
                station="3301e395-46b8-47aa-aa37-139e15708779"
            if text=='/8':
                station="38b8c40b-aef0-4d66-b257-da96ec51620e"
            if text=='/9':
                station="5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f"
            if text=='/10':
                station="60831846-f0e4-47f6-9b5b-46323ebdcef7" 
            if text=='/11':
                station="9c5ac6ca-ec89-48f8-aab0-41b738cb1814"
            if text=='/12':
                station="f2519629-5973-4d08-913b-479cce78a356"   

            form_data["EndStation"]=station

            url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
            request = urllib.request.Request(url) 
            request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")
            data = urllib.parse.urlencode(form_data)
            binary_data = data.encode('utf-8')
            response = urllib.request.urlopen(request,data=binary_data)  
            html = response.read()
#            print(html.decode("utf-8"))

            
            soup = BeautifulSoup(html,"lxml")
            touch_table = soup.findAll('table',class_='touch_table')

            R={}
            str_R="\n"
            for td in touch_table:
                info = td.findAll('td')
                i=0
                for text in info:
                    if i < 4 :
                        str_R=str_R+text.string+"\t\t\t\t\t\t"
                        i=i+1
                str_R=str_R+"\n"

            
            str_R+="\n\n /1 重新查詢  \n /2 回到首頁\n "

            

            bot.send_message(chat_id=update.message.chat.id,text="車次\t\t出發時間\t\t抵達時間\t\t行車時間"+str_R)
                

        else:
            self.go_back(update)

    def on_enter_chat(self,update):
        text=update.message.text
        if "hi" in text.lower() or "hello" in text.lower() or "你好" in text or "嗨" in text or "哈囉" in text:
            bot.send_message(chat_id=update.message.chat.id,text="你好~我是高鐵小幫手年獸 <3 \n很高興認識你 >////< \n\n")
        else:
            num=randint(0,5)
            if num == 0:
                bot.send_message(chat_id=update.message.chat.id,text="你在說甚麼?\n人家聽不懂啦QuQ\n\n ")
            if num == 1:
                bot.send_message(chat_id=update.message.chat.id,text="可以講人話嗎?\n姊聽不懂啦 (白眼)\n\n")
            if num == 2:
                bot.send_message(chat_id=update.message.chat.id,text="啊，跟你說喔~\n沒事。\n\n")
            if num == 3:
                bot.send_photo(chat_id=update.message.chat.id,photo=open('img/me.jpg', 'rb'))
                bot.send_message(chat_id=update.message.chat.id,text="這是我的自拍照ヽ(✿ﾟ▽ﾟ)ノ\n你喜歡嗎(*´∀`)~♥\n\n")
            if num == 4:
                bot.send_message(chat_id=update.message.chat.id,text="這是我的LINE id~\n***123***\n要記得+我好友喔 >.O\n\n")
            print(num)
        self.go_back(update)
