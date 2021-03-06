# main2.py

from header2 import header
from lxml import objectify
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph


def parse_xml(xml_file):
    with open(xml_file) as f:
        xml = f.read()

    root = objectify.fromstring(xml)
    return root

def main(pdf_file, xml_file):
    doc = SimpleDocTemplate(
        pdf_file,
        rightMargin=72, leftMargin=36,
        topMargin=125, bottomMargin=18)

    xml = parse_xml(xml_file)

    elements = []

    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
    styles = getSampleStyleSheet()
    for line in range(150):
        paragraph = Paragraph(txt, styles["Normal"])
        elements.append(paragraph)

    doc.xml = xml

    doc.build(elements, onFirstPage=header, onLaterPages=header)

if __name__ == '__main__':
    main(pdf_file='main2.pdf', xml_file='eob.xml')