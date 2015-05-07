#!/usr/bin/python
# -*- coding: utf-8 -*-
import hermes
import env

template = hermes.Template('encaminhamento_de_estagio')

def cli():
    context = dict(env.context)
    context['@ALUNO']     = raw_input('Aluno: ')
    context['@MATRICULA'] = raw_input('Matricula: ')
    dd, mm, yy            = raw_input('Data de Conclusão: ').split('/')
    context['@CONCLUSÃO'] = '%s de %s de %s' % (dd, hermes.months[int(mm)], yy)

    hermes.cli_builder(template, context, context['@ALUNO'])

if __name__ == '__main__':
    cli()
