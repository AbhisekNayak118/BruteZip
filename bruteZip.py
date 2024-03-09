from zipfile import ZipFile
import argparse

parser = argparse.ArgumentParser(description="\n Usage: python bruteforcer_zip.py -z <zipfile.zip> -p <password.txt>")
parser.add_argument("-z", dest="ziparchieve", help="Zip archive to process")
parser.add_argument("-p", dest="passFile", help="Passsword file")
parsed_args = parser.parse_args()

try:
    zipArchieve = ZipFile(parsed_args.ziparchieve)
    passFile = parsed_args.passFile
    foundPass = ""
except:
    print(parser.description)
    exit(0)

with open(passFile, 'r') as f:
    for line in f:
        password = line.strip('\n').encode('utf8')
        try:
            foundPass = zipArchieve.extractall(pwd=password)
            if(foundPass == None):  
                print("\n Password found: ", password.decode()) 
        except RuntimeError:
            pass
if foundPass == " ":
    print("\n password not found. try a bigger pass list")