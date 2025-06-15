import datetime
import autogen
from autogen import ConversableAgent
#import os

config_list = [
    {
        'model': 'gpt-3.5-turbo',
        'base_url': 'http://localhost:1234/v1',
        'api_key': 'lm-studio'
    }
]

llm_config={
    "timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = ConversableAgent(
    name="CTO",
    llm_config=llm_config,
    system_message="You are a personal assistant and can help people understand true values of life."
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web", "use_docker":False},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)
today = datetime.datetime.now().strftime("%Y-%m-%d")

#task = "Today is "+today+". Write Python code to plot NVDA's and AAPL's stock price gains YTD, and save the plot to a file named 'stock_gains.png'."
task = "I feel lonely."
#task = '''
#Read the file matrix.txt from the file explorer and summarize it.
#'''
user_proxy.initiate_chat(
    assistant,
    message=task
)