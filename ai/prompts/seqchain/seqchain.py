class SeqChainPrompt:

    @staticmethod
    def get_first_template():
        return """
I want you to play the role of a travel bot and answer the question
Return the answer in a json format
you should have all the options listed in an array structure. 
The root of the array should be named as "options"
You should fill up the values yourself
remove non-viable or non-feasible options from the json
You should include at-least mode, duration and price in your output

Question: {question}
        """

    @staticmethod
    def get_second_template(input_key):
        key = "{" + input_key + "}"
        return f"""
From the given Travel_Modes, please extract the 2 modes where travel time is max and travel time is min
Return the answer in a json format like the input
Travel_Modes: {key}
        """

    @staticmethod
    def get_third_template(input_key):
        key = "{" + input_key + "}"
        return f"""
From the given options, please write a summary document on how can a traveller reach the destination
Options: {key}
        """