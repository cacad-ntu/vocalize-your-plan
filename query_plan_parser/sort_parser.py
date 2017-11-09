"""
Parser for sort node type
https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
"""



import query_plan_parser.parser

def sort_parser(plan):
    """initialize empty string"""
    result = ""

    """Get the text of it's child before if exists"""
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = query_plan_parser.parser.parse_plan(child)
            result += temp + " "

    """Parse the Sort"""
    if(plan["Node Type"] == "Sort"):
        if "DESC" in plan["Sort Key"]:
            result += "Then, we sort the result by using attribute " + str(plan["Sort Key"].replace('DESC','')) +" in desceding order."
        elif "INC" in plan["Sort Key"]:
            result += "Then, we sort the result by using attribute " + str(plan["Sort Key"].replace('INC','')) +" in increasing order."
        else:
            result += "Then, we sort the result by using attribute " + str(plan["Sort Key"])+ "."

    return result