"""
File to parse node type hash
"""
# https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/

import query_plan_parser.parser

def hash_parser(plan):
    sentence = query_plan_parser.parser.parse_plan(plan['Plans'][0])
    sentence += " The hash function makes a memory hash with rows from the source."

    return sentence