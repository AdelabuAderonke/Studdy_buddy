import ollama

def get_coach_feedback(duration, focused, confused, distracted):
    mins = duration // 60
    secs = duration % 60

    prompt = f"""
    You are a supportive AI study coach. A student just finished a study session with these stats:
    - Duration: {mins} minutes {secs} seconds
    - Focused: {focused}%
    - Confused: {confused}%
    - Distracted: {distracted}%

    Give them:
    1. A brief encouraging comment on their session (1-2 sentences)
    2. One specific actionable tip based on their stats
    3. A focus score out of 10

    Keep it short, friendly and motivating. No bullet points, just natural conversation.
    """

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
