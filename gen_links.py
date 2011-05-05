import re

f = open('/Users/damien/EPFL/links.txt', 'r')
res = {}
current = ''
md = ''

title = re.compile('^\[(.*?)\]\w*$')
link = re.compile('^\[?(.*?)\]?\<(.*?)\>\w*$')

# extract links
for l in f:
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
		md += '- [%s %s](%s "%s")\n' % (l[0], l[1], l[1], l[0])
	md += '\n'


print md

# into the file
# f = open('resources.md', 'r')
# a = re.match('([.\n]*\<!--start--\>)', f.read(), re.M)
# 
# f = open('resources.md', 'w')
# f.write(a.group(1) + '\n\n' + md)
# f.close()