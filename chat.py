# this script contains the conversation logic

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts.prompt import PromptTemplate
# from langchain.llms import CTransformers
import os
from langchain_community.chat_models import ChatOllama



# using Ollama to run our LLM

local_llm = "mistral"
llm = ChatOllama(model=local_llm, temperature=0.3)


template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
{history}
Human: {input}

Only return the helpful answer below and nothing else.
AI Assistant:

"""
PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)


chat_conversation = ConversationChain(
    prompt=PROMPT,
    llm=llm,
    verbose=False,
    memory=ConversationBufferMemory(ai_prefix="AI Assistant"),
)




