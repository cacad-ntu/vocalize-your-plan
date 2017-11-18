"""
Parser for index scan node type
https://www.depesz.com/2013/04/27/explaining-the-unexplainable-part-2/
"""

import json
import query_plan_parser.parser

def index_scan_parser(plan, start=False):
    """ Index Scan parser """
    result = query_plan_parser.parser.get_conjuction(start)

    #Parse the index scan or index only scan
    if plan["Node Type"] == "Index Scan":
        result += "it does an index scan by using an index table "+ plan["Index Name"]
        if "Index Cond" in plan:
            result += " with conditions "+ plan["Index Cond"].replace('::text', '')
        result += ". Next, it opens the " + plan["Relation Name"]
        result += " table and fetches rows pointed by index matched in the scan."

        if "Filter" in plan:
            result += " The result is then filtered by "+ plan["Filter"].replace('::text', '') +"."

    elif plan["Node Type"] == "Index Only Scan":
        result += "it does an index scan by using an index table "+ plan["Index Name"]
        if "Index Cond" in plan:
            result += " with condition(s) "+ plan["Index Cond"].replace('::text', '')
        result += ". It then returns the matches found in index table scan as the result."
        if "Filter" in plan:
            result += " The result is then filtered by "+ plan["Filter"].replace('::text', '') +"."

    return result


if __name__ == "__main__":
    PLAN = '''
    {                                             
       "Node Type": "Index Scan",                          
       "Parallel Aware": false,                            
       "Scan Direction": "Forward",                        
       "Index Name": "publication_pkey",                   
       "Relation Name": "publication",                     
       "Alias": "publication",                             
       "Startup Cost": 0.42,                               
       "Total Cost": 8.44,                                 
       "Plan Rows": 1,                                     
       "Plan Width": 100,                                  
       "Index Cond": "((pub_key)::text = 'Saxena96'::text)"
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(index_scan_parser(JSON_PLAN, start=True))

    PLAN2 = '''
    {                                             
       "Node Type": "Index Only Scan",                           
       "Parallel Aware": false,                                  
       "Scan Direction": "Forward",                             
       "Index Name": "publication_pkey",                         
       "Relation Name": "publication",                           
       "Alias": "publication",                                   
       "Startup Cost": 0.42,                                     
       "Total Cost": 8.44,                                       
       "Plan Rows": 1,                                           
       "Plan Width": 21,                                         
       "Index Cond": "(pub_key = 'journals/acta/Saxena96'::text)"
    }
    '''
    JSON_PLAN2 = json.loads(PLAN2)
    print(index_scan_parser(JSON_PLAN2, start=True))
