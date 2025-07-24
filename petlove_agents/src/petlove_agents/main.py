#!/usr/bin/env python
import sys
import warnings
import time
from datetime import datetime

from petlove_agents.crew import PetloveAgents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    assistente_petlove = PetloveAgents()
    crew = assistente_petlove.crew()

    while True:
        user_input = input("\nDigite sua mensagem: ")
        
        if user_input.lower() in ['sair']:
            print("Encerrando conversa. Até logo!")
            break
        
        if not user_input.strip():
            print("Por favor, digite uma mensagem válida.")
            continue
        
        try:
            start_time = time.time()
            result = crew.kickoff(inputs={"user_input": user_input})
            end_time = time.time()

            print(f"\n🤖 Assistente PETLOVE: {result}\n")
            print("-" * 50)
            print(f"\nTempo gasto no processamento da Crew: {end_time - start_time:.4f} segundos")
            
        except Exception as e:
            print(f"\nErro: {e}")
            print("\nTente novamente ou digite 'sair' para encerrar.")



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        PetloveAgents().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        PetloveAgents().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        PetloveAgents().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
