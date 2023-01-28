import argparse
import hashlib

parser = argparse.ArgumentParser(description='Hasing giving password') 
parser.add_argument('password', help='Password to hash')
parser.add_argument('-a', '--type', default='sha256', choices=['sha256', 'sha512', 'md5'])
args = parser.parse_args()


password = args.password 
hashtype = args.type
m = getattr(hashlib, hashtype)()
m.update(password.encode())


print("< hash-type : " + hashtype + " >")
print(m.hexdigest())

123123print (m.digest_size)sadsaddasdasddasdas