import asyncio
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from teams.dsa_team import get_dsa_team_and_docker



async def main():
    dsa_team,docker = get_dsa_team_and_docker()
    try:
        await start_docker_container(docker)
        print('Docker Container Started Successfully')
        task = 'Write a python code for binary search to sort a number'
        async for message in dsa_team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print('=====' * 40)
                print(f"{message.source} : {message.content}")
            elif isinstance(message, TaskResult):
                print(f"Stop Reason: {message.stop_reason}")
    except Exception as e:
        print(f'error is: {e}')
    finally:
        await stop_docker_container(docker)

if __name__ == '__main__':
    asyncio.run(main())
            

