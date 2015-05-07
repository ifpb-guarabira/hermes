#!/usr/bin/python
# -*- coding: utf-8 -*-
import hermes
import env

deferido = hermes.Template('canc_mat_disc_deferido')
indeferido = hermes.Template('canc_mat_disc_indeferido')

def cli():
    context = dict(env.context)
    context['@ALUNO']      = raw_input('Aluno: ')
    context['@MATRICULA']  = raw_input('Matricula: ')
    context['@DISCIPLINA'] = raw_input('Disciplina: ')
    context['@PROCESSO']   = raw_input('Processo (caso indeferido): ')

    template = indeferido if context['@PROCESSO'] else deferido

    hermes.cli_builder(template, context, context['@ALUNO'])

if __name__ == '__main__':
    cli()
