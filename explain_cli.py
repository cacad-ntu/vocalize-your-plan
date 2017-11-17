"""
Start script to explain query
- Explain query in normal format
- Explain query in english format
- Explain query in voice
"""

import json
import logging
import sys
from datetime import datetime

from query_executor.explain_query import Explain

def init_logger(log_file):
    """ Initialize logger """
    logging.basicConfig(
        filename=log_file,
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s][%(message)s]'
    )

def main(argv):
    """ Main function to explain query """
    config_path = "config.json"
    with open(config_path, "r") as conf_file:
        conf = json.load(conf_file)

    log_path = conf["log"]["log_path"] + datetime.now().strftime("parser_%Y_%m_%d_%H_%M.log")
    init_logger(log_path)
    logging.info("Start logging")

    try:
        db_conf = conf["db"]
        cli_conf = conf["cli"]
        explanator = Explain(
            host=db_conf["host"],
            port=db_conf["port"],
            dbname=db_conf["database"],
            user=db_conf["username"],
            password=db_conf["password"],
            desc=cli_conf["desc_plan"],
            voice=cli_conf["voice_plan"],
            debug=cli_conf["debug_plan"]
        )
        if len(argv) > 1:
            query_plan_path = " ".join(argv[1:])
            print("Parsing query plan from " + query_plan_path)
            with open(query_plan_path) as query_plan_file:
                query_plan = json.load(query_plan_file)
            parsed_plan = explanator.parse(query_plan)
            if cli_conf["debug_plan"]:
                print("Original plan: " + json.dumps(query_plan, indent=4))
            if cli_conf["desc_plan"]:
                print("Parsed result: " + parsed_plan)
            if cli_conf["voice_plan"]:
                explanator.vocalizator.voice(parsed_plan)
        else:
            explanator.loop_explain()
    except Exception as exception:
        logging.error("Exception: " + str(sys.exc_info()[0]) + " " + str(exception))
        raise
    finally:
        logging.info("Finish logging")
        print("Log can be found at " + log_path)

if __name__ == "__main__":
    main(sys.argv)
