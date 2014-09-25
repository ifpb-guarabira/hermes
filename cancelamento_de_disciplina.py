#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from hermes import Hermes
from hermes import months

template = Hermes('cancelamento_de_disciplina')
data = {}

data['@ALUNO']      = raw_input('Aluno: ')
data['@MATRICULA']  = raw_input('Matricula: ')
data['@DISCIPLINA'] = raw_input('Disciplina: ')

template.build(data, data['@ALUNO'])
