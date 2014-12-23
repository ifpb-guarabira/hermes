#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from hermes import Hermes
from hermes import months

data = {}

<<<<<<< HEAD
model      = open('tex/justificativa_de_falta.tex', 'r').read().replace('@@@', '%s')
now        = datetime.now()
today      = '%s de %s de %s' % (now.day, months[now.month].upper(), now.year)
student    = raw_input('Nome do aluno: ')
year       = raw_input('Turma: ')
dd, mm, yy = raw_input('Data do atestado: ').split('/')
days       = int(raw_input('Duração (dias): '))
license    = '%s/%s/%s' % (dd, mm, yy)
=======
data['@ALUNO']   = raw_input('Aluno: ')
data['@ANO']     = raw_input('Turma: ')
dd, mm, yy       = raw_input('Data do atestado: ').split('/')
days             = int(raw_input('Duração (dias): '))
data['@PERIODO'] = '%s/%s/%s' % (dd, mm, yy)
>>>>>>> 20bc99db544afab2ef68ae452918f499e5056b4f

if days > 1:
    end  = datetime(int(yy), int(mm), int(dd))
    end += timedelta(days=days - 1)

    data['@PERIODO'] += ' à %02d/%02d/%04d' % (end.day, end.month, end.year)

Hermes('justificativa_de_falta').build(data, data['@ALUNO'])
Hermes('comunicado_justificativa_de_falta').build(data, data['@ALUNO'])
