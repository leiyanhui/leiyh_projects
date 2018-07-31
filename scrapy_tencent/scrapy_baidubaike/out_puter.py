# -*- coding: utf-8 -*-


class OutPut(object):

    def __init__(self):
        self.datas =[]


    def cpllect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open("output.html", 'w')

        fout.write('<html>\n')
        fout.write('<body>\n')
        fout.write('<table>\n')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode("utf-8"))
            fout.write('<td>%s</td>' % data['summary'].encode("utf-8"))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')