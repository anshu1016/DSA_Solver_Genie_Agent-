# import streamlit as st 
# from config.docker_utils import start_docker_container,stop_docker_container
# from autogen_agentchat.messages import TextMessage
# from autogen_agentchat.base import TaskResult
# from teams.dsa_team import get_dsa_team_and_docker
# import asyncio
# st.title("DSA Genie - Generate Optimize Code")
# st.write("DSA_Genie – Turn Problem Statements into Code Instantly!")
# st.write("DSA_Genie is an AI-powered tool that transforms problem statements into optimized code solutions. It leverages advanced AI models to understand your requirements and generate efficient code snippets, making coding easier and faster than ever before.")

# task = st.text_input("Enter your problem statement here", 
#     placeholder="e.g., Write a Python function to find the factorial of a number"
# )
# async def run(team,docker,task):
#     try:
#         await start_docker_container(docker)
#         st.write('Docker Container Started Successfully')
#         async for message in team.run_stream(task=task):
#             if isinstance(message, TextMessage):
#                 print(msg:=f"{message.source} : {message.content}")
#                 yield msg
#             elif isinstance(message, TaskResult):
#                 print(msg:=f"Stop Reason: {message.stop_reason}")
#                 yield msg
#         print('Task Completed')
#     except Exception as e:
#         print(f'Error is : {e}')
#         yield f'Error: {e}'
#     finally:
#         await stop_docker_container(docker)   


  
# if st.button('Run'):
#     st.write('Running the Task')

#     team,docker = get_dsa_team_and_docker()

#     async def collect_msg():
#         async for msg in run(team,docker,task):
#             if isinstance(msg,str):
#                 if(msg.startswith('user')):
#                     with st.chat_message('user',avatar='🧑🏻‍🎓'):
#                         st.markdown(msg)
#                 elif msg.startswith('DSAProblemSolverAgent'):
#                     with st.chat_message('assistant',avatar='🤖'):
#                         st.markdown(msg)
#                 elif msg.startswith('CodeExecutorAgent'):
#                     with st.chat_message('code_executor',avatar='👨🏻‍💻'):
#                         st.markdown(msg)
#             elif isinstance(msg,TaskResult):
#                 with st.chat_message('stopper',avatar = '🚫'):
#                     st.markdown(f"Stop Reasoon: {msg.stop_reason}")
              
#     asyncio.run(collect_msg())

import streamlit as st
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from teams.dsa_team import get_dsa_team_and_docker
import asyncio
import time
from pathlib import Path

st.set_page_config(
    page_title="DSA Genie",
    page_icon="🧞‍♂️",
    layout="wide",
    initial_sidebar_state="auto",
)

st.markdown("""
    <style>
    .title-text {
        font-size: 40px;
        font-weight: bold;
        color: #6A5ACD;
    }
    .subtitle-text {
        font-size: 18px;
        color: #4B4B4B;
    }
    .stChatMessageUser, .stChatMessageAssistant, .stChatMessageCode_executor, .stChatMessageStopper {
        font-family: monospace;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title-text'>🤖 DSA Genie – Generate Optimized Code Instantly!</div>", unsafe_allow_html=True)
st.markdown("""
<div class='subtitle-text'>
    DSA_Genie is an AI-powered tool that transforms problem statements into optimized code solutions. 
    It leverages advanced AI agents to understand your requirements and generate efficient code snippets, making coding easier and faster than ever before.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# User input
with st.container():
    task = st.text_input(
        "🧠 Enter your problem statement:",
        placeholder="e.g., Write a Python function to find the factorial of a number",
        key="problem_input"
    )

async def run(team, docker, task):
    try:
        await start_docker_container(docker)
        st.success("🚀 Docker Container Started Successfully")
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg := f"{message.source} : {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg := f"Stop Reason: {message.stop_reason}")
                yield msg
        print('Task Completed')
    except Exception as e:
        print(f'Error is : {e}')
        yield f'Error: {e}'
    finally:
        await stop_docker_container(docker)

if st.button('🧞‍♂️ Run DSA Genie'):
    if not task.strip():
        st.warning("⚠️ Please enter a valid problem statement.")
    else:
        st.write("⏳ Running the Task...")
        team, docker = get_dsa_team_and_docker()

        async def collect_msg():
            chat_area = st.container()
            async for msg in run(team, docker, task):
                with chat_area:
                    if isinstance(msg, str):
                        if msg.startswith('user'):
                            with st.chat_message('user', avatar='🧑🏻‍🎓'):
                                st.markdown(msg)
                        elif msg.startswith('DSAProblemSolverAgent'):
                            with st.chat_message('assistant', avatar='🤖'):
                                st.markdown(msg)
                        elif msg.startswith('CodeExecutorAgent'):
                            with st.chat_message('code_executor', avatar='👨🏻‍💻'):
                                st.markdown(msg)
                    elif isinstance(msg, TaskResult):
                        with st.chat_message('stopper', avatar='🚫'):
                            st.markdown(f"Stop Reason: {msg.stop_reason}")

            # Check if solution.py was created and display it
            # solution_path = Path("temp/solution.py")
            # if solution_path.exists():
            #     with st.expander("📄 View Generated Solution (solution.py)"):
            #         code = solution_path.read_text()
            #         st.code(code, language='python')

            #     with open(solution_path, "rb") as f:
            #         st.download_button(
            #             label="⬇️ Download solution.py",
            #             data=f,
            #             file_name="solution.py",
            #             mime="text/x-python"
            #         )

        asyncio.run(collect_msg())
