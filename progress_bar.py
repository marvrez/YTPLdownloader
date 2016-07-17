import time

class progress_bar(object):
    def __init__(self,barlength = 25):
        self.barlength = barlength
        self.position=  0
        self.longest =   0
    def print_progress(self,cur,total,start):
        current_per = cur/total
        elapsed = time.clock() - start
        curbar = int(current_per * self.barlength)
        bar = "\n[" + "=".join("" for tmp in range(curbar))
        bar += ">"
        bar += " ".join("" for tmp in range(self.barlength - curbar)) + "] "

    def print_end(self,*args): #arbitrary numbers of args

def bytetostr(bits):
    bits = float(bits)
    if  bits >= (1024 ** 4):   #convert from bits to terabytes
        terabytes = bits/ (1024**4)
        size = "%.2fTb" % terabytes
    elif bits >= (1024 ** 3):  #convert from bits to gigabytes
        gigabytes = bits/(1024**3)
        size = "%.2fGb" % gigabytes 
    elif bits >= (1024 ** 2):  #convert from bits to megabytes
        megabytes = bits/(1024**2)
        size = "%.2fMb" % megabytes
    elif bits >= (1024 ** 1):  #convert from bits to kilobytes
        kilobytes = bits/(1024**1)
        size = "%.2fKb" % kilobytes
    else:                      #keep it in bits
        size = "%.2fb"  % bits
    return size

def get_human_time(sec):
    if sec >= 3600: #convert to hours
        return "%d hour(s)" % int(sec/3600)
    elif sec >= 60: #convert to minutes
        return "%d minute(s)" % int(sec/60)
    else:
        return "%d second(s)" % int(sec)
