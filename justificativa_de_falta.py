#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import hermes
import env
import sys

comunicado = hermes.Template('justificativa_de_falta_comunicado')
parecer    = hermes.Template('justificativa_de_falta_parecer')

def build(studdent, year, date, days):
    context = dict(env.context)
    context['@ALUNO']     = studdent
    context['@ANO']       = year
    dd, mm, yy            = date.split('/') if '/' in date else \
                            date.split('-') if '-' in date else \
                            (date[0:2], date[2:4], date[4:])
    days                  = int(days)
    context['@PERIODO']   = '%s/%s/%s' % (dd, mm, yy)
    context['@DIA']       = '_%s_%s_%s_' % (yy, mm, dd)

    if len(yy) < 4:
        yy = '20' + yy

    if days > 1:
        end  = datetime(int(yy), int(mm), int(dd))
        end += timedelta(days=days - 1)

        context['@PERIODO'] += ' à %02d/%02d/%04d' % (end.day, end.month, end.year)

    # hermes.cli_builder(comunicado, context, context['@ALUNO'])
    hermes.cli_builder(parecer, context, context['@ALUNO'])

def cli():
    build(raw_input('Aluno: '),
          raw_input('Turma: '),
          raw_input('Data do atestado: '),
          raw_input('Duração (dias): '))

if __name__ == '__main__':
    try:
        build(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    except:
        cli()
