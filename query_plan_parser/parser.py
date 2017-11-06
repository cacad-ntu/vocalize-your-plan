"""
Main file to parse query plan
"""

from query_plan_parser.groupaggregate_parser import group_aggregate_parser

class ParserSelector:
    """ ParserSelectorClass """
    def __init__(self):
        """ Init Class """
        self.GroupAggregate = group_aggregate_parser

def parse_plan(plan):
    """ Parse json format of query plan """
    selector = ParserSelector()
    parser = getattr(selector, plan["Node Type"].replace(" ", "_"))
    parsed_plan = parser(plan)
    return parsed_plan
