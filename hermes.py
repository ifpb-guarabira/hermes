# -*- coding: utf-8 -*-
import os
from datetime import date
from subprocess import call

# meses do ano em português.
months = ['', 'Janeiro',  'Fevereiro', 'Março',    'Abril',
              'Maio',     'Junho',     'Julho',    'Agosto',
              'Setembro', 'Outubro',   'Novembro', 'Dezembro']

def date_format(fmt, date):
    fmt = fmt.replace('aaaa', '%04d' % date.year)
    fmt = fmt.replace('aa',   '%02d' % date.year)
    fmt = fmt.replace('MM',   months[date.month])
    fmt = fmt.replace('mm',   '%02d' % date.month)
    fmt = fmt.replace('dd',   '%02d' % date.day)

    return fmt

# diretório para armazenamento dos templates.
_template_dir = os.path.join(os.path.dirname(__file__), 'res/tex')

class Template:
    def __init__(self, name):
        self.title   = name
        self.content = open(os.path.join(_template_dir, name + '.tex')).read()

    def render(self, ctx):
        ctx['@HOJE'] = date_format('dd de MM de aaaa', date.today())

        return reduce(lambda x, y : x.replace(y, ctx[y]), ctx, self.content)

# diretório para armazenamento dos documentos.
_output_dir = os.path.join(os.path.dirname(__file__), 'output')

if not os.path.exists(_output_dir):
    os.makedirs(_output_dir)

def cli_builder(template, context, key):
    base_name = os.path.join(_output_dir,
                             template.title +
                             date_format('_aaaa_mm_dd_', date.today()) +
                             key.lower().replace(' ', '_'))

    open(base_name + '.tex', 'w').write(template.render(context))

    call(['pdflatex', '-output-directory', _output_dir, base_name + '.tex'])
    call(['rm', base_name + '.tex', base_name + '.aux', base_name + '.log'])
