"""
Generic Parser
"""

import json
import query_plan_parser.parser

def generic_parser(plan, start=False):
    """ Parse unknown node_type """
    parsed_plan = query_plan_parser.parser.get_conjuction(start)
    parsed_plan += "do " + plan["Node Type"] + "."
    if "Plans" in plan:
        for child in plan["Plans"]:
            parsed_plan += " " + query_plan_parser.parser.parse_plan(child)
    return parsed_plan


if __name__ == "__main__":
    PLAN = '''
    {                                
        "Node Type": "Unrecognize",       
        "Parent Relationship": "Outer",
        "Parallel Aware": false,       
        "Relation Name": "publication",
        "Alias": "publication",        
        "Startup Cost": 0.00,          
        "Total Cost": 15525.89,        
        "Plan Rows": 574989,           
        "Plan Width": 0,
        "Plans" :[
            {                                
                "Node Type": "Seq Scan",       
                "Parent Relationship": "Outer",
                "Parallel Aware": false,       
                "Relation Name": "publication",
                "Alias": "publication",        
                "Startup Cost": 0.00,          
                "Total Cost": 15525.89,        
                "Plan Rows": 574989,           
                "Plan Width": 0                
            }
        ]       
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(generic_parser(JSON_PLAN, start=True))
