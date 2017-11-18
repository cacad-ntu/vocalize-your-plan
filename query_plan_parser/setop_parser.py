"""
Parser for SetOp node type
https://www.depesz.com/2013/05/19/explaining-the-unexplainable-part-4/
"""

import json
import query_plan_parser.parser

def setop_parser(plan, start=False):
    """ SetOp Parser """
    result = query_plan_parser.parser.parse_plan(plan["Plans"][0], start)
    result += " " + query_plan_parser.parser.get_conjuction()
    result += "it finds the "
    cmd_name = str(plan["Command"])
    if cmd_name == "Except" or cmd_name == "Except All":
        result += "differences "
    else:
        result += "similarities "
    result += "between the two previously scanned tables using the "
    result += plan["Node Type"] + " operation."

    return result


if __name__ == "__main__":
    PLAN = '''
    {                                           
        "Node Type": "SetOp",                             
        "Strategy": "Sorted",                             
        "Parallel Aware": false,                          
        "Command": "Except",                              
        "Startup Cost": 659139.58,                        
        "Total Cost": 668626.83,                          
        "Plan Rows": 574989,                              
        "Plan Width": 222,                                
        "Plans": [                                        
            {                                               
                "Node Type": "Some Node Type"     
            }
        ]
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(setop_parser(JSON_PLAN, start=True))
