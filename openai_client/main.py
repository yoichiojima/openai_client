from argparse import ArgumentParser
from lib.openai_wrapper import OpenAiWrapper
from lib.prompt import Prompt, Prompts

def main(prompt: str):
    p1 = Prompt(role = "system", content = "you're an helpful assistant.")
    p2 = Prompt(role = "user", content = prompt)

    ps = Prompts()
    ps.append(p1)
    ps.append(p2)

    prompts = ps.get_prompts()

    gpt = OpenAiWrapper()
    gpt.complete_chat(prompts)
    print(gpt.show_first_message())


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--role", "-r")
    parser.add_argument("--prompt", "-p")
    args = parser.parse_args()
    
    main(prompt = args.prompt)

