"""
Main file to parse query plan
"""

import query_plan_parser.hash_join_parser as hash_join
import query_plan_parser.sort_parser as sort
import query_plan_parser.groupaggregate_parser as groupaggregate
import query_plan_parser.seq_scan_parser as seq_scan
import query_plan_parser.hash_parser as hash
import query_plan_parser.merge_join_parser as merge_join
import query_plan_parser.limit_parser as limit
import query_plan_parser.unique_parser as unique
import query_plan_parser.function_scan_parser as function_scan

class ParserSelector:
    """ ParserSelectorClass """
    def __init__(self):
        """ Init Class """
        self.Hash_Join = hash_join.hash_join_parser
        self.Sort = sort.sort_parser
        self.Aggregate = groupaggregate.group_aggregate_parser
        self.Seq_Scan = seq_scan.seq_scan_parser
        self.Hash = hash.hash_parser
        self.Merge_Join = merge_join.merge_join_parser
        self.Limit = limit.limit_parser
        self.Unique = unique.unique_parser
        self.Function_Scan = function_scan.function_scan_parser

def parse_plan(plan):
    """ Parse json format of query plan """
    selector = ParserSelector()
    parser = getattr(selector, plan["Node Type"].replace(" ", "_"))
    parsed_plan = parser(plan)
    return parsed_plan
