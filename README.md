# check_mssql_metrics
Naemon and Nagios -compatible module for fetching metrics of Microsoft SQL Server databases.

This is an early version of the plug-in. Only the database size part of it is implemented at the moment, but more functionality is on the way!

Please let me know if you experience any issues when using the plug-in by making an issue in the Github project for it.


REQUIREMENTS

* This script requires Python 3.2 or newer (which includes the argparse module), and the mssql_python module. Install it with 'pip3 install mssql-python'.
* mssql-python requires the libltdl library. On Debian and Ubuntu systems, install that with 'apt install libltdl7'.
* The MSSQL user employed by the script must have the 'VIEW SERVER STATE' permission on the 'master' database, and 'CONNECT' and 'SELECT' privileges on each database it gathers metrics on.

To grant VIEW SERVER STATE permission, run the following SQL as an administrative user:
USE MASTER
GRANT VIEW SERVER STATE TO [username]


Usage: check_mssql_metrics.py [-h] -s server -d database -u username -p password [-e encrypt] [-t trust] [-w warnsize] -m maxsize

options:

  -h, --help            show this help message and exit

  -s, --server Database server / host to connect to.

  -d, --database Database to connect to.

  -u, --username User name of user to connect with.

  -p, --password Password for the user that is connecting.

  -e, --encrypt Specify if connection should be encrypted (yes/no). Default is 'yes'.

  -t, --trust Specify to trust the server certificate (yes/no). Default is 'yes'.

  -w, --warnsize Warning database size threshold.

  -m, --maxsize Critical database size threshold.
