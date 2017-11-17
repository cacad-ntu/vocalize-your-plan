"""
Parser for materialize node type
https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
"""

import json
import query_plan_parser.parser

def materialize_parser(plan, start=False):
    """ Materialize parser """
    result = ""

    # Get the text of it's child before if exists
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = query_plan_parser.parser.parse_plan(child, start)
            result += temp + " "
            if start:
                start = False

    #Parse the materialize
    if plan["Node Type"] == "Materialize":
        result += query_plan_parser.parser.get_conjuction(start)
        result += "the results are stored in memory for faster access. "

    return result

if __name__ == "__main__":
    test = '''
    {                                             
        "Node Type": "Materialize",                                        
        "Parent Relationship": "Inner",                                    
        "Parallel Aware": false,                                           
        "Startup Cost": 19215.45,                                          
        "Total Cost": 19223.67,                                            
        "Plan Rows": 274,                                                  
        "Plan Width": 15,                                                  
        "Plans": [                                                         
            {                                                                
                "Node Type": "Unrecognize",                                      
                "Strategy": "Sorted",                                          
                "Partial Mode": "Simple",                                      
                "Parent Relationship": "Outer",                                
                "Parallel Aware": false,                                       
                "Startup Cost": 19215.45,                                      
                "Total Cost": 19220.25,                                        
                "Plan Rows": 274,                                              
                "Plan Width": 23,                                              
                "Group Key": ["a_1.author"],                                   
                "Filter": "(count(a_1.author) >= 10)"                        
            }
        ]
    }
    '''
    test_plan = json.loads(test)
    print(materialize_parser(test_plan, start=True))