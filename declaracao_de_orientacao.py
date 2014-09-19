#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from subprocess import call

months = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

document   = 'declaracao_de_orientacao'
model      = open(document + '.tex', 'r').read().replace('@@@', '%s')
now        = datetime.now()
student    = raw_input('Aluno(a): ')
year       = raw_input('Ano: ')
mentor     = raw_input('Orientador(a): ')
siape_id   = raw_input('Matricula SIAPE: ')
social_no  = raw_input('CPF: ')
today      = '%s de %s de %s' % (now.day, months[now.month], now.year)
result     = model % (today, mentor, social_no, siape_id, student, year)

file_name  = document.replace('_', ' ')
file_name += ' - %d.%02d.%02d - ' % (now.year, now.month, now.day)
file_name += mentor

tex = open(file_name + '.tex', 'w')
tex.write(result)
tex.close()

call(['pdflatex', file_name + '.tex'])
call(['rm',       file_name + '.tex'])
call(['rm',       file_name + '.aux'])
call(['rm',       file_name + '.log'])
call(['mv',       file_name + '.pdf', str(now.year) + '/' + file_name + '.pdf'])
