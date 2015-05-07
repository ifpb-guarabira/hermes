# -*- coding: utf-8 -*-
import os
from datetime import date
from subprocess import call

# Meses do ano em português. months[1] -> Janeiro, months[2] -> Fevereiro...
months = ['', 'Janeiro',  'Fevereiro', 'Março',    'Abril',
              'Maio',     'Junho',     'Julho',    'Agosto',
              'Setembro', 'Outubro',   'Novembro', 'Dezembro']

# Formatador de datas.
def date_format(fmt, date):
    fmt = fmt.replace('aaaa', '%04d' % date.year)  # ano com 4 dígitos
    fmt = fmt.replace('aa',   '%02d' % date.year)  # ano com 2 dígitos
    fmt = fmt.replace('MM',   months[date.month])  # mês em português
    fmt = fmt.replace('mm',   '%02d' % date.month) # mês com 2 dígitos
    fmt = fmt.replace('dd',   '%02d' % date.day)   # dia com 2 dígitos

    return fmt


# diretório dos templates.
_dir     = 'res/tex'
_tpl_dir = os.path.join(os.path.dirname(__file__), _dir)

# shared templates precisam ser injetados no template alvo durante __init__().

# deretório dos templates compartilhados.
_shd     = os.path.join(_tpl_dir, 'shared')
# lista de arquivos da pasta res/tex/shared
_shd_tpl = [os.path.join(_shd, f) for f in os.listdir(_shd)]
# lista de arquivos .tex da pasta res/tex/shared
_shd_tpl = filter(lambda f: f.endswith('.tex'), _shd_tpl)
# dicionário mapeando template a conteúdo.
_shd_tpl = {'\input{%s}' % f[f.find(_dir):] : open(f).read() for f in _shd_tpl}


class Template:
    def __init__(self, name):
        self.title   = name
        # carrega o template alvo.
        self.content = open(os.path.join(_tpl_dir, name + '.tex')).read()
        # injeta shared templates no template alvo.
        self.content = reduce(lambda x, y : x.replace(y, _shd_tpl[y]),
                              _shd_tpl, self.content)

    def render(self, ctx):
        ctx['@HOJE'] = date_format('dd de MM de aaaa', date.today())

        # injeta dados no template e retorna tex pronto para ser compilado.
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
