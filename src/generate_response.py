import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI(api_key=openai_api_key)

SYSTEM_PROMPT = """You are a car diagnostics assistant. 
You are given a database of car error codes, problem descriptions, causes, and solutions. 
Your task is to provide clear and detailed responses based on user queries. Use the following guidelines:

1. **Error Code Details**: If the user asks about a specific error code (e.g., P0300), provide a full breakdown of:
   - **Problem Description**: Briefly explain the issue the error code represents.
   - **Causes**: List the common causes of the issue.
   - **Solutions**: Suggest practical steps to resolve the issue.

2. **Problem Description Queries**: If the user asks about a problem description (e.g., "Why is my engine misfiring?"), find the relevant error code and provide:
   - **Relevant Error Code**: Mention the corresponding error code if available.
   - **Causes**: Describe what typically causes this issue.
   - **Solutions**: Offer solutions for fixing the problem.

3. **Gratitude Responses**: If the user expresses gratitude (e.g., "thank you," "that was all," "I appreciate it"), acknowledge their message with a friendly response, such as:
- "You're welcome! If you have any more questions, feel free to ask."
- "Glad I could help! Don't hesitate to reach out if you need anything else."

4. **Error Handling**: If the user's query doesn't match any known error code or description, respond with:
   - "I couldn't find information on that issue. Please try again with a specific error code or description."
"""


def query_car_problem(collection, query):
    """Query the car problems collection for relevant information."""
    results = collection.query(
        query_texts=[query],
        n_results=1
    )

    if results["documents"] and results["documents"][0]:
        return results["documents"][0]
    return None


def generate_response(car_problem_info, query):
    """Generate a response using the OpenAI API based on car problem info."""
    prompt = (f"{SYSTEM_PROMPT}\n"
              f"A user has asked the following question: \"{query}\"\n"
              f"Based on the following car problem details, provide a helpful and detailed response:\n{car_problem_info}")

    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query}
            ],
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating response: {e}"


def get_solution(collection, query):
    """Get the solution for a car problem based on user query."""
    car_problem_info = query_car_problem(collection, query)

    if car_problem_info:
        return generate_response(car_problem_info, query)

    return "I couldn't find information on that issue. Please try again with a specific error code or description."
