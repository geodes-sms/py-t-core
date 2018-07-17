
import os.path

for fname in os.listdir(os.path.curdir):
    print 'from %s import %s' % (fname[:-3], fname[:-3])
