
def makeHtmlTag(tag, *args, **kwds):
    print tag
    print args
    print kwds
    def real_decorator(fn):
        print fn
        css_class = " class='{0}'".format(kwds["css_class"]) \
                                     if "css_class" in kwds else ""
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">" + fn(*args, **kwds) + "</"+tag+">"
        return wrapped
    return real_decorator

@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"

print hello()
# <b class='bold_css'><i class='italic_css'>hello world</i></b>