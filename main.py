from ai.completion.chainutility import seqchainutility
from ai.prompts.seqchain import seqchain


if __name__ == '__main__':

    chains = []
    output_variables = []
    input_variables = ["question"]

    chainUtility = seqchainutility.ChainUtility(input_variables=input_variables)

    question_template = seqchain.SeqChainPrompt.get_first_template()
    output_key = "travel_modes"
    output_variables.append(output_key)
    question_chain = chainUtility.get_chain(template=question_template,output_key=output_key)
    chains.append(question_chain)

    travel_modes_template = seqchain.SeqChainPrompt.get_second_template(output_key)
    output_key = "options"
    output_variables.append(output_key)
    travel_mode_chain = chainUtility.get_chain(template=travel_modes_template, output_key=output_key)
    chains.append(travel_mode_chain)

    options_template = seqchain.SeqChainPrompt.get_third_template(output_key)
    output_key = "travel_advice"
    output_variables.append(output_key)
    options_chain = chainUtility.get_chain(template=options_template, output_key=output_key)
    chains.append(options_chain)

    overall_chain = chainUtility.get_overall_chain(chains=chains,output_variables=["travel_modes", "options", "travel_advice"])

    startQuestion = "How can I reach from Jersey City to Hoboken"
    chainUtility.print_completion(overall_chain,start=startQuestion)