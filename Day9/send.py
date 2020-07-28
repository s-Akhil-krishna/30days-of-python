import sys
from formatting import format_msg
from send_mail import send_mail
#enabling to format a message with either (username) or (username,website)

def send(name,website=None,to_email=None):
    assert to_email!=None
    msg = None
    if website!=None:
        msg = format_msg(my_name=name,my_website=website)
    else:
        msg = format_msg(my_name=name)
    #now,we have the formatted message,lets send it
    sent = True
    try:
        send_mail(text=msg,to_emails=[to_email])
    except:
        sent = False
    return sent
if __name__ == '__main__':
    args =  sys.argv 
    #cmd: python filename.py arg1 arg2 ... argn
    #args = [filename.py, arg1, arg2,....,argn]
    name,email = 'unknown',None
    if len(args)>1:
        name = args[1]
    if len(args)>2:
        email = args[2]
    response = send(name=name,to_email=email)
    print(response)

