from sys import argv,exit
import requests

COLOR = {"HEADER": "\033[95m","BLUE": "\033[94m","GREEN": "\033[92m","RED": "\033[91m","ENDC": "\033[0m"}
def get(repo):    
    try:
        url = 'https://raw.githubusercontent.com/'+repo+'/main/code.alf'
        print(COLOR['BLUE']+'Connecting to ['+url+']'+COLOR['ENDC'])
        req = requests.get(url)
        print('Done...')
        f = open(argv[2].split('/')[1]+'.alf','w')
        cont = str(req.content).replace("b'",'',1)
        cont = cont[:-1]
        cont = cont.replace('\\n','\n')
        cont = cont.replace("\\'","'")
        print(COLOR["BLUE"]+"Writing file..."+COLOR["ENDC"])
        f.write(cont)
        print(COLOR["GREEN"]+'Done! You have now installed "'+argv[2]+'"!'+COLOR["ENDC"])
    except Exception as error:
        print(error)
        print(COLOR["RED"]+'It seems to me that repository is not correct. Use "get" like this: username/repo \nP.S. It also has to be on Github.'+COLOR["ENDC"])
def desc(repo):
    try:
        url = 'https://raw.githubusercontent.com/'+repo+'/main/desc.txt'
        req = requests.get(url)
        cont = str(req.content).replace("b'",'',1)
        cont = cont[:-1]
        cont = cont.replace('\\n','\n')
        print(cont)
    except Exception as error:
        print(COLOR["RED"]+'It seems to me that repository is not correct. Use "get" like this: username/repo \nP.S. It also has to be on Github.'+COLOR["ENDC"])
try:
    exec(argv[1]+'("'+argv[2]+'")')
except:
    print(COLOR["RED"]+'Error: I do not know that command.'+COLOR["ENDC"])
