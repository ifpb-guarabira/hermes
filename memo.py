#!/usr/bin/python
# -*- coding: utf-8 -*-
import hermes
import env

template = hermes.Template('memo')

def cli():
    context = dict(env.context)
    context['@NUMERO']  = raw_input('Número (ex. 001/2015): ')
    context['@DESTINO'] = raw_input('Setor de Destino: ')
    context['@ASSUNTO'] = raw_input('Assunto: ')
    context['@TEXTO']   = open(raw_input('Corpo (arquivo): ')).read()

    hermes.cli_builder(template, context, context['@NUMERO'].replace('/', '_'))

if __name__ == '__main__':
    cli()
