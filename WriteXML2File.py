import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape, quoteattr

LINE_TERMINATOR = '\n'

def writeXMLtoFile(root, outFile, indent):
    if root is None:
        return;
    else:
        writeAllChildNodes(root, outFile, indent, 0)

        
'''
For root node i.e level 0, do not add the new line
write the open tag e.g <tag1
if tag has text or children
    close the tag and write text or children
    e.g <tag1>text
    <tag1><child1>
else close the tag as empty. e.g <tag1/>
for every tag, add indentation as needed
'''
def writeAllChildNodes(nodeToTraverse, outFile, indent, level):
    if nodeToTraverse is None:
        return;
    else:
        if level != 0:
            # add a new line
            outFile.write(LINE_TERMINATOR)

        # write tag, its attributes and text
        openElement(nodeToTraverse, outFile, indent, level)

        # process children
        hasChildren = False
        for node in nodeToTraverse:
            if not hasChildren:
                hasChildren = True
                outFile.write('>') # close the parent tag
            writeAllChildNodes(node, outFile, indent, level + 1)
        
        if hasChildren:
            # add a new line
            outFile.write(LINE_TERMINATOR)
        
        # close the tag
        closeElement(nodeToTraverse, outFile, hasChildren, indent, level)

def openElement(element, outFile, indent, level):
    # indentation
    indentStr = indent * level
    outFile.write(indentStr)
    
    # open element tag
    outFile.write('<')
    outFile.write(element.tag)

    SPACE = ' '
    EQL = '='
    # attributes
    keys = element.keys()
    for key in keys:
        outFile.write(SPACE)
        outFile.write(key)
        outFile.write(EQL)
        outFile.write(quoteattr(element.get(key)))
        
    # text
    # check for empty text
    emptyText = hasEmptyText(element)
    if not emptyText:
        # close element
        outFile.write('>')
        # write the text
        outFile.write(escape(element.text.strip()))

def closeElement(element, outFile, hasChildren, indent, level):
    if hasChildren:
        # indentation
        indentStr = indent * level
        outFile.write(indentStr)
    
    # for - empty text or no children > close the tag as empty
    # check for empty text
    emptyText = hasEmptyText(element)
        
    if emptyText and not hasChildren:
        outFile.write('/>')    # empty tag
    else:    
        outFile.write('</')    # end tag
        outFile.write(element.tag)
        outFile.write('>')     # >

    # tail
    if element.tail is not None:
        outFile.write(element.tail.strip())

def hasEmptyText(element):
    emptyText = True
    if element.text is not None:
        text = element.text.strip()
        if text:
            emptyText = False
    return emptyText
