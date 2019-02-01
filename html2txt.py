import html2text
import codecs

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True
with codecs.open('./meeting.html', 'r', encoding='utf-8') as f:
    htmlcontent = f.read()
    textcontent = h.handle(htmlcontent)
    write_file = codecs.open('./meeting.txt', 'w+', encoding='utf-8')
    write_file.write(textcontent)
    write_file.close()
