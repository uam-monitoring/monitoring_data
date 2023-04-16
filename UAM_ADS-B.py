from xml.etree.ElementTree import Element, ElementTree, SubElement, dump

def indent(elem, level=0): #자료 출처 https://goo.gl/J8VoDK
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def makeADSBXmlFile():
    root = makeUAM()

    ElementTree(root).write("ADSTestData/ADSTestData.xml")


def makeUAM():
    root = Element("UAM")
    
    makeFlightIdentifier(root)
    makeCurrentPosition(root)
    indent(root)
    dump(root)

    return root


def makeFlightIdentifier(root):
    node = SubElement(root, "flightIdentifier")

    makeUAMIdentifier(node)


def makeUAMIdentifier(node):
    node2 = Element("uamIdentification")

    node2.text = "UAL123"

    node.append(node2)


def makeCurrentPosition(root):
    node = SubElement(root, "currentPosition")

    makeLocation(node)


def makeLocation(node):
    location_node = Element("location")

    SubElement(location_node, "longitude").text = "126.9525465"
    SubElement(location_node, "latitude").text = "37.5453577"

    node.append(location_node)


if __name__ == "__main__":
    makeADSBXmlFile()