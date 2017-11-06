#Hash Join Class

import query_plan_parser.parser

def hash_join_parser(sentence):
    result = 'The two table is joined with Hash Join'

    if 'Hash Cond' in sentence:
        result += ' on the condition' + sentence['Hash Cond'] + '.'
    if 'Plans' in sentence:
        result += 'Then, '
        for child in sentence['Plans']:
            result += query_plan_parser.parser.parse_plan(child) + " "
    else:
        result += '.'
    
    return result

    


