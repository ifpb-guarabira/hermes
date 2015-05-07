#!/usr/bin/python
# -*- coding: utf-8 -*-
import hermes
import env

template = hermes.Template('declaracao_de_orientacao')

def cli():
    context = dict(env.context)
    context['@ALUNO']      = raw_input('Aluno(a): ')
    context['@ANO']        = raw_input('Ano: ')
    context['@ORIENTADOR'] = raw_input('Orientador(a): ')
    context['@SIAPE']      = raw_input('Matricula SIAPE: ')
    context['@CPF']        = raw_input('CPF: ')

    hermes.cli_builder(template, context, context['@ORIENTADOR'])

if __name__ == '__main__':
    cli()
