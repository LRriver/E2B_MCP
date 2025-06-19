# E2B_MCP
中文 | [English](./README.md)

支持通过 MCP 协议连接 E2B，包含自定义的服务端和客户端，无需依赖如 Claude 应用、Cursor 等工具。

## 环境配置
```
conda create -n mcp python=3.12 -y
conda activate mcp
pip install -r requirements.txt
```

## 运行MCP
首先创建 `.env` 文件，并填写以下变量：
```
E2B_API_KEY= ""
model=""
llm_api_key=""
llm_api_base = ""
```
其中 `E2B_API_KEY` 需要前往 [E2B官网](https://e2b.dev/) 申请，`model`是LLM的名称，`llm_api_base`是LLM的url，`llm_api_key` 是 LLM 的 API Key。

然后启动服务端：
```bash
python ./e2b_mcp_server.py
```

打开一个新的终端窗口，运行客户端：
```bash
python ./e2b_mcp_llamaindex_client.py
```

效果如下：

![示意图](./img/image.png)
