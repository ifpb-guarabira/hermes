#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from subprocess import call

months = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

model      = open('tex/justificativa_de_falta.tex', 'r').read().replace('@@@', '%s')
now        = datetime.now()
today      = '%s de %s de %s' % (now.day, months[now.month].upper(), now.year)
student    = raw_input('Nome do aluno: ')
year       = raw_input('Turma: ')
dd, mm, yy = raw_input('Data do atestado: ').split('/')
days       = int(raw_input('Duração (dias): '))
license    = '%s/%s/%s' % (dd, mm, yy)

if days > 1:
    end      = datetime(int(yy), int(mm), int(dd))
    end     += timedelta(days=days - 1)
    license += ' à %02d/%02d/%04d' % (end.day, end.month, end.year)

result     = model % (today, student, student, year, license)
file_name  = 'justificativa de falta - %d.%02d.%02d - %s' % (now.year, now.month, now.day, student)
tex = open(file_name + '.tex', 'w')
tex.write(result)
tex.close()

call(['pdflatex', file_name + '.tex'])
call(['rm',       file_name + '.tex'])
call(['rm',       file_name + '.aux'])
call(['rm',       file_name + '.log'])
call(['mv',       file_name + '.pdf', str(now.year) + '/' + file_name + '.pdf'])
