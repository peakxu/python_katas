import re
import urllib
import zipfile

NEXT_ID_REGEX = re.compile('Next nothing is (\d+)')

urllib.urlretrieve ("http://www.pythonchallenge.com/pc/def/channel.zip", "channel.zip")
channel_zip = zipfile.ZipFile('channel.zip')

def filename_for_id(id):
    return '{id}.txt'.format(id=id)

def next_id_for_id(id):
    contents = channel_zip.read(filename_for_id(id))
    return int(NEXT_ID_REGEX.search(contents).group(1))

def comments_for_id(id):
    return channel_zip.getinfo(filename_for_id(id)).comment

comments = []
id = 90052

while True:
    try:
        id = next_id_for_id(id)
    except:
        break
    comments.append(comments_for_id(id))

print "".join(comments)
