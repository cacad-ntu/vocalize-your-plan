"""
http://www.postgresql-archive.org/Query-plan-for-Merge-Semi-Join-td5990041.html
"""

import query_plan_parser.parser
import json

def merge_join_parser(sentence):
    result = ''

    if 'Plans' in sentence:
        for child in sentence['Plans']:
            result += query_plan_parser.parser.parse_plan(child)

    result += ' the result from previous operation is joined with Hash Join'

    if 'Merge Cond' in sentence:
        result += ' with condition ' + sentence['Merge Cond']

    if 'Join Type' == 'Semi':
        result += ' but only the row from the left relation is returned.'
    else:
        result += '.'

    return result



