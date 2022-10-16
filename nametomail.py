#! /usr/bin/python3
import argparse
# Usage: python3 nametomail.py -h 
# Example: python3 nametomail.py -f names.txt -d yahoo.com
parser = argparse.ArgumentParser(description='E-mail generator from list of names ')
parser.add_argument("-f", "--file", help = "Specify .txt file, includes list of names")
parser.add_argument("-d", "--domain", help = "Specify domain name to generate E-mails based on")

args = parser.parse_args()
domain=args.domain 

with open(args.file,"r") as filo:
    lines = filter(None, (line.rstrip() for line in filo))
    for line in lines:
        name=line.lower()
        if " " in line:
            name.split()
            first_name=name.split()[0]
            last_name=name.split()[1]
            arr_list=["-","_","."]
            for arr in arr_list :
                # charlie-brown@target.com
                print(first_name+arr+last_name+"@"+domain)
                print(first_name+"@"+domain)
                print(last_name+"@"+domain)
                # CHARLIE-BROWN@target.com
                print(first_name.upper()+arr+last_name.upper()+"@"+domain)
                print(first_name.upper()+"@"+domain)
                print(last_name.upper()+"@"+domain)
                # Charlie-Brown@target.com
                print(first_name.capitalize()+arr+last_name.capitalize()+"@"+domain)
                print(first_name.capitalize()+"@"+domain)
                print(last_name.capitalize()+"@"+domain)
                # Charlie-brown@target.com
                print(first_name.capitalize()+arr+last_name+"@"+domain)

        # ****************************************************************************************
                # brown-charlie@target.com:
                print(last_name+arr+first_name+"@"+domain)
                # BROWN-CHARLIE@target.com
                print(last_name.upper()+arr+first_name.upper()+"@"+domain)
                # Brown-Charlie@target.com
                print(last_name.capitalize()+arr+first_name.capitalize()+"@"+domain)
                # Brown-charlie@target.com
                print(last_name.capitalize()+arr+first_name+"@"+domain)
        # ****************************************************************************************
                # c.brown@target.com: 
                print(first_name[0]+arr+last_name+"@"+domain)
                # charlie.b@target.com
                print(first_name+arr+last_name[0]+"@"+domain)
                # C.BROWN@target.com: 
                print(first_name[0].upper()+arr+last_name.upper()+"@"+domain)
                # CHARLIE.B@target.com
                print(first_name.upper()+arr+last_name[0].upper()+"@"+domain)

                # C.brown@target.com: 
                print(first_name[0].upper()+arr+last_name+"@"+domain)
                # c.BROWN@target.com:
                print(first_name[0]+arr+last_name.upper()+"@"+domain)
                # c.Brown@target.com: 
                print(first_name[0]+arr+last_name.capitalize()+"@"+domain)
                # C.Brown@target.com: 
                print(first_name[0].upper()+arr+last_name.capitalize()+"@"+domain)
                
                # charlie.B@target.com
                print(first_name+arr+last_name[0].upper()+"@"+domain)
                # CHARLIE.b@target.com
                print(first_name.upper()+arr+last_name[0]+"@"+domain)
                # Charlie.B@target.com
                print(first_name.capitalize()+arr+last_name[0].upper()+"@"+domain)
                # Charlie.b@target.com
                print(first_name.capitalize()+arr+last_name[0]+"@"+domain)

        else:
            name.split()
            first_name=name.split()[0]
            print(first_name+"@"+domain)
            print(first_name.upper()+"@"+domain)
            print(first_name.capitalize()+"@"+domain)
