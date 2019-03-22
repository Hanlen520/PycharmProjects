import xml.dom.minidom as minidom
import sys


def find_activities(filePath):
    xml = minidom.parse(filePath)
    root = xml.getElementsByTagName('manifest')
    appNode = None
    for node in root[0]._get_childNodes():
        if(node._get_localName() == "application"):
            appNode = node
            break
    content = ''
    for item in appNode._get_childNodes():
        if(item._get_localName() == 'activity'):
            content = content + item.getAttribute("android:name") + '\n'

    fs = open("Activity_List", 'w')
    fs.write(content)
    fs.close()


if __name__ == '__main__':
    filePath = sys.argv[1]
    find_activities(filePath)
