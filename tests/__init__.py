# TODO split tests by protocol
from io import BytesIO, StringIO
from lxml import etree, html
from lxml.html.clean import clean_html


def parse_html(html_body):
    parser = html.HTMLParser()
    raw = clean_html(html_body)
    tree = html.parse(StringIO(raw), parser)
    xml = etree.tostring(
        tree,
        pretty_print=True,
        xml_declaration=True,
        encoding='UTF-8'
    )
    doc = etree.parse(BytesIO(xml))
    return doc
