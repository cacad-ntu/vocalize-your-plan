"""
File to parse node type seq scan
"""

def seq_scan_parser(plan):
    """ Parser for the Seq Scan Node Type"""
    sentence = "It does a sequential scan on relation "
    if "Relation Name" in plan:
        sentence += plan['Relation Name']
        sentence += " "
    if "Alias" in plan:
        sentence += "with an alias of "
        sentence += plan['Alias']
        sentence += ". "
    if "Filter" in plan:
        sentence += "This is bounded by the condition: "
        sentence += plan['Filter']
    return sentence

# sentence = "It does a sequential scan on relation \'"
# with open("seqscan.json") as test:
#     plan = json.load(test)
# if "Relation Name" in plan:
#     sentence += plan['Relation Name']
#     sentence += "\' "
# if "Alias" in plan:
#     sentence += "with an alias of "
#     sentence += plan['Alias']
#     sentence += ". "
# if "Filter" in plan:
#     sentence += "This is bounded by the filter: "
#     sentence += plan['Filter']
# print(sentence)

# with open("test.json") as test:
#     plan = json.load(test)
#     print(plan['Plans'][0])
    