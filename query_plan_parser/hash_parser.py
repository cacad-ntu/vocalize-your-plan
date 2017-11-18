"""
File to parse node type hash
https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
"""

import json
import query_plan_parser.parser

def hash_parser(plan, start=False):
    """Parser for Hash node type"""

    if "Plans" in plan:
        sentence = query_plan_parser.parser.parse_plan(plan['Plans'][0], start)
        sentence += " The hash function makes a memory hash with rows from the source."
    else:
        sentence = query_plan_parser.parser.get_conjuction(start)
        sentence += "the hash function makes a memory hash with rows from the source."

    return sentence

if __name__ == "__main__":
    PLAN = '''
    {                                                    
        "Node Type": "Hash",                               
        "Parent Relationship": "Inner",                    
        "Parallel Aware": false,                           
        "Startup Cost": 16963.36,                          
        "Total Cost": 16963.36,                            
        "Plan Rows": 35630,                                
        "Plan Width": 22,                                  
        "Plans": [                                         
            {                                                
                "Node Type": "Seq Scan",                       
                "Parent Relationship": "Outer",                
                "Parallel Aware": false,                       
                "Relation Name": "publication",                
                "Alias": "b",                                  
                "Startup Cost": 0.00,                          
                "Total Cost": 16963.36,                        
                "Plan Rows": 35630,                            
                "Plan Width": 22,                              
                "Filter": "(year = 2017)"                      
            }                                                
        ]                                                  
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(hash_parser(JSON_PLAN, start=True))
