import query_plan_parser.parser
import json

def hash_join_parser(sentence):
    result = ""

    if "Plans" in sentence:
        for child in sentence["Plans"]:
            result += query_plan_parser.parser.parse_plan(child)

    """Hash Semi Join"""
    if str(sentence["Join Type"]) == "Semi":
        hash_cond = str(sentence["Hash Cond"]).replace("::text", "")
        hash_cond = hash_cond.replace("=", "is inside the table")
        # attr = hash_cond.partition("=")[0]
        # table = hash_cond.partition("=")[2]
        result += " Hash Semi Join is performed to find out whether the attribute "
        result += hash_cond
    #Hash Join
    else:
        result += " the result from previous operation is joined with Hash Join"
        if 'Hash Cond' in sentence:
            result += ' with condition ' + sentence['Hash Cond'].replace("::text", "") + '.'
        else:
            result += '.'
    
    return result

if __name__ == "__main__":
    test = '''
    {                                                   
        "Node Type": "Hash Join",                        
        "Parent Relationship": "Outer",                   
        "Parallel Aware": false,                          
        "Join Type": "Semi",                              
        "Startup Cost": 16963.39,                         
        "Total Cost": 34094.11,                           
        "Plan Rows": 8582,                                
        "Plan Width": 22,                                 
        "Hash Cond": "(a.year = (min(publication.year)))",
        "Plans": [                                        
            {                                               
            "Node Type": "Seq Scan",                      
            "Parent Relationship": "Outer",               
            "Parallel Aware": false,                      
            "Relation Name": "publication",               
            "Alias": "a",                                 
            "Startup Cost": 0.00,                         
            "Total Cost": 15525.89,                       
            "Plan Rows": 574989,                          
            "Plan Width": 26                              
            },                                              
            {                                               
            "Node Type": "Hash",                          
            "Parent Relationship": "Inner",               
            "Parallel Aware": false,                      
            "Startup Cost": 16963.38,                     
            "Total Cost": 16963.38,                       
            "Plan Rows": 1,                               
            "Plan Width": 4
            }
        ]
    }
    '''
    test_plan = json.loads(test)
    print(hash_join_parser(test_plan))