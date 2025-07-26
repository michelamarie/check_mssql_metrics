#!/usr/bin/python3

# Naemon / Nagios module to fetch size of a given MS SQL database, then alert if above a given threshold
# By Michela Toscano

# mssql-python module is required. Install with 'pip3 install mssql-python'.

import mssql_python
# from mssql_python import connect
import re, sys, argparse

# Set variables from user input

# Define argument options
parser = argparse.ArgumentParser(description='Naemon / Nagios module for Microsoft SQL Server metrics, especially database size. It can also be used as a utility to run a report of database metrics to the terminal.')
parser.add_argument("-s", "--server", metavar='server', type=str, required=True, help="Database server / host to connect to.")
parser.add_argument("-d", "--database", metavar='database', type=str, required=True, help="Database to connect to.")
parser.add_argument("-u", "--username", metavar='username', type=str, required=True, help="User name of user to connect with.")
parser.add_argument("-p", "--password", metavar='password', type=str, required=True, help="Password for the user that is connecting.")
parser.add_argument("-e", "--encrypt", metavar='encrypt', type=str, default="yes", help="Specify if connection should be encrypted (yes/no). Default is 'yes'.")
parser.add_argument("-t", "--trust", metavar='trust', type=str, default="yes", help="Specify to trust the server certificate (yes/no). Default is 'yes'.")
parser.add_argument("-w", "--warnsize", metavar='warnsize', type=float, help="Warning database size threshold.")
parser.add_argument("-m", "--maxsize", metavar='maxsize', type=float, required=True, help="Critical database size threshold.") 
args = parser.parse_args()

# Set variables from user input
server = args.server
database = args.database
user_name = args.username
password = args.password
encrypt = args.encrypt
trust = args.trust
warn_size = args.warnsize
max_size = args.maxsize

# print(server)

connection_string = 'SERVER='+ server + ';DATABASE=' + database + ';UID=' + user_name + ';PWD=' + password + ';Encrypt=' + encrypt + ';TrustServerCertificate=' + trust + ';'

print (connection_string) 

authenticate = mssql_python.connect(connection_string)
cursor = authenticate.cursor()

### Note: output from mssql-python is as one list item in this case. So we convert it to a string, then back to a list with multiple comma-delimited items

# Run stored procedure to fetch space used of database in use (as defined in connection string)
cursor.execute("EXEC sp_spaceused")

# Fetch the output of the space used stored procedure
space_used = cursor.fetchall()

# Transform the strange one-item list output of the stored procedure to a string data structure type.
space_list = str(space_used)

# Transform that new string to a comma-delimited list
delimited = space_list.split(',')

# Set the value of the database size list item in a variable
database_size = delimited[1]

# Slice numbers from database size output
dbfloat = database_size[2:9]

# Transform slice output 
dbfloat = float(dbfloat)

# Close the connection. Without this, Python may throw a segmentation fault with older versions of mssql_python.
authenticate.close()

# Print the list item we want to see (the space used by the database)
print(dbfloat)

if dbfloat < max_size:
    print('OK: Database size within specified parameters')
    sys.exit(0)
else:
    print('CRITICAL: Database size too large or connection failed')
    sys.exit(2)
