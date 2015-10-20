from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern

MAGIC_RE = r'(\<magic\>)(.*?)\<\/magic\>'

class Magic(Extension):
    def extendMarkdown(self, md, md_globals):
            
        pass
