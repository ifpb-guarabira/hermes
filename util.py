# -*- coding: utf-8 -*-

# meses do ano em português.
months = ['', 'Janeiro',  'Fevereiro', 'Março',    'Abril',
              'Maio',     'Junho',     'Julho',    'Agosto',
              'Setembro', 'Outubro',   'Novembro', 'Dezembro']

def date_format(fmt, date):
    fmt = fmt.replace('aaaa', '%04d' % date.year)
    fmt = fmt.replace('aa',   '%02d' % date.year)
    fmt = fmt.replace('MM',   months[date.month])
    fmt = fmt.replace('mm',   '%02d' % date.month)
    fmt = fmt.replace('dd',   '%02d' % date.day)
    
    return fmt
