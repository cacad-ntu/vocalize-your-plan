"""
File to parse node type function scan
"""
# https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/

import json

def function_scan_parser(plan):
    """Parser for Function Scan node type"""
    parsed_plan = "It runs the function " + plan["Function Name"]
    parsed_plan += " and returns the recordset created by it."
    return parsed_plan

if __name__ == "__main__":
    test = '''                        
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
    test_plan = json.loads(test)
    print(function_scan_parser(test_plan))