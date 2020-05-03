import json

def delete_line(file_name,word):
    with open(file_name,"r+",encoding='utf8',errors='ignore') as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if word not in line:
                f.write(line)
        f.truncate()

def open_file(file_name):
    delete = 0
    with open(file_name,'r',encoding='utf8',errors='ignore') as file: 
        for line in file:        
            for word in line.split():            
                if not word.isascii():
                    delete_line(file_name,word)
                    delete+=1
    print('Line deleted =',delete)

def read_file(file_name,list_of_elements):
    with open(file_name) as f:
        data = json.load(f)
    for c in data['conversations']:
        for u in c['uris']:
            for element in list_of_elements:
                print(u[element])
            print('---------------------------------------------------')

#l = ['id','server_ip_port','uri','short_uri','req_head','res_base64','magic_name','magic_ext','res_head','res_num','res_type','host','referer','filename','method','epochtime','res_len','md5','sha256']
l = ['id','server_ip_port','uri','short_uri','res_base64','magic_name','magic_ext','res_head','res_num','res_type','host','referer','filename','method','epochtime','res_len','md5','sha256'] #Without req_head

#read_file('test.json',l)
#open_file('data20.json')
read_file('test.json',l)
#open_file('data21.json')



'''import json
with open("data7.json", 'rb') as f:
    contents = f.read()
    
with open("data7.json", encoding="utf8", errors='ignore') as f:
    contents = f.read()
    s=""
    contents = contents.encode().decode()
    if '\u9c87' in contents:
        contents = ""
    else:
        print(contents)
print("fin")'''

'''f = open('data7.json','r', encoding='utf8',errors='ignore')
r = f.readlines()
for i in r:
    print(i.encode('utf-8'))'''
    
'''def is_ascii(s):
    return all(ord(c) < 128 for c in s)

try:
                pass
            except
                print ("It was not a ascii-encoded unicode string",word)
            else:
                #print ("It may have been an ascii-encoded unicode string",word)
                pass'''
