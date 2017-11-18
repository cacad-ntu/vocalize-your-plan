"""
Hash Join parser
"""

import json
import query_plan_parser.parser

def hash_join_parser(plan, start=False):
    """ Hash join parser """
    result = ""

    result += query_plan_parser.parser.parse_plan(plan["Plans"][1], start) + " "
    result += query_plan_parser.parser.parse_plan(plan["Plans"][0]) + " "

    result += "The result from previous operation is joined using Hash "
    result += plan["Join Type"] + " Join"
    if 'Hash Cond' in plan:
        result += ' with condition ' + plan['Hash Cond'].replace("::text", "") + '.'
    else:
        result += '.'

    return result


if __name__ == "__main__":
    PLAN = '''
    {                                                   
        "Node Type": "Hash Join",                        
        "Parent Relationship": "Outer",                   
        "Parallel Aware": false,                          
        "Join Type": "Semi",                              
        "Startup Cost": 16963.39,                         
        "Total Cost": 34094.11,                           
        "Plan Rows": 8582,                                
        "Plan Width": 22,                                 
        "Hash Cond": "(a.year = (min(publication.year)))",
        "Plans": [                                        
            {                                               
                "Node Type": "Seq Scan",                      
                "Parent Relationship": "Outer",               
                "Parallel Aware": false,                      
                "Relation Name": "publication",               
                "Alias": "a",                                 
                "Startup Cost": 0.00,                         
                "Total Cost": 15525.89,                       
                "Plan Rows": 574989,                          
                "Plan Width": 26                              
            },                                              
            {                                               
                "Node Type": "Hash",                          
                "Parent Relationship": "Inner",               
                "Parallel Aware": false,                      
                "Startup Cost": 16963.38,                     
                "Total Cost": 16963.38,                       
                "Plan Rows": 1,                               
                "Plan Width": 4
            }
        ]
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(hash_join_parser(JSON_PLAN, start=True))

    JSON_PLAN["Join Type"] = "Inner"
    print(hash_join_parser(JSON_PLAN, start=True))
