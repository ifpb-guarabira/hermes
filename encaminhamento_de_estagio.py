# -*- coding: utf-8 -*-
from datetime import datetime
from subprocess import call

months = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

model      = open('encaminhamento_de_estagio.tex', 'r').read().replace('@@@', '%s')
now        = datetime.now()
student    = raw_input('Aluno: ')
enrollment = raw_input('Matricula: ')
dd, mm, aa = raw_input('Data de Conclusão: ').split('/')
date       = '%s de %s de %s' % (dd, months[int(mm)], aa)
result     = model % (date, student, enrollment, date, date)
file_name  = 'encaminhamento de estagio - %d.%02d.%02d - %s' % (now.year, now.month, now.day, student)
tex = open(file_name + '.tex', 'w')
tex.write(result)
tex.close()

call(['pdflatex', file_name + '.tex'])
call(['rm',       file_name + '.tex'])
call(['rm',       file_name + '.aux'])
call(['rm',       file_name + '.log'])
call(['mv',       file_name + '.pdf', str(now.year) + '/' + file_name + '.pdf'])
