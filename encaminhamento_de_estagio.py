#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from hermes import Hermes
from hermes import months

data = {}

data['@ALUNO']      = raw_input('Aluno: ')
data['@MATRICULA']  = raw_input('Matricula: ')
dd, mm, yy          = raw_input('Data de Conclusão: ').split('/')
data['@CONCLUSÃO']  = '%s de %s de %s' % (dd, months[int(mm)], yy)

Hermes('encaminhamento_de_estagio').build(data, data['@ALUNO'])
