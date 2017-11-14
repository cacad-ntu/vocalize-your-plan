"""

"""

import query_plan_parser.parser
import json

def subquery_scan_parser(sentence):
    result = ''

    if 'Plans' in sentence:
        for child in sentence['Plans']:
            result += query_plan_parser.parser.parse_plan(child)

    result += ' the Subquery Scan process the result from the previous operations and output it without any changes. The purpose of Subquery scan is mainly for internal bookkeeping.'
      
    return result