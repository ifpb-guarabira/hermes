#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import hermes
import env

comunicado = hermes.Template('justificativa_de_falta_comunicado')
parecer    = hermes.Template('justificativa_de_falta_parecer')

def cli():
    context = dict(env.context)
    context['@ALUNO']     = raw_input('Aluno: ')
    context['@ANO']       = raw_input('Turma: ')
    dd, mm, yy            = raw_input('Data do atestado: ').split('/')
    days                  = int(raw_input('Duração (dias): '))
    context['@PERIODO']   = '%s/%s/%s' % (dd, mm, yy)

    if days > 1:
        end  = datetime(int(yy), int(mm), int(dd))
        end += timedelta(days=days - 1)

        context['@PERIODO'] += ' à %02d/%02d/%04d' % (end.day, end.month, end.year)

    hermes.cli_builder(comunicado, context, context['@ALUNO'])
    hermes.cli_builder(parecer, context, context['@ALUNO'])

if __name__ == '__main__':
    cli()
