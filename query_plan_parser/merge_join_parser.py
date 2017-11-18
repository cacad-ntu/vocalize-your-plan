"""
Merge Join parser
http://www.postgresql-archive.org/Query-plan-for-Merge-Semi-Join-td5990041.html
"""

import json
import query_plan_parser.parser

def merge_join_parser(plan, start=False):
    """ Merge Join parser """
    result = ''

    if 'Plans' in plan:
        for child in plan['Plans']:
            result += query_plan_parser.parser.parse_plan(child, start) + " "
            if start:
                start = False

    result += query_plan_parser.parser.get_conjuction(start)
    result += 'the result from previous operation is joined using Merge Join'

    if 'Merge Cond' in plan:
        result += ' with condition ' + plan['Merge Cond'].replace("::text", "")

    if 'Join Type' == 'Semi':
        result += ' but only the row from the left relation is returned.'
    else:
        result += '.'

    return result


if __name__ == "__main__":
    PLAN = '''
    {                                                   
        "Node Type": "Merge Join",                                             
        "Parent Relationship": "Outer",                                        
        "Parallel Aware": false,                                               
        "Join Type": "Inner",                                                  
        "Startup Cost": 48100.69,                                              
        "Total Cost": 48128.80,                                                
        "Plan Rows": 575,                                                      
        "Plan Width": 15,                                                      
        "Merge Cond": "((a.author)::text = (a_1.author)::text)",
        "Plans" :[
            {
                "Node Type": "Unrecognize"
            }
        ]
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(merge_join_parser(JSON_PLAN, start=True))
