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
            self, host, dbname, user, password,
            desc=True, voice=False, debug=False
        ):
        """ init Explain """
        conn_string = "host='%s' dbname='%s' user='%s' password='%s'"%(host, dbname, user, password)
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()
        logging.info("Connected to database: " + conn_string)

        self.desc = desc
        self.voice = voice
        self.debug = debug

        self.query = ""

        self.vocalizator = Vocalizator()

    def explain(self, query="", ret=False):
        """ explain query """
        if query != "":
            self.query = query

        logging.info("Executing: " + self.query)
        self.cursor.execute("EXPLAIN (FORMAT JSON) " + self.query)
        plan = self.cursor.fetchall()

        parsed_plan = parse_plan(plan[0][0][0]["Plan"], start=True)

        if self.debug:
            print(json.dumps(plan[0][0][0]["Plan"], indent=4))
        if self.desc:
            print(parsed_plan)
        if self.voice:
            self.vocalizator.voice(parsed_plan)

        logging.info("Parsed plan: " + parsed_plan)

        if ret:
            return parsed_plan

    def loop_explain(self):
        """ continuously explain queries """
        next_line = ""
        self.query = ""
        while next_line.strip().lower() != "quit":
            next_line = input("postgres=# ")
            self.query += "\n" + next_line.strip()
            if self.query[-1] == ";":
                self.explain()
                self.query = ""
        