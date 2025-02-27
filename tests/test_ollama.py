from langchain_ollama import OllamaLLM

def get_llm():
    """Returns an instance of OllamaLLM configured for llama3.2."""
    return OllamaLLM(
        model="llama3.2",
        system_message="Analyze the text and provide a clear summary in valid JSON format.",
        output_format="json",
        strict_mode=True,
        low_cpu_mem_usage=True
    )

# Prevent automatic execution when imported
if __name__ == "__main__":
    llm = get_llm()
    print(llm.invoke("Hello!"))
