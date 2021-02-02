#!/usr/bin/python3
import requests
from optparse import *
import urllib.parse
parser = OptionParser("""
\033[1;33m This tool is used to guess the paths of a specific website

\033[1;32mAuthored by Hamza-Abdulrahman
        github: https://github.com/Hamza-Abdulrahman/

Use -h to ask for help
""")

parser.add_option("-i","--target",dest="target",type="string",help="Enter your target")
parser.add_option("-f","--file",dest="file",default="wordlist-default.txt",type="string",help="Enter the file possibilities")
parser.add_option("-o","--output",dest="output",help="Enter a FileName for save output")

(options,args) = parser.parse_args()

if not options.target or not options.file :

    print(parser.usage)

else:

    if options.output:
        file = open(options.output,'a')

    target = str(options.target)
    _file = str(options.file)
    read_file = open(f"{_file}", "r")
    print("""
\033[1;33m This tool is used to guess the paths of a specific website

\033[0;91mAuthored ->\033[0;95m Hamza Abdulrahman
        github: https://github.com/Hamza-Abdulrahman/



\033[0;34m[+]Satrting attak ... \033[1;37m
 
""")
    for r in read_file.readlines():

        url = urllib.parse.urljoin(target , r.strip("\n")) 
        response = requests.get(url)
        
        if response.status_code == 200:
            
            print(url , f"\033[0;34m\t\t{response.status_code}\tis founded\033[1;37m")
            if options.output:
                file.write(f"{url}")
            if options.output:
                file.write("\n")
        if options.output : file.close
            

print("\n\n\033[0;34m[+]completed successfully")