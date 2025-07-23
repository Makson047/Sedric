def load_prompt(prompt_path):
    """
    Loads the text of the prompt template from a file.
    :param prompt_path: path to the .txt file
    :return: string with the prompt template
    """
    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()

def format_prompt(prompt_template, **kwargs):
    """
    Substitutes values into the prompt template through .format()
    :param prompt_template: string with the template
    :param kwargs: dictionary of substitutions
    :return: ready prompt with substituted values
    """
    return prompt_template.format(**kwargs)