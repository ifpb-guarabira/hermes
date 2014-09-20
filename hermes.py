# -*- coding: utf-8 -*-
from datetime import datetime
from subprocess import call

months = ['', \
    'Janeiro',  'Fevereiro', 'Março',    'Abril',  \
    'Maio',     'Junho',     'Julho',    'Agosto', \
    'Setembro', 'Outubro',   'Novembro', 'Dezembro']

class Hermes:
    def __init__(self, template):
        now = datetime.now()
        
        self.template  = open('tex/%s.tex' % template, 'r').read()
        self.today     = '%s de %s de %s' % (now.day, months[now.month], now.year)
        self.output    = template + ' - %d.%02d.%02d - ' % (now.year, now.month, now.day)
    
    
    def build(self, data, sufix):
        file_name = self.output + sufix
        
        result = self.template.replace('@HOJE', self.today)
        
        for key in data.keys():
            result = result.replace(key, data[key])

        tex = open(file_name + '.tex', 'w')
        tex.write(result)
        tex.close()

        call(['pdflatex', file_name + '.tex'])
        call(['rm',       file_name + '.tex'])
        call(['rm',       file_name + '.aux'])
        call(['rm',       file_name + '.log'])
        call(['mv',       file_name + '.pdf', self.today[-4:] + '/' + file_name + '.pdf'])
    
