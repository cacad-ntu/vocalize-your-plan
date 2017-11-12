"""
Parser for nested loop node type
https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
"""
import query_plan_parser.parser

def nested_loop_parser(plan):
    """initialize empty string"""
    result = ""

    """Get the text of it's child"""
    temp = query_plan_parser.parser.parse_plan(plan["Plans"][0])
    result += "First, " + temp + " For every row of this results, "
    temp = query_plan_parser.parser.parse_plan(plan["Plans"][1])
    result += temp


    """Parse the nested loop """
    if(plan["Node Type"] == "Nested Loop"):
        result += "Then, the loop result between the first scan and second scan are returned as new rows."

    return result