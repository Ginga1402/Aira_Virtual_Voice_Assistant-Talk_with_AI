


## Overview


This project introduces a cutting-edge voice assistant powered by Large Language Models (LLMs) and Generative AI, designed to revolutionize user interaction. The application allows seamless conversation with the assistant, which not only answers a wide range of queries but also remembers the context of previous interactions. This memory feature enables the assistant to provide more accurate and context-aware responses over time. By leveraging advanced query handling and the generative capabilities of AI, this voice assistant is ideal for use cases such as customer support, personal assistance, and interactive education, offering a sophisticated, intelligent, and user-friendly experience.


## Tech Stack Used

The following technologies and libraries were used in the development of this chatbot:

[Python](https://www.python.org/): Programming language used for the implementation.

[Langchain](https://www.langchain.com/): LangChain is a framework designed to simplify the creation of applications using large language models.

[Ollama](https://ollama.com/): It provides a simple API for creating, running, and managing models, as well as a library of pre-built models that can be easily used in a
variety of applications.

Model Used: [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1)  is a decoder only model which means that it resembles the decoder block of the transformer architecture. Most language models today are decoder only model since they are designed for text generation which doesn’t need bidirectional processing.

[Whisper](https://github.com/openai/whisper) is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.


## Getting Started

To get started with the Open-source AI equipped voice assistant, follow these steps:

1. Clone the repository
```py
git clone https://github.com/Ginga1402/Talk_with_AI
```
2. Install the required dependencies:

```py
pip install -r requirements.txt
```

3. Run the Whisper API :

```py
python run whisper_api.py
```


4. Run the Voice Assistant application 
```py
python run main.py
```


