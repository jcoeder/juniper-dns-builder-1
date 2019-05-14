############################# dns-builder-1.py ########################################
# Author: Trevor Rowe
# Purpose: Creates a table of DNS entries for the interfaces on Juniper devices using the XML configuration from the device.
#
##Directions:
##1. Run command 'show interfaces | display xml' command on Juniper device and place the output in a file (default name is 'config.xml')
##2. Remove all output before <configuration> and after </configuration>
##3. If using a bash log file, remove any ---<more xx%>--- statements
##4. Make sure that the <configuration> tag has no other information in it (ex: junos:changed-seconds="1494007269" junos:changed-localtime="2017-05-05 14:01:09 EDT")
##5. Modify 'coreNumber', 'domain', and 'hostName' variables to match the core number, host name, and domain of the device
##6. Put this script in the same folder as your xml file and run
#######################################################################################

import xml.etree.ElementTree as ET

config = ET.parse("config.xml") #enter the input file name as the argument to ET.parse() here (default 'config.xml')
configRoot = config.getroot()

domain = "corp.company.com" #specify domain to create entries for 
hostName = "core-edge-1001" #specify device host name
coreNumber = "-1" #Specify core number (putting the - here instead of in the print statement allows entries to be made with no core number included)

def hasAddress(unit):
        test = unit.find("family")
        if test != None:
            test = test.find("inet")
            if test != None:
                test = test.find("address")
                if test != None:
                    return True
        return False
    
def hasVRRP(unit):
        test = unit.find("family")
        if test != None:
            test = test.find("inet")
            if test != None:
                test = test.find("address")
                if test != None:
                    test = test.find("vrrp-group")
                    if test != None:
                        test = test.find("virtual-address")
                        if test != None:
                            return True
        return False
    
def stripNetMask(address):
    address = address.rsplit("/", 1)
    return address

for interface in configRoot[0]:
    interfaceName = interface.find("name").text
    for unit in interface:
        if hasAddress(unit):
            address = stripNetMask(unit.find("family").find("inet").find("address").find("name").text)
            unitName = unit.find("name").text
            print(address[0] + " " + hostName + "-" + interfaceName + "-" + unitName + coreNumber + "." + domain)
            
        if hasVRRP(unit):
            address = stripNetMask(unit.find("family").find("inet").find("address").find("vrrp-group").find("virtual-address").text)
            unitName = unit.find("name").text
            print(address[0] + " " + hostName + "-" + interfaceName + "-" + unitName + "-00." + domain)
            
            
Credit to Trevor Rowe
