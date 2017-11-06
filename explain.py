"""
Start script to explain query
- Explain query in normal format
- Explain query in english format
- Explain query in voice
"""

import logging
import json

from query_executor.explain_query import Explain

def init_logger(log_file):
    """ Initialize logger """
    logging.basicConfig(
        filename=log_file,
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s][%(message)s]'
    )

def main():
    """ Main function to explain query """
    config_path = "config.json"
    with open(config_path, "r") as conf_file:
        conf = json.load(conf_file)

    init_logger(conf["log"]["log_path"])
    logging.info("Start logging")

    db_conf = conf["db"]
    app_conf = conf["app"]
    explanator = Explain(
        db_conf["host"], db_conf["database"], db_conf["username"], db_conf["password"],
        app_conf["normal_plan"], app_conf["desc_plan"], app_conf["voice_plan"]
    )
    explanator.loop_explain()

    logging.info("Finish logging")

if __name__ == "__main__":
    main()
