"""
Parser for GroupAggregate node type
"""

from query_plan_parser.parser import parse_plan

def group_aggregate_parser(plan):
    """ Parser for GroupAggregate node type """
    parsed_plan = parse_plan(plan["Plans"][0])
    parsed_plan += " Then we group the result by " + plan["Group Key"]
    if "Filter" in plan:
        parsed_plan += " bounded with condition " + plan["Filter"]
    parsed_plan += "."
