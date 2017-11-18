"""
Parser for nested loop node type
https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
"""

import json
import query_plan_parser.parser

def nested_loop_parser(plan, start=False):
    """ Nested Loop Parser """
    result = ""

    # Get the text of it's child
    temp = query_plan_parser.parser.parse_plan(plan["Plans"][0], start)
    result += temp + " "
    temp = query_plan_parser.parser.parse_plan(plan["Plans"][1])
    result += temp + " "


    # Parse the nested loop
    result += "Then, the join result between both scan results are returned as new rows."

    return result


if __name__ == "__main__":
    PLAN = '''
    {                                             
        "Node Type": "Nested Loop",                                      
        "Parallel Aware": false,                                         
        "Join Type": "Inner",                                            
        "Startup Cost": 0.42,                                            
        "Total Cost": 27931.81,                                          
        "Plan Rows": 1,                                                  
        "Plan Width": 100,                                               
        "Plans": [                                                       
            {                                                              
                "Node Type": "Seq Scan",                                     
                "Parent Relationship": "Outer",                              
                "Parallel Aware": false,                                     
                "Relation Name": "pub_auth",                                 
                "Alias": "pub_auth",                                         
                "Startup Cost": 0.00,                                        
                "Total Cost": 27889.54,                                      
                "Plan Rows": 5,                                              
                "Plan Width": 23,                                            
                "Filter": "((author)::text = 'Hongli Xu'::text)"             
            },                                                             
            {                                                              
                "Node Type": "Index Scan",                                   
                "Parent Relationship": "Inner",                              
                "Parallel Aware": false,                                     
                "Scan Direction": "Forward",                                 
                "Index Name": "publication_pkey",                            
                "Relation Name": "publication",                              
                "Alias": "publication",                                      
                "Startup Cost": 0.42,                                        
                "Total Cost": 8.45,                                          
                "Plan Rows": 1,                                              
                "Plan Width": 100,                                           
                "Index Cond": "((pub_key)::text = (pub_auth.pub_key)::text)",
                "Filter": "(year = 2015)"                                    
            }                                                              
        ]                                                                
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(nested_loop_parser(JSON_PLAN, start=True))
