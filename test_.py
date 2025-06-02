# e2b_mcp_server.py
import argparse
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from e2b_code_interpreter import Sandbox
import json
import asyncio
import dotenv
dotenv.load_dotenv()
# 创建 MCP 服务实例
mcp = FastMCP("E2BServer")


class CodeExecutionResult(BaseModel):
    code: str
    result: str


@mcp.tool(description="Execute Python code in a sandbox environment.")
async def execute_python(code: str) -> str:
    """
    在沙盒环境中执行 Python 代码。
    
    Args:
        code (str): 要执行的 Python 代码。
    
    Returns:
        str: 执行结果（JSON 格式）。
    """
    try:
        with Sandbox() as sandbox:
            execution = sandbox.run_code(code, timeout=5)
            result = execution.text
            return json.dumps({"code": code, "result": result}, indent=2)
    except Exception as e:
        return json.dumps({"error": f"Failed to execute code: {str(e)}"}, indent=2)


async def test_execute_python():
    """
    测试 execute_python 工具是否能正确执行代码。
    """
   
    test_code = """
word = 'strawberry'
count_r = word.count('r')
count_r
"""
    print("Running test...")
    result = await execute_python(test_code)  
    print("Test Result:")
    print(result)


if __name__ == "__main__":
   
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--server_type",
        type=str,
        default="sse",
        choices=["sse", "stdio"],
        help="Type of server transport (sse or stdio).",
    )

    parser.add_argument(
        "--test",
        action="store_true",
        help="Run a test for the execute_python tool.",
    )
    args = parser.parse_args()

    if args.test:
        
        asyncio.run(test_execute_python())  
    else:
       
        mcp.settings.port=8001
        mcp.run(args.server_type)