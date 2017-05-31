# juniper-dns-builder-1

Purpose: Creates DNS entries for the interfaces on Juniper devices using the XML configuration from that device.

## Installation

Install Python.  Nothing more required.

## Usage

1. Run command 'show interfaces | display xml' command on Juniper device and place the output in a file (default name is 'config.xml')
2. Remove all output before \<configuration> and after \</configuration>
3. If using a bash log file, remove any ---\<more xx%>--- statements
4. Make sure that the \<configuration> tag has no other information in it (ex: junos:changed-seconds="1494007269" junos:changed-localtime="2017-05-05 14:01:09 EDT")
5. Modify 'coreNumber', 'domain', and 'hostName' variables to match the core number, host name, and domain of the device
6. Put this script in the same folder as your xml file and run

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## Credits

Trevor Rowe

## End

Special thanks to Trevor Rowe

Justin Oeder

http://beyondhosting.net

Managed Public Cloud Provider
