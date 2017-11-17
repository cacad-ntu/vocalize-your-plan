"""
Parser for values scan node type
https://www.depesz.com/2013/05/19/explaining-the-unexplainable-part-4/
"""

import json
import query_plan_parser.parser

def values_scan_parser(plan, start=False):
    """ Value Scan Parser """
    result = query_plan_parser.parser.get_conjuction(start)
    result += "it does a scan through the given values from the query."

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
    print(values_scan_parser(test_plan, start=True))
    