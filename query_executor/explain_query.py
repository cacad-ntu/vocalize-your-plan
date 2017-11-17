"""
Class to explain query plan (without execution)
"""

import json
import logging
import psycopg2

from query_plan_parser.parser import parse_plan
from voice_the_string.vocalize import Vocalizator

class Explain:
    """ Class to explain query """
    def __init__(
            self, host, port, dbname, user, password,
            desc=True, voice=False, debug=False
        ):
        """ init Explain """
        conn_string = "host='%s' port='%s' dbname='%s' user='%s' password='%s'"%(
            host, port, dbname, user, password)
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()
        logging.info("Connected to database: " + conn_string)

        self.desc = desc
        self.voice = voice
        self.debug = debug

        self.query = ""
        self.query_plan = {}
        self.parsed_plan = ""

        self.vocalizator = Vocalizator()


    def explain(self, query=None):
        """ explain query """
        if query:
            self.query = query

        logging.info("Generating query plan for: " + self.query)
        try:
            self.cursor.execute("EXPLAIN (FORMAT JSON) " + self.query)
            plan = self.cursor.fetchall()
            self.query_plan = plan[0][0][0]["Plan"]
        except:
            logging.error("Failed to generate query plan execution!")
            self.query_plan = {}
            self.parsed_plan = "Failed to generate query plan execution!"
            raise
        finally:
            logging.info("Generated query plan: " + json.dumps(self.query_plan, indent=4))

        return self.query_plan


    def parse(self, query_plan=None):
        """ Parse query plan """
        if query_plan:
            self.query_plan = query_plan

        logging.info("Parsing plan for: " + json.dumps(self.query_plan, indent=4))
        try:
            self.parsed_plan = parse_plan(self.query_plan, start=True)
        except:
            logging.error("Failed to parse query plan execution!")
            self.parsed_plan = "Failed to parse query plan execution!"
            raise
        finally:
            logging.info("Parsed plan: " + self.parsed_plan)

        return self.parsed_plan


    def loop_explain(self):
        """ continuously explain queries """
        print("postgres=# Please input query (end with ';')")
        next_line = ""
        self.query = ""
        while next_line.strip().lower() != "quit":
            next_line = input("postgres=# ")
            self.query += "\n" + next_line.strip()
            if self.query[-1] == ";":
                try:
                    self.explain()
                    self.parse()
                except Exception as exception:
                    logging.error("Error on Explain.explain(): " + str(exception))
                finally:
                    if self.debug:
                        print(json.dumps(self.query_plan, indent=4))
                    if self.desc:
                        print(self.parsed_plan)
                    if self.voice:
                        self.vocalizator.voice(self.parsed_plan)
                    self.query = ""
        