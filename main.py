from ai.completion.zeroshotutility import zeroshotutility
from ai.prompts.zeroshot import zeroshot

if __name__ == '__main__':
    prompt_template = zeroshot.get_prompt_template()

    zeroShot = zeroshotutility.ZeroShotUtility(template=prompt_template)
    question = "How to reach Jersey City from Hoboken?"
    zeroShot.print_travel_modes(question=question)