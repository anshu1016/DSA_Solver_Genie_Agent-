from config.docker_executor import get_docker_executor
async def start_docker_container(docker):
    await docker.start()
    print('Docker Container Started Successfully!')
    
async def stop_docker_container(docker):
    print('Stopping Docker Container...')
    await docker.stop()

