import pytest
import logging
import json
import sys
from langchain_ollama import OllamaLLM

# Configure logging for error tracking
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
LOGGER = logging.getLogger(__name__)

MODEL_NAME = "llama3.2"


def get_llm(model: str = MODEL_NAME) -> OllamaLLM | None:
    """
    Returns an instance of OllamaLLM with the appropriate configuration.

    Args:
        model (str): The name of the model to be used.

    Returns:
        OllamaLLM | None: An instance of the model, or `None` if initialization fails.
    """
    try:

        if not isinstance(model, str) or not model.strip():
            raise ValueError("Invalid model name provided.")
        
        return OllamaLLM(
            model=model,
            system_message="Analyze the text and provide a clear summary in valid JSON format.",
            output_format="json",
            strict_mode=True,
        )
    except Exception as e:
        LOGGER.error(f"Error initializing the model: {e}")
        return None


def explain_question_mark(question: str, model: str = MODEL_NAME) -> str:
    """
    Uses the LLM model to explain the given question.

    Args:
        question (str): The input question to be explained.
        model (str): The name of the model to be used.

    Returns:
        str: The model's response or an error message.
    """
    llm = get_llm(model)
    if llm is None:
        return " Error: Model initialization failed."

    try:
        response = llm.invoke(question)
        return response
    except Exception as e:
        LOGGER.error(f"Error invoking the model: {e}")
        return f" Error retrieving response: {e}"


def main():
    """Interactive console interface for asking questions and receiving responses from the model."""
    print("Willkommen! Geben Sie Ihre Frage ein (oder 'exit' zum Beenden):")

    while True:
        user_input = input("\nIhre Frage: ").strip()

        # Exit condition
        if user_input.lower() in {"exit", "quit"}:
            print("\nProgramm beendet. Auf Wiedersehen!")
            sys.exit(0)

        if not user_input:
            print("⚠ Bitte geben Sie eine gültige Frage ein.")
            continue  # Prevent sending an empty request to the model

        explanation = explain_question_mark(user_input)

        print("\nAntwort des Modells:\n")
        try:
            parsed_response = json.loads(explanation) if isinstance(explanation, str) else explanation
            print(json.dumps(parsed_response, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print(explanation)  # Print response as is if it's not in JSON format


if __name__ == "__main__":
    main()
