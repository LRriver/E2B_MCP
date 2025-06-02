from openai import OpenAI
from dotenv import load_dotenv
import json
from e2b_code_interpreter import Sandbox
import re
# 加载环境变量
load_dotenv()

# pip install openai e2b-code-interpreter

from e2b_code_interpreter import Sandbox

# Create OpenAI client

api_key = "EMPTY"
base_url = "http://localhost:6005/v1"
client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

system = """
You are a helpful assistant that can execute python code in a Jupyter notebook.
"""
prompt = """Answer the given question. You must conduct reasoning inside <think> and </think> first every time you get new information,for example: <think> The request is asking to solve </think>. After reasoning, if you encounter a computational problem, you must use the execute_python tool to run the code for calculation. Only respond with the code to be executed and nothing else. Remove backticks from code blocks. Your code content needs to be enclosed within <code>and </code>tags, for example: <code>return word.count('r')</code>. If you find no further external knowledge needed, you can directly provide the answer inside <answer> and </answer>, without detailed illustrations. For example, <answer> Beijing </answer>.Question:{Given the complex number $z$ has a modulus of 1. Find
$$
u=\frac{(z+4)^{2}-(\bar{z}+4)^{2}}{4 i} \text {. }
$$

the maximum value.}"""

# Send messages to OpenAI API
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
                {"role": "system", "content": "You are a helpful assistant that can execute python code in a Jupyter notebook.遇到计算题时你必须调用execute_python工具帮你运行代码计算， Only respond with the code to be executed and nothing else. Strip backticks in code blocks.你需要代码内容包含在<code> </code>标签中，例如:<code> return word.count('r')</code>"},
                {"role": "user", "content": prompt}
            ]
)

# Extract the code from the response
content = response.choices[0].message.content
print(content)


# 假设 content 是从 API 响应中提取的内容
content = response.choices[0].message.content

# 使用正则表达式提取 <code> 和 </code> 之间的内容
match = re.search(r'<code>(.*?)</code>', content, re.DOTALL)

if match:
    code = match.group(1).strip()  # 提取代码并去除多余空白
    print("Extracted Code:")
    print(code)


# Execute code in E2B Sandbox
if code:
    with Sandbox() as sandbox:
        execution = sandbox.run_code(code)
        result = execution.text

    print(result)
