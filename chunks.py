from __future__ import with_statement

import json

###
import SimpleHTTPServer
import SocketServer
###

# def paragraphs(line):
#     return [l.split('. ') for l in line.splitlines() if l]
#data = filter(lambda x: len(x) > 0, map(paragraphs, open('text-sample.txt')))
#data = [f.splitlines() for f in open('text-sample.txt') if len(f) > 1]
#data = [l for l in open('text-sample.txt', 'r')]


data = []
with open('text-sample.txt', 'r') as f:
    for f in f.readlines():
        if len(f) > 1:
            line = f.rstrip().split('. ')
            data.append(line)

#data = map(sentences, data)

print(len(data))

j = open('text-output.json', 'w')
j.write(json.dumps(data, sort_keys=True, indent=4))
j.close()

order = [0, 3, 5, 7, 9, 1, 2, 4, 6, 8, 10, 11]


def show_text(data, order=False):
    text = []

    if not order:
        for l in data:
            if isinstance(l, list):
                text.append('. '.join(l))
    else:
        for pos in order:
            text.append('. '.join(data[pos]))

    return '\n\n'.join(text)


with open('text-output.txt', 'w') as f:
    f.write(show_text(data, order))


###

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)


print "serving at port", PORT
httpd.serve_forever()
