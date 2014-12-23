#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from hermes import Hermes
from hermes import months

<<<<<<< HEAD
def gen(aluno, matricula, disciplina):
	months = ['', 'Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

	model      = open('tex/cancelamento_de_disciplina.tex', 'r').read().replace('@@@', '%s')
	now        = datetime.now()
	student    = aluno
	enrollment = matricula
	course     = disciplina
	today      = '%s de %s de %s' % (now.day, months[now.month], now.year)
	result     = model % (today, student, enrollment, course)
	file_name  = 'cancelamento de matricula em disciplina opcional - %d.%02d.%02d - %s' % (now.year, now.month, now.day, student)
	tex = open(file_name + '.tex', 'w')
	tex.write(result)
	tex.close()

	call(['pdflatex', file_name + '.tex'])
	call(['rm',       file_name + '.tex'])
	call(['rm',       file_name + '.aux'])
	call(['rm',       file_name + '.log'])
	call(['mv',       file_name + '.pdf', str(now.year) + '/' + file_name + '.pdf'])

	return file_name + '.pdf'

# gen('test', 'test', 'test')
=======
data = {}

data['@ALUNO']      = raw_input('Aluno: ')
data['@MATRICULA']  = raw_input('Matricula: ')
data['@DISCIPLINA'] = raw_input('Disciplina: ')

Hermes('cancelamento_de_disciplina').build(data, data['@ALUNO'])
>>>>>>> 20bc99db544afab2ef68ae452918f499e5056b4f
