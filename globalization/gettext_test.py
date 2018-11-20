
import gettext
catalogs = gettext.find("example", localedir="locale", all=True)
print 'catalogs:', catalogs
t = gettext.translation('example', "locale", fallback=True)
_ = t.ugettext
print(_("this message"))
