#!/usr/bin/env python

import re

f1 = open('/Users/damien/EPFL/links.txt', 'r')
res = {}
current = ''
md = ''

title = re.compile(r'^\[(.*?)\]\w*$')
link = re.compile(r'^\[?(.*?)\]?\<(.*?)\>\w*$')

# extract links
for l in f1:
	m = title.match(l)
	if m:
		current = m.group(1)
		res[current] = []
	n = link.match(l)
	if n:
		res[current].append((n.group(1), n.group(2)))

# build markdown
for subject, links in res.iteritems():
	md += '## %s\n' % subject
	for l in links:
		if l[0]:
			md += '- [%s](%s "%s") <small>%s</small>\n' % (l[0], l[1], l[0], l[1])
		else:
			md += '- [%s](%s)\n' % (l[1], l[1])
	md += '\n'

f1.close()


# into the file
f2 = open('resources.md', 'r')
a = re.sub(r'\<!--start--\>(.|\s)*?\<!--end--\>', '<!--start-->\n%s\n<!--end-->' % md, f2.read(), flags=re.M)
f2.close()

f3 = open('resources.md', 'w')
f3.write(a)
f3.close()