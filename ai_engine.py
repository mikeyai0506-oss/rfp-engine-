from openai import OpenAI
from vector_store import search_similar

client = OpenAI(api_key="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")  # 🔥 PUT YOUR KEY HERE

def generate_answer(question):
    similar_data = search_similar(question)

    context = ""
    for item in similar_data:
        context += item["answer"] + "\n"

    prompt = f"""
    Answer this RFP question professionally.

    Question: {question}
    Context: {context}

    Keep it concise and formal.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content