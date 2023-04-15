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


def makeFlight():
    root = Element("UAM")

    makeFlightIdentifier(root)
    makeDeparture(root)
    makeArrival(root)
    makeRoute(root)
    indent(root)
    dump(root)

    return root


def makeFlightIdentifier(root):
    node = SubElement(root, "flightIdentifier")
    makeUamIdentifier(node)


def makeDeparture(root):
    node = Element("departure")

    makeAirport(node)
    makePlannedDepatureTime(node)
    
    root.append(node)


def makeAirport(node):
    node2 = Element("uamPort")

    SubElement(node2, "uamPortIATA").text = "LAX"

    node.append(node2)

def makePlannedDepatureTime(node):
    node2 = Element("plannedDepatureTime")

    SubElement(node2, "Date").text = "111"
    SubElement(node2, "Time").text = "222"
    SubElement(node2, "TimeReference").text = "333"

    node.append(node2)


def makeArrival(root):
    node = Element("arrival")

    makeAirport(node)
    makePlannedDepatureTime(node)

    root.append(node)

def makeRoute(root):
    node = Element("route")

    makeWayPoint(node)
    makeWayPoint(node)
    makeWayPoint(node)
    makeWayPoint(node)

    root.append(node)

def makeWayPoint(node):
    node2 = Element("waypoint")

    waypointLocation = SubElement(node2, "waypointLocation")
    location = SubElement(waypointLocation, "location")
    SubElement(location, "longitude").text = "126.9525465"
    SubElement(location, "latitude").text = "37.5453577"

    node.append(node2)

def makeUamIdentifier(node):
    node2 = Element("uamIdentification")

    node2.text = "UAL123"

    node.append(node2)


def makeFixmXmlFile():
    root = makeFlight()
    ElementTree(root).write("FixmTestData.xml")


if __name__ == "__main__":   
    makeFixmXmlFile()
