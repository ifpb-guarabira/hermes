# -*- coding: utf-8 -*-
import os
from datetime import date
from subprocess import call
from util import date_format

# diretório para armazenamento dos templates.
_template_dir = os.path.join(os.path.dirname(__file__), 'tex')
# diretório para armazenamento dos documentos.
_output_dir   = os.path.join(os.path.dirname(__file__), 'output')


class Template:
    def __init__(self, name):
        self.title   = name
        self.content = open(os.path.join(_template_dir, name + '.tex')).read()


class Builder:
    def __init__(self, template, data):
        today = date.today()
        data['@HOJE'] = date_format('dd de MM de aaaa', today)

        self.prefix = os.path.join(_output_dir, 
                            date_format(template.title + '_aaaa_mm_dd_', today))
        self.result = reduce(lambda x, y : x.replace(y, data[y]),
                                                         data, template.content)
    
    def build(self, id):
        file = self.prefix + id.replace(' ', '_')
        open(file + '.tex', 'w').write(self.result)

        call(['pdflatex', '-output-directory', 'output', file + '.tex'])
        call(['rm', file + '.tex', file + '.aux', file + '.log'])
