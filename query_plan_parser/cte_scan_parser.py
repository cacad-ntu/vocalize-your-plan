"""
Parser for CTE scan node type
https://www.depesz.com/2013/05/19/explaining-the-unexplainable-part-4/
"""

import query_plan_parser.parser
import json 

def cte_scan_parser(plan):
    """initialize empty string"""
    result = ""

    """Get the text of it's child before if exists"""
    """if "Plans" in plan:
        for child in plan["Plans"]:
            temp = query_plan_parser.parser.parse_plan(child)
            result += temp + " "
    """

    """Parse the values scan"""
    if(plan["Node Type"] == "CTE Scan"):
        result += "It does a CTE scan through the table "+ str(plan["CTE Name"]) + " which is stored in memory "
        if "Index Cond" in plan:
            result += " with condition(s) "+ plan["Index Cond"].replace('::text','')
        result += ". "

        if "Filter" in plan:
            result += "The results then filtered by "+ plan["Filter"].replace('::text','') +". "
    
    return result

if __name__ == "__main__":

    test = '''
   {                                             
       "Node Type": "CTE Scan",                  
        "Parent Relationship": "Outer",           
        "Parallel Aware": false,                  
        "CTE Name": "x",                          
        "Alias": "x",                             
        "Startup Cost": 0.00,                     
        "Total Cost": 11651.98,                   
        "Plan Rows": 582599,                      
        "Plan Width": 218       
     }
    '''
    test_plan = json.loads(test)
    print(cte_scan_parser(test_plan))