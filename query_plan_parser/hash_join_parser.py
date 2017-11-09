import query_plan_parser.parser

def hash_join_parser(sentence):
    result = ''

    if 'Plans' in sentence:
        for child in sentence['Plans']:
            result += query_plan_parser.parser.parse_plan(child)

    result += ' the result from previous operation is joined with Hash Join'
    
    if 'Hash Cond' in sentence:
        result += ' with condition ' + sentence['Hash Cond'] + '.'
    else:
        result += '.'
    
    return result
