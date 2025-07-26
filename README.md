# check_mssql_metrics
Naemon and Nagios -compatible module for fetching metrics of Microsoft SQL Server databases.

This is an early version of the plug-in. Only the database size part of it is implemented at the moment, but more functionality is on the way!

Please let me know if you experience any issues when using the plug-in by making an issue in the Github project for it.

This script requires the mssql_python module in order to operate. Install it with 'pip3 install mssql-python'.

Usage: check_mssql_metrics.py [-h] -s server -d database -u username -p password [-e encrypt] [-t trust] [-w warnsize] -m maxsize

options:

  -h, --help            show this help message and exit

  -s, --server server       Database server / host to connect to.

  -d, --database database   Database to connect to.

  -u, --username username   User name of user to connect with.

  -p, --password password   Password for the user that is connecting.

  -e, --encrypt encrypt     Specify if connection should be encrypted (yes/no). Default is 'yes'.

  -t, --trust trust         Specify to trust the server certificate (yes/no). Default is 'yes'.

  -w, --warnsize warnsize   Warning database size threshold.

  -m, --maxsize maxsize     Critical database size threshold.
