from zipfile import ZipFile
import argparse

parser = argparse.ArgumentParser(description="\n Usage: python bruteforcer_zip.py -z <zipfile.zip> -p <password.txt>")
parser.add_argument("-z", dest="ziparchieve", help="Zip archive to process")
parser.add_argument("-p", dest="passFile", help="Passsword file")
args = parser.parse_args()

try:
    foundPass = ""
except RuntimeError:
    pass