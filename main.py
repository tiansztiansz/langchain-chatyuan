from chains.local_doc_qa import LocalDocQA
import os

EMBEDDING_MODEL = "text2vec"  # embedding 模型，对应 embedding_model_dict
VECTOR_SEARCH_TOP_K = 1
LLM_MODEL = "chatyuan"  # LLM 模型名，对应 llm_model_dict
LLM_HISTORY_LEN = 1  # 上下文记忆长度，1为单轮对话


local_doc_qa = LocalDocQA()

local_doc_qa.init_cfg(
    llm_model=LLM_MODEL,
    embedding_model=EMBEDDING_MODEL,
    llm_history_len=LLM_HISTORY_LEN,
    top_k=VECTOR_SEARCH_TOP_K,
)


def display_answer(agent, query, vs_path, history=[]):
    for resp, history in local_doc_qa.get_knowledge_based_answer(
        query=query, vs_path=vs_path, chat_history=history, streaming=False
    ):
        print(resp["result"])
        print("\n")
        print(resp["source_documents"])


if __name__ == "__main__":
    file_path = os.path.join('docs', 'FAQ.md')
    # 设置文档所在位置
    vs_path, _ = local_doc_qa.init_knowledge_vector_store(file_path)

    history = []
    # 提问问题
    display_answer(
        local_doc_qa, query="本项目能否在colab中运行", vs_path=vs_path, history=history
    )

