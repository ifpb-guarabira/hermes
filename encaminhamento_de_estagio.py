#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from hermes import Hermes
from hermes import months

student    = raw_input('Aluno: ')
enrollment = raw_input('Matricula: ')
dd, mm, yy = raw_input('Data de Conclusão: ').split('/')

template = Hermes('encaminhamento_de_estagio')
data = {'@ALUNO' : student, '@MATRICULA' : enrollment, \
        '@CONCLUSÃO' : '%s de %s de %s' % (dd, months[int(mm)], yy)}

template.build(data, student)
