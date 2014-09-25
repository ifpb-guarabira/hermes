#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from hermes import Hermes
from hermes import months

data = {}

data['@ALUNO']      = raw_input('Aluno: ')
data['@MATRICULA']  = raw_input('Matricula: ')
data['@DISCIPLINA'] = raw_input('Disciplina: ')

Hermes('cancelamento_de_disciplina').build(data, data['@ALUNO'])
