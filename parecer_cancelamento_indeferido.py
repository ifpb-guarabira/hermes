#!/usr/bin/python
# -*- coding: utf-8 -*-
import hermes
import env

template = hermes.Template('parecer_cancelamento_indeferido')

def cli():
    context = dict(env.context)
    context['@ALUNO']      = raw_input('Aluno: ')
    context['@PROCESSO']   = raw_input('Processo: ')
    context['@MATRICULA']  = raw_input('Matricula: ')
    context['@DISCIPLINA'] = raw_input('Disciplina: ')

    hermes.cli_builder(template, context, context['@ALUNO'])

if __name__ == '__main__':
    cli()
