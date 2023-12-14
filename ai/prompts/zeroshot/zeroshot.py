def get_prompt_template():
    return """
    I want you to play the role of a travel bot and answer the question
    Return the answer in a json format
    you should have all the options listed in an array structure. 
    The root of the array should be named as "options"
    You should fill up the values yourself
    remove non-viable or non-feasible options from the json

    Question: {question}
    """