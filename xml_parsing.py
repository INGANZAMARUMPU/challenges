from lxml import etree
from _io import StringIO, BytesIO

import xmltodict 

xml = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ws="http://ws.ussd/">
    <soapenv:Header />
    <soapenv:Body>
        <ws:InsertMO>
            <!--Optional:-->
            <InsertMO>
                <!--Optional:-->
                <msg>*220#</msg>
                <!--Optional:-->
                <msisdn>25761069606</msisdn>
                <!--Optional:-->
                <pass>ussd</pass>
                <!--Optional:-->
                <requestType>100</requestType>
                <!--Optional:-->
                <sessionid>168</sessionid>
                <!--Optional:-->
                <transactionid>W591-28503-1657378849927</transactionid>
                <!--Optional:-->
                <user>ussd</user>
                <!--Optional:-->
                <ussdgw_id>1</ussdgw_id>
            </InsertMO>
        </ws:InsertMO>
    </soapenv:Body>
</soapenv:Envelope>
"""
root = etree.fromstring(xml)

tags = {}
for e in root[1][0][1]:
    if(type(e.tag) == str):
        tags[e.tag] = e.text
print(tags)