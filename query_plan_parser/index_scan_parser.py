"""
Parser for index scan node type
https://www.depesz.com/2013/04/27/explaining-the-unexplainable-part-2/
"""

import query_plan_parser.parser

def index_scan_parser(plan):
    """initialize empty string"""
    result = ""

    """Parse the index scan or index only scan"""
    if(plan["Node Type"] == "Index Scan"):
        result += "It does an index scan by using an index table "+ plan["Index Name"]
        if "Index Cond" in plan:
            result += " with condition(s) "+ plan["Index Cond"].replace('::text','')
        result += ". And next it open the " + plan["Relation Name"]+ " table and fetch(es) row(s) pointed by index matched in the scan. "

        if "Filter" in plan:
            result += "The results then filtered by "+ plan["Filter"].replace('::text','') +". "

    elif(plan["Node Type"] == "Index Only Scan"):
        result += "It does an index scan by using an index table "+ plan["Index Name"]
        if "Index Cond" in plan:
            result += " with condition(s) "+ plan["Index Cond"].replace('::text','') 
        result += ". It returns the matches found in index table scan as the result(s). "
        if "Filter" in plan:
            result += "The result(s) then filtered by "+ plan["Filter"].replace('::text','') +". "

    return result