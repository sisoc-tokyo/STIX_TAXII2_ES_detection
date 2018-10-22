# Real-time Log Analysis Tool with STIX/TAXII 2.0

We publish the sample code of our research.
The tools are tested in the following environment.

- Log Server
	- Elasticsearch: 5.6.4
	- Logstash: 5.6.4
	- Python 3.6
	- cti-taxii-client

- Proxy Server
	- Squid:3.3
	- Filebeat:5.5.1

- TAXII Server
	- cti-taxii-server
	- medallion 0.1.0
	- Python 2.7.5 

- Real-time detection when receiving logs<br/>
<a href="https://github.com/sisoc-tokyo/STIX_TAXII2_ES_detection/tree/master/detection_from_proxylog">The tools for Real-time detection when receiving logs is here</a><br/>
　The programs for detection launched by Logstash when proxy logs are transferred in real time.<br/>
　This tool compares each proxylog with blacklists and if matches, sends an alert mail.<br/>
　Also add flag "matched" to the "indicator" field in "squid" index which indicates a log matches blacklists.<br/>
　Put the tool on the server where Logstash is running.<br/>

	- logstash.conf: Lofstash configuration file. Proxy logs are sent through the pipline of Logstash. Logstash parses logs and launch the detection prpgram "search_blacklist.py".
 	The useage is the following.<br/>
　Specify the conf file path so that Logstash can loads "logstash.con" during starting.<br/>
	 e.g.）logstash -f /etc/logstash/conf.d/logstash.conf &<br/>
	 The deteciton program "search_blacklist.py" is lauched when Logstash receives logs from Filebeat.<br/>

- Real-time detection when receiving indicators<br/>
<a href="https://github.com/sisoc-tokyo/STIX_TAXII2_ES_detection/tree/master/detection_from_indicator">The tool for Real-time detection when receiving indicators is here.</a><br/>
　Extract domain or IP address from STIX 2.0 indicators, registers them in the blacklist.<br/>
　Compare the extracted domain or IP address with proxy logs, if there is a log which matches indicators, add flag "matched" to the "indicator" field in "squid" index which indicates a log matches blacklists.<br/>
Put the tool on the PC which manages Elastic Stack(e.g. A PC which can access the REST API of Elastic Stack)<br/>

　The useage is the following.<br/>
　python input_report.py {IP address of Elastic Stack}:9200 {STIX 2.0 format json file}<br>
  e.g）python input_report.py 192.0.2.100:9200 apt1.json 

