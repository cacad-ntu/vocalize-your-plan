"""
Parser for append node type
https://www.depesz.com/2013/05/19/explaining-the-unexplainable-part-4/
"""

import json
import query_plan_parser.parser

def append_parser(plan, start=False):
    """ Append Parser """
    result = ""

    # Get the text of it's child before if exists
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = query_plan_parser.parser.parse_plan(child, start)
            if start:
                start = False
            result += temp + " "

    #Parse the values scan
    if plan["Node Type"] == "Append":
        result += query_plan_parser.parser.get_conjuction(start)
        result += "all of the scan results is combined as one resultset."

    return result


if __name__ == "__main__":
    PLAN = '''
    {                             
       "Node Type": "Append",              
       "Parallel Aware": false,            
       "Startup Cost": 0.00,               
       "Total Cost": 40150.02,             
       "Plan Rows": 1902002,               
       "Plan Width": 22,                   
       "Plans": [                          
            {                                 
                "Node Type": "Seq Scan",        
                "Parent Relationship": "Member",
                "Parallel Aware": false,        
                "Relation Name": "publication", 
                "Alias": "publication",         
                "Startup Cost": 0.00,           
                "Total Cost": 15558.99,         
                "Plan Rows": 582599,            
                "Plan Width": 21                
            },                                
            {                                 
                "Node Type": "Seq Scan",        
                "Parent Relationship": "Member",
                "Parallel Aware": false,        
                "Relation Name": "pub_auth",    
                "Alias": "pub_auth",            
                "Startup Cost": 0.00,           
                "Total Cost": 24591.03,         
                "Plan Rows": 1319403,           
                "Plan Width": 23                
            }                                 
        ]                                   
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(append_parser(JSON_PLAN, start=True))
