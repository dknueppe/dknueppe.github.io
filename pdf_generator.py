#!/usr/bin/env python3

import weasyprint as wp
from datetime import date
from pathlib import Path
from os import listdir
files = [f for f in listdir() if '.html' in f]
mail = 'max.musterman@domain.com'
phone ='0123 4567 8910'

for f in files:
    lines = []
    with open(f) as file:
        for line in file:
            if 'id="mail"' in line:
                lines.append('<li id="mail"><a href="mailto:{}">{}</a></li>'.format(mail, mail))
            elif '<hr>' in line:
                pass
            elif 'id="phone"' in line:
                lines.append('<li id="phone">{}</li>\n'.format(phone))
            else:
                lines.append(line)

    lines = ''.join(lines)

    doc = wp.HTML(string=lines, base_url='./')
    doc.write_pdf(Path('Lebenslauf_wp.pdf'))
    # doc.write_pdf(Path(f.split('.')[0] + '.pdf'))
