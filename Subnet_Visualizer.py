import sys
from prettytable import PrettyTable

def toBin(dec):
    bin = ''
    for i in range(0,8):
        bin += str(dec % 2)
        dec = dec // 2
    bin += ' '
    return bin[::-1]


def invalidIP(address):
    print(address + " is not a valid IP address...")
    sys.exit(0)
    

def IpToBin(address):
    numbers = str.split(address,'.')
    if(not(len(numbers) == 4)):
        invalidIP(address)
    bin = ''
    for num in numbers:
        try:
            if(int(num) < 0 or int(num) > 255):
                 invalidIP(address)
            else:
                bin += toBin(int(num))
        except:
           invalidIP(address)
    return bin


def checkSubnet(first,second,subnet):
    match=''
    for i in range(0,len(first)):
        if(first[i] == ' '):
             match += " "
        elif((subnet[i] == '1' and (first[i] == second[i] or first == ' '))):
             match += '_'
        elif(subnet[i] == '0'):
            match += '*'
        else:
            match += 'X'

    return match

firstIP = input("Enter the First IP address: ")
firstBin= IpToBin(firstIP)
secondIP = input("Enter the Second IP Address: ")
secondBin= IpToBin(secondIP)
subnetMask = input("Enter the Subnet Mask:" )
subnetBin = IpToBin(subnetMask)

check = checkSubnet(firstBin,secondBin,subnetBin)
same = "yes"
if('X' in check):
    same = "no"

table = PrettyTable([' ','Ip Address','Binary'])
table.align = "l"
table.add_row(['First IP',firstIP,firstBin])
table.add_row(['Second IP',secondIP,secondBin])
table.add_row(['Subnet Mask',subnetMask,subnetBin])
table.align = "c"
table.add_row(['--------------','--------------','---------------------------------'])
table.add_row(['Same Subnet ?', same ,check])

print (table)

