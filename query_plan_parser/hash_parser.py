"""
File to parse node type hash
"""

import query_plan_parser.parser

def hash_parser(plan):
    sentence = query_plan_parser.parser.parse_plan(plan['Plans'][0])
    sentence += " This hashes into memory."

    return sentence