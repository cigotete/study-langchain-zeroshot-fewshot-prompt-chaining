class FewShot:

    @staticmethod
    def get_examples():
        examples = [
            {
                "question": "How to reach Kolkata airport to Kolkata Zoo?",
                "answer": """
option 1: mode=bus, min_time_in_min=75, max_time_in_min=90, description=take bus no 37 from airport. It
will drop you in alipore. Take a walk of 5 mins
option 2: mode=metro, min_time_in_min=40, max_time_in_min=60, description=take metro rail from airport. It
will drop you in joka. Take a walk of 10 mins
option 3: mod=train, min_time_in_min=45, max_time_in_min=60, description=take local train from airport. It
will drop you in new alipore. Take a walk of 10 mins
option 4: mod=walk, min_time_in_min=400, max_time_in_min=500, description=take Take a walk of 500 mins
"""
            },
            {
                "question": "How to reach Hyderabad airport to Hyderabad HiTech City?",
                "answer": """
option 1: mode=bus, min_time_in_min=60, max_time_in_min=75, description=take bus no 23 from airport. It
will drop you in hitech city.
option 2: mode=car, min_time_in_min=30, max_time_in_min=45, description=take ola/uber/airport shuttle.
It will drop you in HiTech city
option 3: mode=motorbike, min_time_in_min=25, max_time_in_min=40. description=take motorbike.It will 
drop you in HiTech city
                """
            },
            {
                "question": "How to reach Heathrow airport to Hounslow Central?",
                "answer": """
option 1: mode=tube, min_time_in_min=10, max_time_in_min=15. description=take tube from airport.
It will frop you in Hounslow central
option 2: mode=car, min_time_in_min=25, max_time_in_min=35. description=take rental car from
airport . It will drop you in Hounslow Central
"""
            }
        ]
        return examples

    @staticmethod
    def get_example_template():
        template = """
Question: {question}
Answer: {answer}
        """
        example_variables = ["question", "answer"]
        return template, example_variables

    @staticmethod
    def get_prefix():
        return f"""
I want you to play the role of a travel bot and answer the question
Return the answer in a json format
you should have all the options listed in an array structure. 
The root of the array should be named as "options"
You should fill up the values yourself
remove non-viable or non-feasible options from the json
"""

    @staticmethod
    def get_suffix():
        return """
Question: {question}
                """