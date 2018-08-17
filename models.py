class MDDocument(object):

    def __init__(self, title, lines=[]):
        self.load(title, lines)

    def load(self, title, lines=[]):
        self.title = title
        self.lines = lines

    def dump(self, filename, encoding='utf8'):
        pass

class MDBaseElement(object):
    
    def __init__(self, parent=None, children=[]):
        self.parent = parent
        self.children = children

# Markdown Root Element
class MDRootElement(MDBaseElement):

    def __init__(self):
        pass

# Markdown Syntax Element
class MDSyntaxElement(MDBaseElement):
    
    def __init__(self):
        self.start_delimiter = []
        self.end_delimiter = []

class MDBlockElement(MDSyntaxElement):
    pass

class MDInlineElement(MDSyntaxElement):
    
    def __init__(self):
        pass

# Markdown Block Element
class MDHtmlBlockTag(MDBlockElement):
    pass

class MDParagraph(MDBlockElement):
    pass

class MDHeader(MDBlockElement):
    pass

class MDBlockquote(MDBlockElement):
    pass

class MDList(MDBlockElement):
    pass

class MDBlockCode(MDBlockElement):
    pass

class MDHorizontalLine(MDBlockElement):
    pass

# Markdown Inline Element
class MDHtmlInlineTag(MDInlineElement):
    pass

class MDHtmlSpecialChar(MDInlineElement):
    pass

class MDInlineLink(MDInlineElement):
    pass

class MDReferenceLink(MDInlineElement):
    pass

class MDInlineImg(MDInlineElement):
    pass

class MDReferenceImg(MDInlineElement):
    pass

class MDEmphasis(MDInlineElement):
    pass

class MDBreakLine(MDInlineElement):
    pass

class MDInlineCode(MDInlineElement):
    pass

class MDEscapeChar(MDInlineElement):
    pass