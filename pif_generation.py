import os
import openai

api_key = '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'

from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(temperature=0.9, openai_api_key=api_key, model='gpt-4')

review_template = """you are an expert health consultant who specializes in creating paitent intake form, \
you come up with 10 specific and precise questions for patient intake form

take the disease description or symptomps description below by triple backticks and use it to create 10 precise and specific question for patient intake form


description: ```{pif_description}```

format the output as delimeter seperated question with the following delimeter
$
"""

from langchain.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(review_template)


