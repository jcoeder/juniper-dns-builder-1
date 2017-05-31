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

Special thanks to Trevor Rowe
Justin Oeder
http://beyondhosting.net
Managed Public Cloud Provider
