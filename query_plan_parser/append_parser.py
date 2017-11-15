"""
Parser for append node type
https://www.depesz.com/2013/05/19/explaining-the-unexplainable-part-4/
"""

import query_plan_parser.parser
import json

def append_parser(plan):
    """initialize empty string"""
    result = ""

    """Get the text of it's child before if exists"""
    
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = query_plan_parser.parser.parse_plan(child)
            result += temp + " "
    


    """Parse the values scan"""
    if(plan["Node Type"] == "Append"):
        result += "Then, it returns all the scan result as one resultset."

    return result

if __name__ == "__main__":
    test = '''
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
    test_plan = json.loads(test)
    print(append_parser(test_plan))