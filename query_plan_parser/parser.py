"""
Main file to parse query plan
"""

from query_plan_parser.sort_parser import sort_parser
from query_plan_parser.groupaggregate_parser import group_aggregate_parser

class ParserSelector:
    """ ParserSelectorClass """
    def __init__(self):
        """ Init Class """
        self.Sort = sort_parser
        self.GroupAggregate = group_aggregate_parser

def parse_plan(plan):
    """ Parse json format of query plan """
    selector = ParserSelector()
    parser = getattr(selector, plan["Node Type"].replace(" ", "_"))
    parsed_plan = parser(plan)
    return parsed_plan
