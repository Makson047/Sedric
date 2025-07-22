def load_prompt(prompt_path):
    """
    Завантажує текст шаблону промпта з файлу.
    :param prompt_path: шлях до .txt файлу
    :return: строка з шаблоном промпта
    """
    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()

def format_prompt(prompt_template, **kwargs):
    """
    Підставляє значення у шаблон промпта через .format()
    :param prompt_template: строка з шаблоном
    :param kwargs: словник підстановок
    :return: готовий промпт з підставленими значеннями
    """
    return prompt_template.format(**kwargs)