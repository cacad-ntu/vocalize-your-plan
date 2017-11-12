"""
Parser for materialize node type
https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
"""
import query_plan_parser.parser

def materialize_parser(plan):

    """initialize empty string"""
    result = ""


    """Get the text of it's child before if exists"""
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = query_plan_parser.parser.parse_plan(child)
            result += temp + " "


    """Parse the materialize"""
    if(plan["Node Type"] == "Materialize"):
        result += "Next the results are stored in memory for faster access. "
        
    return result