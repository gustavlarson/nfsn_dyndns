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
* PyYAML: http://pyyaml.org/

Install all using pip:

    pip install ipgetter python-nfsn pyyaml

Configuration
========
Place a configuration file at `/etc/nfsn_dyndns.conf` with the content
```yaml
login: LOGIN_NAME
api-key: API_KEY
domains:
- domain: example.com
```

There is support for multiple domains. Just list all domains under the domains key:
```yaml
domains:
- domain: example.com
- domain: example.net
```


Usage
========
Execute the script using
    ./nfsn_dyndns.py

For continous monitoring of your public IP, configure it to run as a cronjob.
