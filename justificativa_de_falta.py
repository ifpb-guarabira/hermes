#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from hermes import Hermes
from hermes import months

data = {}

data['@ALUNO']   = raw_input('Aluno: ')
data['@ANO']     = raw_input('Turma: ')
dd, mm, yy       = raw_input('Data do atestado: ').split('/')
days             = int(raw_input('Duração (dias): '))
data['@PERIODO'] = '%s/%s/%s' % (dd, mm, yy)

if days > 1:
    end  = datetime(int(yy), int(mm), int(dd))
    end += timedelta(days=days - 1)

    data['@PERIODO'] += ' à %02d/%02d/%04d' % (end.day, end.month, end.year)

Hermes('justificativa_de_falta').build(data, data['@ALUNO'])
Hermes('comunicado_justificativa_de_falta').build(data, data['@ALUNO'])
