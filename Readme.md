[![Build Status](https://travis-ci.org/gustavlarson/nfsn_dyndns.svg?branch=master)](https://travis-ci.org/gustavlarson/nfsn_dyndns)
About
========
Dynamic DNS for NearlyFreeSpeech.net!
This python script updates DNS records on NearlyFreeSpeech.net when a change of public ip is detected.

Requirements
========
Requires ipgetter and python-nfsn
* ipgetter: https://github.com/phoemur/ipgetter
* python-nfsn: https://github.com/ktdreyer/python-nfsn

Install both using pip:

    pip install ipgetter
    pip install python-nfsn

Configuration
========
Place a configuration file at `/etc/nfsn_dyndns.conf` with the content
```json
{
  "login": "LOGIN NAME",
  "api-key": "API KEY",
  "domain": "example.com"
}
```

Usage
========
Execute the script using
    ./nfsn_dyndns.py

For continous monitoring of your public IP, configure it to run as a cronjob.
