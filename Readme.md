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
Copy `nfsn_dyndns.conf.example` to `/etc/nfsn_dyndns.conf` and edit it to suit your needs.
```yaml
# Your NFSN login name and API key
login: LOGIN_NAME
api-key: API_KEY

# List your domains to monitor and update. Without subdomains, all subdomains are monitored.
domains:
- domain: example.com
- domain: example.net
  subdomains: # Optional, list the subdomains to monitor and update
  - test
  - www
```

There is support for multiple domains. Just list all domains under the domains key.
A domain with subdomains listed will only monitor and update the listed subdomains. Without this key, all subdomains will be monitored and updated.

Usage
========
Execute the script using
    ./nfsn_dyndns.py

For continous monitoring of your public IP, configure it to run as a cronjob.
