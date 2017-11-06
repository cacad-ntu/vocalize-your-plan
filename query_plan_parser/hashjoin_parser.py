#Hash Join Class

from query_plan_parser.parser import parse_plan

def hash_join_parser(sentence):
    result = 'The two table is joined with Hash Join'

    if 'Hash Cond' in sentence:
        result += ' on the condition' + sentence['Hash Cond'] + '.'
    elif 'Plans' in sentence:
        result += 'Then, '
        parse_plan(sentence['Plans'])
    else:
        result += '.'

    


