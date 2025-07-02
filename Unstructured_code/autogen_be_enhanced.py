from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.agents import CodeExecutorAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
import asyncio
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_agentchat.base import TaskResult
import os
from dotenv import load_dotenv
load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY_1")  # ✅ Correct function is getenv
if GROQ_API_KEY:
    print("✅ Key loaded.")
else:
    print("❌ Key missing.")


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



async def main():

    docker  = DockerCommandLineCodeExecutor(
        work_dir = '/tmp',
        timeout = 120
    )
    code_executor_agent = CodeExecutorAgent(
        name = 'CodeExecutorAgent',
        code_executor = docker
    )

    
    problem_solver_agent = AssistantAgent(
        name = 'DSAProblemSolverAgent',
        description = 'An agent that solves DSA Problem',
        model_client =model_client,
        system_message = """
            You are a problem-solving agent specializing in Data Structures and Algorithms (DSA).

            Your responsibilities include:
            - Collaborating with a code executor agent to test and run Python code.
            - Receiving problem statements and providing a clear, structured solution approach.
            - Starting your response by briefly explaining your plan to solve the problem.
            - Writing the solution in a **single Python code block**, properly formatted and self-contained.
            - Passing only one code block at a time to the executor agent for execution.

            After execution:
            - Analyze and explain the result of the code execution.
            - If the execution is successful and the task is completed, end your response with the word **'STOP'** to terminate the conversation.

            Always respond with your reasoning followed by exactly one code block.
"""
    )
    termination_condition = TextMentionTermination('STOP')
 
    
    try:
        await docker.start()
        team = RoundRobinGroupChat(
        participants = [problem_solver_agent,code_executor_agent],
        termination_condition = termination_condition,
        max_turns=10
        )   
        task = 'write a python code to add two numbers'
        async for message in team.run_stream(task=task):
            if isinstance(message,TextMessage):
                print(message.source,":",message.content)
            elif isinstance(message,TaskResult):
                print('Stop Reason: ',message.stop_reason)
            
            print('=='*30)
            print(message)
            print('=='*30)

        
        
    except Exception as e:
        print(f'error is: {e}')
    finally:
        await docker.stop()

if __name__ == '__main__':
    asyncio.run(main())