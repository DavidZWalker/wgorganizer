import sys
import xml.etree.cElementTree as XMLTree

class WGInfo():
    def __init__(self):
        self.xmlFilePath = "data/wginfo.xml"
        self.members = []
        self.readXml()

    def readXml(self):
        self.members = []
        tree = XMLTree.parse(self.xmlFilePath)
        root = tree.getroot()
        for member in root[0].getchildren():
            self.members.append(member.text)

        print(self.members)

    def writeXml(self):
        root = XMLTree.Element("WGInfo")
        membersElem = XMLTree.SubElement(root, "Members")
        for member in self.members:
            memberElem = XMLTree.SubElement(membersElem, "Member")
            memberElem.text = member
        tree = XMLTree.ElementTree(root)
        tree.write(self.xmlFilePath)
