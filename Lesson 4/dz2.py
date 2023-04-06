def check_ip(ip:str):
    return all(map(lambda s: False if not s.isdigit() 
                   else (True if int(s) in range(0,256) else False), ip.split('.')))

def check_num(s:str):
    try:
        int(s)
        return True
    except BaseException:
        return False
    


print(check_ip('1.1.1.1'))
print(check_ip('1.1.1.s'))
print(check_ip('1.255.1.1'))
print(check_ip('1.1.256.1'))

