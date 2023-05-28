from datetime import datetime
from argparse import ArgumentParser
from lib.openai_wrapper import OpenAiWrapper
from lib.prompt import Prompt, Prompts
from lib.role import Role


def main(prompt: str, role: str):
    role_description = Role().get_role(role)

    p1 = Prompt(role="system", content=role_description)
    p2 = Prompt(role="user", content=prompt)

    ps = Prompts()
    ps.append(p1)
    ps.append(p2)
    prompts = ps.get_prompts()

    gpt = OpenAiWrapper()
    gpt.complete_chat(prompts)
    first_message = gpt.get_first_message()

    # TODO: add logger

    return first_message


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--role", "-r")
    parser.add_argument("--prompt", "-p")
    args = parser.parse_args()

    print(main(prompt=args.prompt, role=args.role))
