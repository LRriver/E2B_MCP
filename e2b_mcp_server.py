# e2b_mcp_server.py
import argparse
from fastmcp import FastMCP
from pydantic import BaseModel
from e2b_code_interpreter import Sandbox
import json
import dotenv
dotenv.load_dotenv()
# from mcp.server.fastmcp import FastMCP
mcp = FastMCP("E2BServer")


# class CodeExecutionResult(BaseModel):
#     code: str
#     result: str

#
@mcp.tool(description="Execute python code in a Jupyter notebook cell and return result. Only respond with the python code whithout explanatory note to be executed and nothing else. Strip backticks in code blocks.")
async def execute_python(code: str) -> str:
    try:
        with Sandbox() as sandbox:
            execution = sandbox.run_code(code, timeout=5)
            result = execution.text
            return json.dumps({"code": code, "result": result}, indent=2)
    except Exception as e:
        return json.dumps({"error": f"Failed to execute code: {str(e)}"}, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--server_type",
        type=str,
        default="sse",
        choices=["sse", "stdio"],
    )

    args = parser.parse_args()
    mcp.settings.port=8000
    mcp.run(args.server_type)