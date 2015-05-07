#!/usr/bin/python
# -*- coding: utf-8 -*-
import hermes
import env

template = hermes.Template('cancelamento_de_disciplina')

def cli():
    context = dict(env.context)
    context['@ALUNO']      = raw_input('Aluno: ')
    context['@MATRICULA']  = raw_input('Matricula: ')
    context['@DISCIPLINA'] = raw_input('Disciplina: ')

    hermes.cli_builder(template, context, context['@ALUNO'])

if __name__ == '__main__':
    cli()
