"""
Parser for sort node type
https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
"""


import json
import query_plan_parser.parser

def sort_parser(plan):
    """initialize empty string"""
    result = ""

    """Get the text of it's child before if exists"""
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = query_plan_parser.parser.parse_plan(child)
            result += temp + " "

    """Parse the Sort"""
    if(plan["Node Type"] == "Sort"):
        if "DESC" in plan["Sort Key"]:
            result += "Then, the result is sort by using attribute " + str(plan["Sort Key"].replace('DESC','')) +" in desceding order."
        elif "INC" in plan["Sort Key"]:
            result += "Then, the result is sort by using attribute " + str(plan["Sort Key"].replace('INC','')) +" in increasing order."
        else:
            result += "Then, the result is sort by using attribute " + str(plan["Sort Key"])+ "."

    return result


if __name__ == "__main__":

    test = '''
   {                                             
         "Node Type": "Sort",               
           "Parent Relationship": "Outer",    
           "Parallel Aware": false,           
           "Startup Cost": 31061.74,          
           "Total Cost": 32518.24,            
           "Plan Rows": 582599,               
           "Plan Width": 100,                 
           "Sort Key": ["title"],             
           "Plans": [                         
             {                                
               "Node Type": "Seq Scan",       
               "Parent Relationship": "Outer",
               "Parallel Aware": false,       
               "Relation Name": "publication",
               "Alias": "publication",        
               "Startup Cost": 0.00,          
               "Total Cost": 15558.99,        
               "Plan Rows": 582599,           
               "Plan Width": 100              
             }                                
           ]           
     }
    '''
    test_plan = json.loads(test)
    print(sort_parser(test_plan))