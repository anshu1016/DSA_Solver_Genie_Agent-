from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constant import WORK_DIR,TIMEOUT

def get_docker_executor():
    """
    Returns an instance of DockerCommandLineCodeExecutor configured for code execution.
    """
    docker  = DockerCommandLineCodeExecutor(
            work_dir = WORK_DIR,
            timeout = TIMEOUT
    )
    return docker