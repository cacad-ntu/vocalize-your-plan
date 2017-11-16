"""
Query Plan App (Windows Compatible)
"""

try:
    # python 2.x
    from Tkinter import *
except ImportError:
    # python 3.x
    from tkinter import *

from query_executor.explain_query import Explain
from voice_the_string.vocalize import Vocalizator

class QueryPlanApp(Tk):
    def __init__(self,parent):
        self.vocalizator = Vocalizator()
        self.parsed_plan = ""

        Tk.__init__(self,parent)
        self.parent = parent
        self.minsize(width=800,height=500)
        self.initialize()

    def initialize(self):
        """ GUI Initialization """
        self.label_host = Label(self, text="Host:", width=10, anchor="w")
        self.label_host.grid(column=0, row=0, columnspan=1, sticky='W')
        self.entry_var_host = StringVar()
        self.entry_host = Entry(self, textvariable=self.entry_var_host)
        self.entry_host.grid(column=1, row=0, columnspan=3, sticky='EW')
        self.entry_var_host.set("localhost")

        self.label_database = Label(self, text="Database:", width=10, anchor="w")
        self.label_database.grid(column=0, row=1, columnspan=1, sticky='W')
        self.entry_var_database = StringVar()
        self.entry_database = Entry(self, textvariable=self.entry_var_database)
        self.entry_database.grid(column=1, row=1, columnspan=3, sticky='EW')
        self.entry_var_database.set("postgres")

        self.label_port = Label(self, text="Port:", width=10, anchor="w")
        self.label_port.grid(column=0, row=2, columnspan=1, sticky='W')
        self.entry_var_port = StringVar()
        self.entry_port = Entry(self, textvariable=self.entry_var_port)
        self.entry_port.grid(column=1, row=2, columnspan=3, sticky='EW')
        self.entry_var_port.set("5432")

        self.label_username = Label(self, text="Username:", width=10, anchor="w")
        self.label_username.grid(column=0, row=3, columnspan=1, sticky='W')
        self.entry_var_username = StringVar()
        self.entry_username = Entry(self, textvariable=self.entry_var_username)
        self.entry_username.grid(column=1, row=3, columnspan=3, sticky='EW')
        self.entry_var_username.set("postgres")

        self.label_password = Label(self, text="Password:", width=10, anchor="w")
        self.label_password.grid(column=0, row=4, columnspan=1, sticky='W')
        self.entry_var_password = StringVar()
        self.entry_password = Entry(self, show='*', textvariable=self.entry_var_password)
        self.entry_password.grid(column=1, row=4, columnspan=3, sticky='EW')
        self.entry_var_password.set("admin")

        self.label_query = Label(self, text="Query:", anchor="w")
        self.label_query.grid(column=0, row=5, columnspan=1, sticky='W')
        self.frame_query = Frame(self)
        self.frame_query.grid(column=1, row=6, columnspan=6, rowspan=1, sticky='W')
        self.button_query = Button(
            self.frame_query, text="Explain!",
            width=20, command=self.explain_query)
        self.button_query.pack(side=BOTTOM)
        self.entry_query = Text(self.frame_query, height=15, wrap=WORD)
        self.entry_query.pack(side='left', fill='both', expand=True)
        self.scrollbar_query = Scrollbar(self.frame_query)
        self.entry_query.config(yscrollcommand=self.scrollbar_query.set)
        self.scrollbar_query.config(command=self.entry_query.yview)
        self.grid()
        self.scrollbar_query.pack(side='right', fill='y')

        self.label_plan = Label(self, text="Query Plan:", anchor="w")
        self.label_plan.grid(column=0, row=8, columnspan=1, sticky='W')
        self.frame_plan = Frame(self)
        self.frame_plan.grid(column=1, row=9, columnspan=6, rowspan=1, sticky='W')
        self.button_plan = Button(
            self.frame_plan, text="Vocalize!",
            width=20, command=self.vocalize_plan)
        self.button_plan.pack(side=BOTTOM)
        self.entry_plan = Text(self.frame_plan, height=10, wrap=WORD)
        self.entry_plan.pack(side='left', fill='both', expand=True)
        self.scrollbar_plan = Scrollbar(self.frame_plan)
        self.entry_plan.config(yscrollcommand=self.scrollbar_plan.set)
        self.scrollbar_plan.config(command=self.entry_plan.yview)
        self.grid()
        self.scrollbar_plan.pack(side='right', fill='y')

    def explain_query(self):
        """ Explain query """
        explanator = Explain(
            self.entry_var_host.get(),
            self.entry_var_database.get(),
            self.entry_var_username.get(),
            self.entry_var_password.get(),
            desc=False, voice=False, debug=False
        )
        query = self.entry_query.get("1.0", END)
        self.parsed_plan = explanator.explain(query=query, ret=True)
        self.entry_plan.delete("1.0", END)
        self.entry_plan.insert("1.0", self.parsed_plan)

    def vocalize_plan(self):
        """ Vocalize Plan """
        parsed_plan = self.entry_plan.get("1.0", END)
        self.vocalizator.voice(parsed_plan)


if __name__ == "__main__":
    app = QueryPlanApp(None)
    app.title('Postgres Query Explainator')
    app.mainloop()