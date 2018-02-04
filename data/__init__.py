from lxml import etree


def get_xmlschema():
    with open('../data/schema.xsd', 'r') as xsd:
        xmlschema_doc = etree.parse(xsd)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        return xmlschema
