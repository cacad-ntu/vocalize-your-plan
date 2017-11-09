"""
File to parse node type seq scan
"""
# https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
import json

def seq_scan_parser(plan):
    """ Parser for the Seq Scan Node Type"""
    sentence = "It does a sequential scan on relation "
    if "Relation Name" in plan:
        sentence += plan['Relation Name']
    if "Alias" in plan:
        if plan['Relation Name'] == plan['Alias']:
            sentence += ". "
        else:
            sentence += " with an alias of "
            sentence += plan['Alias']
            sentence += ". "
    else:
        sentence += ". "
    if "Filter" in plan:
        sentence += "This is bounded by the condition: "
        sentence += plan['Filter']
    return sentence

if __name__ == "__main__":
    test = '''
    {                                
        "Node Type": "Seq Scan",       
        "Parent Relationship": "Outer",
        "Parallel Aware": false,       
        "Relation Name": "publication",
        "Alias": "publication",        
        "Startup Cost": 0.00,          
        "Total Cost": 15525.89,        
        "Plan Rows": 574989,           
        "Plan Width": 0                
    }
    '''
    test_plan = json.loads(test)
    print(seq_scan_parser(test_plan))