#!/usr/bin/python
# -*- coding: utf-8 -*-
import hermes
from util import months
        
def main():
    data = {}

    data['@ALUNO']     = raw_input('Aluno: ')
    data['@MATRICULA'] = raw_input('Matricula: ')
    dd, mm, yy         = raw_input('Data de Conclusão: ').split('/')
    data['@CONCLUSÃO'] = '%s de %s de %s' % (dd, months[int(mm)], yy)

    builder = hermes.Builder(hermes.Template('encaminhamento_de_estagio'), data)

    builder.build(data['@ALUNO'].lower())
    
if __name__ == "__main__":
    main()