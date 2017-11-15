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
        "Filter": "(NOT (hashed SubPlan 1))"
    }
    '''
    test_plan = json.loads(test)
    print(subquery_scan_parser(test_plan))