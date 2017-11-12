"""
Parser for append node type
https://www.depesz.com/2013/05/19/explaining-the-unexplainable-part-4/
"""

import query_plan_parser.parser

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

