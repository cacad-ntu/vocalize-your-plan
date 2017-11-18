"""
Parser for sort node type
https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
"""

import json
import query_plan_parser.parser

def sort_parser(plan, start=False):
    """ Sort Parser """
    result = ""

    # Get the text of it's child before if exists
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = query_plan_parser.parser.parse_plan(child, start)
            result += temp + " "
            if start:
                start = False

    # Parse the Sort
    if plan["Node Type"] == "Sort":
        result += query_plan_parser.parser.get_conjuction(start)
        result += "the result is sorted by using attribute "
        if "DESC" in plan["Sort Key"]:
            result += str(plan["Sort Key"].replace('DESC', '')) +" in desceding order."
        elif "INC" in plan["Sort Key"]:
            result += str(plan["Sort Key"].replace('INC', '')) +" in increasing order."
        else:
            result += str(plan["Sort Key"])+ "."

    return result


if __name__ == "__main__":
    PLAN = '''
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
    JSON_PLAN = json.loads(PLAN)
    print(sort_parser(JSON_PLAN, start=True))
