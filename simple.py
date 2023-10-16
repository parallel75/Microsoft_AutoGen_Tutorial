from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# 配置 openai api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# 创建 assistant agent
assistant = AssistantAgent(name="assistant", llm_config={
                           "config_list": config_list})

# 创建 user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"work_dir": "sources"})


# 设置目标 开始干活
user_proxy.initiate_chat(
    assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
