from pif_generation import prompt_template, chat

def generate_questions(descroption = "sickness and weakness"):
    pif = prompt_template.format_messages(pif_description=descroption)
    res = chat(pif)
    qus = res.content.split('$\n')
    return qus
