RTMPDump
========

iptables -t nat -A OUTPUT -p tcp --dport 1935 \
	-m owner \! --uid-owner root -j REDIRECT

./rtmpsrv &> log.txt  # capture rtmpdump commands ;)

cat log.txt  | grep "^rtmpdump" > download_script.sh

chmod +x download_script.sh

./download_script.sh  # ;)

Tested On
=========

* https://www.cbtnuggets.com/ (easily automated with python-selenium)
