from ai.completion.fewshotutility import fewshotutility
from ai.prompts.fewshot import fewshot

if __name__ == '__main__':
    examples = fewshot.FewShot.get_examples()
    prefix = fewshot.FewShot.get_prefix()
    suffix = fewshot.FewShot.get_suffix()
    example_template, example_variables = fewshot.FewShot.get_example_template()

    fewShot = fewshotutility.FewShotUtility(examples=examples,
                                            prefix=prefix,
                                            suffix=suffix,
                                            input_variables=["question"],
                                            example_template=example_template,
                                            example_variables=example_variables
                                            )
    question = "How to reach Jersey City from Hoboken?"
    prompt = fewShot.get_prompt(question)
    fewShot.print_travel_modes(prompt)