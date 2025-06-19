# E2B_MCP
English | [中文](./README_zh.md)

Support connecting E2B via MCP with a custom server and client, without the need for tools like the Claude app or Cursor.

## Environment configuration
```
conda create -n mcp python=3.12 -y
conda activate mcp
pip install -r requirements.txt
```

## Run MCP
First, create a `.env` file and fill in the following variables:  
```
E2B_API_KEY= ""
model=""
llm_api_key=""
llm_api_base = ""
```

`E2B_API_KEY` needs to be obtained from [E2B](https://e2b.dev/) , `model` is the name of the LLM, `llm_api_base` is the URL of the LLM, and `llm_api_key` is the API Key for the LLM.

Then start the server:
```bash
python ./e2b_mcp_server.py
```

Open a new terminal window and run the client:
```bash
python ./e2b_mcp_llamaindex_client.py
```

The result looks like this:

![alt text](./img/image.png)
