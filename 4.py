import re
import urllib2

URL_FORMAT_STRING = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={id}'
NEXT_ID_REG_EX = re.compile('nothing is (\d+)')
DIVIDE_BY_TWO = 'Yes. Divide by two and keep going.'

def get_next_item(id):
    page_contents = contents_for_id(id)
    next_id = next_id_from_contents(page_contents, id)
    return next_id

def contents_for_id(id):
    url = URL_FORMAT_STRING.format(id=id)
    response = urllib2.urlopen(url)
    return response.read()

def next_id_from_contents(contents, id):
    match = NEXT_ID_REG_EX.search(contents)
    if match:
        return int(match.group(1))
    if contents.rstrip() == DIVIDE_BY_TWO:  # First encountered at 16044
        return id / 2

id = 11094
for i in xrange(0, 400):
    id = get_next_item(id)
    print id
