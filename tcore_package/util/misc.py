from itertools import imap

def indent_text(text, indent):
    return reduce(lambda line1,line2: '%s\n%s' % (line1, line2),
                  imap(lambda line: (' ' * 4 * indent) + line,
                      text.splitlines()))