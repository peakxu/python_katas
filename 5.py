import pickle, urllib

handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(handle)
handle.close()

for line in data:
    print "".join([e[1] * e[0] for e in line])