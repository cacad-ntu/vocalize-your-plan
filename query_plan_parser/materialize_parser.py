"""
Parser for materialize node type
https://www.depesz.com/2013/05/09/explaining-the-unexplainable-part-3/
"""
import json
import query_plan_parser.parser

def materialize_parser(plan):

    """initialize empty string"""
    result = ""


    """Get the text of it's child before if exists"""
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = query_plan_parser.parser.parse_plan(child)
            result += temp + " "


    """Parse the materialize"""
    if(plan["Node Type"] == "Materialize"):
        result += "Next the results are stored in memory for faster access. "
        
    return result

if __name__ == "__main__":

    test = '''
   {                                             
    "Node Type": "Materialize",                                        
    "Parent Relationship": "Inner",                                    
    "Parallel Aware": false,                                           
    "Startup Cost": 19215.45,                                          
    "Total Cost": 19223.67,                                            
    "Plan Rows": 274,                                                  
    "Plan Width": 15,                                                  
    "Plans": [                                                         
        {                                                                
        "Node Type": "Aggregate",                                      
        "Strategy": "Sorted",                                          
        "Partial Mode": "Simple",                                      
        "Parent Relationship": "Outer",                                
        "Parallel Aware": false,                                       
        "Startup Cost": 19215.45,                                      
        "Total Cost": 19220.25,                                        
        "Plan Rows": 274,                                              
        "Plan Width": 23,                                              
        "Group Key": ["a_1.author"],                                   
        "Filter": "(count(a_1.author) >= 10)",                         
        "Plans": [                                                     
        {                                                            
            "Node Type": "Sort",                                      
            "Parent Relationship": "Outer",                           
            "Parallel Aware": false,                                  
            "Startup Cost": 19215.45,                                  
            "Total Cost": 19216.14,                                    
            "Plan Rows": 274,                                          
            "Plan Width": 15,                                          
            "Sort Key": ["a_1.author"],                                
            "Plans": [                                                
                {                                                        
                "Node Type": "Nested Loop",                            
                "Parent Relationship": "Outer",                        
                "Parallel Aware": false,                               
                "Join Type": "Inner",                                  
                "Startup Cost": 0.43,                                  
                "Total Cost": 19204.36,                                
                "Plan Rows": 274,                                      
                "Plan Width": 15,                                      
                "Plans": [                                             
                    {                                                    
                    "Node Type": "Seq Scan",                           
                    "Parent Relationship": "Outer",                    
                    "Parallel Aware": false,                           
                    "Relation Name": "publication",                    
                    "Alias": "b_1",                                    
                    "Startup Cost": 0.00,                              
                    "Total Cost": 17015.49,                            
                    "Plan Rows": 121,                                  
                    "Plan Width": 21,                                  
                    "Filter": "((title_abbrev)::text = 'sigmod'::text)"
                    },                                                   
                    {                                                    
                    "Node Type": "Index Only Scan",                    
                    "Parent Relationship": "Inner",                    
                    "Parallel Aware": false,                           
                    "Scan Direction": "Forward",                       
                    "Index Name": "pub_auth_pkey",                     
                    "Relation Name": "pub_auth",                       
                    "Alias": "a_1",                                    
                    "Startup Cost": 0.43,                              
                    "Total Cost": 18.05,                               
                    "Plan Rows": 4,                                    
                    "Plan Width": 38,                                  
                    "Index Cond": "(pub_key = (b_1.pub_key)::text)"    
                    }                                                    
                ]                                                      
            }                                                        
        ] 
        }
        ]                                                         
        }
        ]
     }
    '''
    test_plan = json.loads(test)
    print(materialize_parser(test_plan))