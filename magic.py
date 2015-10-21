import re
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

from imageGen import processString

# Regex for finding user input into [magic] tag
MAGIC_RE = r'(\[magic\] ?)(.*?)\[\/magic\]'

class MagicPattern(Pattern):
    def handleMatch(self, m):
        """
        Handles user input into [magic] tag, processes it,
        and inserts the returned URL into an <img> tag
        through a Python ElementTree <img> Element.
        """
        userStr = m.group(3)
        # print(userStr)
        imgURL = processString(userStr)
        # print(imgURL)
        el = etree.Element('img')
        # Sets imgURL to 'src' attribute of <img> tag element
        el.set('src', imgURL)       
        el.set('alt', userStr)
        el.set('title', userStr)
        return el

class Magic(Extension):
    """
    The actual Magic extension object.
    """
    def extendMarkdown(self, md, md_globals):
        magic = MagicPattern(MAGIC_RE)
        md.inlinePatterns['magic'] = magic

def makeExtension(*args, **kwargs):
    """
    Inform Markdown of the existence of the extension.
    """
    return Magic(*args, **kwargs)
