#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from hermes import Hermes
from datetime import datetime
from hermes import months

student    = raw_input('Aluno: ')
processo = raw_input('Processo: ')
enrollment = raw_input('Matricula: ')
disciplina = raw_input('Disciplina: ')
now        = datetime.now()
hoje       = '%s de %s de %s' % (now.day, months[now.month], now.year)


template = Hermes('parecer_cancelamento')
data = {'@ALUNO' : student, '@DISCIPLINA' : disciplina, '@MATRICULA' : enrollment, \
        '@HOJE' : hoje, '@PROCESSO': processo}

template.build(data, student)
