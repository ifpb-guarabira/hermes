#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from hermes import Hermes
from hermes import months
from datetime import datetime
from subprocess import call
import os #Importo o modulo "os"
import sys

#Lista os arquivos e gera a numeração automatica do MEMO
diretorioDeMemo = '~/Dropbox/CTIN/Documentos/2015/MEMO'
arquivos = os.listdir(os.path.expanduser(diretorioDeMemo)  )
num = len(arquivos) # quantidade de arquivos na pasta 

numeroFormatado = ''
for align, text in zip('>', [str(num +1)]):
	numeroFormatado+='{0:{fill}{align}3}'.format(text, fill=align, align=align)
numeroFormatado = numeroFormatado.replace('>', '0')


data = {}

data['@NUMERO']   = str(numeroFormatado) + '/'+ '2015'
data['@DESTINO']  = raw_input('Setor de Destino: ')
data['@ASSUNTO']  = raw_input('Assunto: ')

arq = open('memo.txt', 'r')
texto = arq.read()
arq.close()

data['@TEXTO']  = texto

now        = datetime.now()
hoje       = '%s de %s de %s' % (now.day, months[now.month], now.year)

data['@HOJE']  = hoje

template = Hermes('memo')
template.build(data, data['@NUMERO'])
