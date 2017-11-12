"""
File to parse node type hash
"""
# https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/

import query_plan_parser.parser
import json

def hash_parser(plan):
    """Parser for Hash node type"""
    if "Plans" in plan:
        sentence = query_plan_parser.parser.parse_plan(plan['Plans'][0])
        sentence += " The hash function makes a memory hash with rows from the source."
    else:
        sentence = " The hash function makes a memory hash with rows from the source."

    return sentence

if __name__ == "__main__":
    test = '''
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
    test_plan = json.loads(test)
    print(hash_parser(test_plan))