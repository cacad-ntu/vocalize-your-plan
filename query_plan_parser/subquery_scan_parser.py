"""
Subquery scan parser
"""

import json
import query_plan_parser.parser

def subquery_scan_parser(plan, start=False):
    """ Subquery scan parser """
    result = ''

    if 'Plans' in plan:
        for child in plan['Plans']:
            result += query_plan_parser.parser.parse_plan(child, start) + " "
            if start:
                start = False

    result += query_plan_parser.parser.get_conjuction(start)
    result += 'Subquery Scan is performed on the result from the previous operations and output it without any changes '
    result += '(the purpose of Subquery scan is mainly for internal bookkeeping).'

    return result

if __name__ == "__main__":
    test = '''
    {                                                   
        "Node Type": "Subquery Scan",                                     
        "Parent Relationship": "Outer",                                   
        "Parallel Aware": false,                                          
        "Alias": "tmp_a",                                                 
        "Startup Cost": 48103.23,                                         
        "Total Cost": 48113.40,                                           
        "Plan Rows": 170,                                                 
        "Plan Width": 15,                                                 
        "Filter": "(NOT (hashed SubPlan 1))",
        "Plans":[
            {
                "Node Type": "Another Operation"
            }
        ]
    }
    '''
    test_plan = json.loads(test)
    print(subquery_scan_parser(test_plan, start=True))
