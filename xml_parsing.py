from lxml import etree

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

def rootToDict(root):
    tags = {}
    for el in root:
        if(type(el) == etree._Element):
            key = el.tag.split('}')[-1]
            content = rootToDict(el)
            if(content == {}):
                tags[key] = el.text
            else:
                tags[key] = content
    return tags

def xmlToDict(xml):
    return rootToDict(etree.fromstring(xml))

print(xmlToDict(xml))
