#!/usr/bin/python3
import requests
import threading
import queue
from colorama import Style
from colorama import Fore
import argparse

#variables
host=None
wordlist=None
redirection_text=None
q=queue.Queue()
threads=[]
out_file=None
lock=threading.Lock()
thread_count=None
verbose=True
wordlist_file=None
cookies=None
proxies=None
headers=None
proxy=None



#edited printing function
def printOutput(path,resp,isRedirected):
    if isRedirected:
        print(f"{Fore.RED}/{path} , Status: {resp.status_code}{Fore.RESET}")
    else:
        print(f"{Fore.GREEN}/{path} , Status: {resp.status_code}{Fore.RESET}")

def checkIfRedirected(resp_text):
    if redirection_text in resp_text:
        return True
    return False

def sendRequest(path):
    resp=requests.get(host+path,headers=headers,proxies=proxies)
    isRedirected= checkIfRedirected(resp.text)
    if verbose:
        printOutput(path,resp,isRedirected)
    if not isRedirected:
        q.put([path,resp])
        if not verbose:
            printOutput(path,resp,isRedirected)
            

    

def fileHandle():
    with lock:
        path=wordlist_file.readline()
        path=path.rstrip()
        if path:
            return path
        else:
            return 

def threadHandle():
    path=fileHandle()
    if path:
        sendRequest(path)
        threadHandle()
        


def intiateThreads():
    for i in range(thread_count):
        t=threading.Thread(target=threadHandle)
        threads.append(t)
        i+=1
    for t in threads:
        t.start()

def writeOutputToFile():
    with open(out_file,'w') as file:
        while not q.empty():
            path,resp=q.get()
            file.write(f"/{path} , Status: {resp.status_code}\n")    
        file.close()

def main():
    parser=argparse.ArgumentParser(description="Example: python3 bustme.py -u http://localhost:3000 -s '<title>OWASP Juice Shop</title>' -w /root/wordlist.txt)")
    parser.add_argument('-u','--url', help='Host e.g. http://test.com:8080',default=None)
    parser.add_argument('-w','--wordlist', help='Wordlist to use e.g. /root/wordlist.txt',default=None)
    parser.add_argument('-s','--string', help='The string to match in the response body',default=None)
    parser.add_argument('-p','--proxy', help='Proxy e.g. http://127.0.0.1:8080',default=None)
    parser.add_argument('-c','--cookies', help='Cookies sent with the request e.g. language=en; welcomebanner_status=dismiss',default=None)
    parser.add_argument('-o','--out', help='File to write output to e.g. /root/out.txt',default=None)
    parser.add_argument('-v','--verbose', help='Enable verbose output',action="store_true",default=False)
    parser.add_argument('-t','--threads', help='Threads to use , Default is 10',default=10)
    args=parser.parse_args()
    if not( args.url and args.url and args.wordlist):
        print('''The -u URL -s STRING -w WORDLIST arguments are mandatory
        
Example:
    python3 bustme.py -u http://localhost:3000 -s '<title>OWASP Juice Shop</title>' -w /root/wordlist.txt
        ''')
        parser.print_usage()
        exit()
    global host,wordlist,redirection_text,proxy,cookies,out_file,verbose,thread_count,proxies,headers,wordlist_file
    host=args.url
    wordlist=args.wordlist
    redirection_text=args.string
    proxy=args.proxy
    cookies=args.cookies
    out_file=args.out
    verbose=bool(args.verbose)
    thread_count=int(args.threads)
    if proxy:
        proxies=proxies = {
            'http': proxy,
            'https': proxy
            }
    if cookies:
        headers = {
        'Cookie': cookies
    }
    if wordlist:
        wordlist_file=open(wordlist,'r')
    if not host.endswith('/'):
        host=host+'/'
    print('\nResults::\n')
    intiateThreads()
    for t in threads:
        t.join()
    wordlist_file.close()
    if out_file:
        print(f'\nWriting output to file: {out_file}')
        writeOutputToFile()
    print('\nProgram Finished\n')


main()