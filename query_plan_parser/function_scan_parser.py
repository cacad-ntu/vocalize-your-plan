"""
File to parse node type function scan
https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
"""

import json
import query_plan_parser.parser

def function_scan_parser(plan, start=False):
    """ Parser for Function Scan node type """
    parsed_plan = query_plan_parser.parser.get_conjuction(start)
    parsed_plan += "it runs the function " + plan["Function Name"]
    parsed_plan += " and returns the recordset created by it."
    return parsed_plan


if __name__ == "__main__":
    PLAN = '''
    {                                    
        "Node Type": "Function Scan",      
        "Parent Relationship": "Outer",    
        "Parallel Aware": false,           
        "Function Name": "generate_series",
        "Alias": "i",                      
        "Startup Cost": 0.00,              
        "Total Cost": 12.50,               
        "Plan Rows": 1000,                 
        "Plan Width": 8                    
    }                                                                         
    '''
    JSON_PLAN = json.loads(PLAN)
    print(function_scan_parser(JSON_PLAN, start=True))
