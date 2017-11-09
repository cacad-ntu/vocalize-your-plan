"""
File to parse node type HashAggregate
"""

import json
import query_plan_parser.parser

def hash_aggregate_parser(plan):
    """Parser for HashAggregate node type"""
    parsed_plan = query_plan_parser.parser.parse_plan(plan["Plans"][0])
    if len(plan["Group Key"]) == 1:
        sentence = "It hashes all the rows based on the key " + plan["Group Key"]
    else:
        sentence = "It hashes all the rows based on the keys "
        for i in plan["Group Key"]:
            sentence += i + ", "
    sentence += "then scans all rows at first then return the desired row after manipulation."
    parsed_plan = sentence + parsed_plan
    return parsed_plan

if __name__ == "__main__":
    test = '''
    {                                                   
       "Node Type": "Aggregate",                                 
       "Strategy": "Hashed",                                     
       "Partial Mode": "Simple",                                 
       "Parallel Aware": false,                                  
       "Startup Cost": 40297.34,                                 
       "Total Cost": 40494.72,                                   
       "Plan Rows": 19738,                                       
       "Plan Width": 23,                                       
       "Group Key": ["b.author"],                              
       "Plans": [                                                
        {                                                       
           "Node Type": "Nested Loop",                           
           "Parent Relationship": "Outer",                       
           "Parallel Aware": false,                              
           "Join Type": "Inner",                                 
           "Startup Cost": 16963.82,                             
           "Total Cost": 40198.65,                               
           "Plan Rows": 19738,                                   
           "Plan Width": 15
        }
        ]
    }
    '''
    test_plan = json.loads(test)
    print(hash_aggregate_parser(test_plan))
    