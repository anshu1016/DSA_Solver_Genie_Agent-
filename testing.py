from autogen_agentchat.agents import AssistantAgent,UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination,TextMessageTermination
from autogen_agentchat.ui import Console
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
job_position = 'Data Scientist'
experience = 3
model_client = OpenAIChatCompletionClient(
    model="llama3-70b-8192",
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    model_info={
        "family": "llama",
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True
    },
    default_params={
        "temperature": 1
    }
)

interviewer_agent= AssistantAgent(
    name="Interviewer",
    model_client = model_client,
    description=f'An AI agent that takes interview for a {job_position} position.',
    system_message = f'''
            You are a professional interviewer conducting an interview for the position of {job_position} having an experience of {experience} years.

            Ask one clear and concise question at a time according to user experience and position.

            Wait for the user’s response before proceeding to the next question.

            Ask a total of three questions, each focused on one of the following areas:

            Technical skills and relevant experience

            Problem-solving or critical thinking ability
            Your job is to continue and ask question, don't pay any attention to career coach agent.
            Cultural fit and work style

            After the third question is answered, politely end the interview by saying “TERMINATE”.
'''

)

candidate_agent = UserProxyAgent(
    name = 'Candidate',
    description=f'An AI agent that simulates a candidate for a {job_position} position.',
    input_func= input,

)

career_coach_agent = AssistantAgent(
    name = 'Career_Coach',
    model_client=model_client,
    description=f'An AI agent that provides feedback and advice to candidate for a {job_position} position and point the particular topic to be focus on.',
    system_message = f"""
            You are a career coach specializing in preparing candidates for the {job_position} position.

            Your role is to:
            - Provide **constructive feedback** on each of the candidate's responses.
            - Suggest **specific improvements** to enhance their answers.
            - At the end of the interview, deliver a **summary of the candidate's overall performance**.
            - Offer **actionable advice** to help the candidate improve for future interviews.
    """

)


team = RoundRobinGroupChat(
    participants=[interviewer_agent,candidate_agent,career_coach_agent],
    termination_condition=TextMentionTermination(text='TERMINATE'),
    max_turns=20  
)

# Running the Interview

stream = team.run_stream(task = 'Conducting an interview for a software engineer position')
async def main():
    await Console(stream)


if __name__=="__main__":
    import asyncio
    asyncio.run(main())