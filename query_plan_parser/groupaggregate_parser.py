"""
Parser for GroupAggregate node type
"""

import query_plan_parser.parser

def group_aggregate_parser(plan):
    """ Parser for GroupAggregate node type """
    parsed_plan = query_plan_parser.parser.parse_plan(plan["Plans"][0])
    parsed_plan += " Then we group the result by " + str(plan["Group Key"])
    if "Filter" in plan:
        parsed_plan += " bounded with condition " + plan["Filter"]
    parsed_plan += "."
    return parsed_plan