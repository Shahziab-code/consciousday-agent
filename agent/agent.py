import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

PROMPT_TEMPLATE = """
You are a daily reflection and planning assistant. Your goal is to:
1. Reflect on the user's journal and dream input
2. Interpret the user's emotional and mental state
3. Understand their intention and 3 priorities
4. Generate a practical, energy-aligned strategy for their day

INPUT:
Morning Journal: {journal}
Intention: {intention}
Dream: {dream}
Top 3 Priorities: {priorities}

OUTPUT:
1. Inner Reflection Summary
2. Dream Interpretation Summary
3. Energy/Mindset Insight
4. Suggested Day Strategy (time-aligned tasks)
"""

def get_agent_response(journal, intention, dream, priorities):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("❌ OPENROUTER_API_KEY is not set.")

    llm = ChatOpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        model="openai/gpt-3.5-turbo",   # Cheaper & lighter
        temperature=0.7,
        max_tokens=800                  # reduce to avoid 402 errors
    )

    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["journal", "intention", "dream", "priorities"]
    )

    chain = LLMChain(prompt=prompt, llm=llm)
    return chain.run({
        "journal": journal,
        "intention": intention,
        "dream": dream,
        "priorities": priorities
    })
