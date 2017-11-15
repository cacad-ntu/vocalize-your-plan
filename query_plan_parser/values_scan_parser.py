"""
Parser for values scan node type
https://www.depesz.com/2013/05/19/explaining-the-unexplainable-part-4/
"""

import query_plan_parser.parser
import json

def values_scan_parser(plan):
    """initialize empty string"""
    result = ""

    """Get the text of it's child before if exists"""
    """
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = query_plan_parser.parser.parse_plan(child)
            result += temp + " "
    """


    """Parse the values scan"""
    if(plan["Node Type"] == "Values Scan"):
        result += "It does a scan through the given values from the query."

    return result

if __name__ == "__main__":

    test = '''
   {                                             
        "Node Type": "Values Scan",
        "Parallel Aware": false,   
        "Alias": "*VALUES*",       
        "Startup Cost": 0.00,      
        "Total Cost": 0.04,        
        "Plan Rows": 3,            
        "Plan Width": 36           
     }
    '''
    test_plan = json.loads(test)
    print(values_scan_parser(test_plan))