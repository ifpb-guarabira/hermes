#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from hermes import Hermes
from hermes import months

data = {}

data['@ALUNO']      = raw_input('Aluno(a): ')
data['@ANO']        = raw_input('Ano: ')
data['@ORIENTADOR'] = raw_input('Orientador(a): ')
data['@SIAPE']      = raw_input('Matricula SIAPE: ')
data['@CPF']        = raw_input('CPF: ')

Hermes('declaracao_de_orientacao').build(data, data['@ORIENTADOR'])
