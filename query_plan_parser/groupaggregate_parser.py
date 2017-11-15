"""
Parser for GroupAggregate node type
"""

import json
import query_plan_parser.parser

def group_aggregate_parser(plan):
    """ Parser for GroupAggregate node type """
    parsed_plan = query_plan_parser.parser.parse_plan(plan["Plans"][0])
    parsed_plan += " the result is grouped by " 
    for group_key in plan["Group Key"]:
        parsed_plan += group_key.replace("::text", "") + ", "
    parsed_plan = parsed_plan[:-2]
    if "Filter" in plan:
        parsed_plan += " then bounded with condition " + plan["Filter"].replace("::text", "")
    parsed_plan += "."
    return parsed_plan

if __name__ == "__main__":
    PLAN = '''
    {                                                        
       "Node Type": "Aggregate",                                      
       "Strategy": "Sorted",                                          
       "Partial Mode": "Simple",                                      
       "Parallel Aware": false,                                       
       "Startup Cost": 513461.61,                                     
       "Total Cost": 519210.47,                                       
       "Plan Rows": 220200,                                           
       "Plan Width": 15,                                              
       "Group Key": ["a.author", "something else"],                                     
       "Filter": "(count(a.author) > 20)",
       "Plans": [                                         
            {                                                
            "Node Type": "Seq Scan",                       
            "Parent Relationship": "Outer",                
            "Parallel Aware": false,                       
            "Relation Name": "publication",                
            "Alias": "a",                                  
            "Startup Cost": 0.00,                          
            "Total Cost": 102857.50,                       
            "Plan Rows": 164431,                           
            "Plan Width": 23,                              
            "Filter": "(year = 2017)"                      
            }                                                
        ]
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(group_aggregate_parser(JSON_PLAN))
