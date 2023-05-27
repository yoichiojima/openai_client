from lib.openai_wrapper import OpenAiWrapper
from lib.prompt import Prompt, Prompts

def main():
    p1 = Prompt(role = "system", content = "you're an helpful assistant.")
    p2 = Prompt(role = "user", content = "tell me what is good about rust as programming language.")

    ps = Prompts()
    ps.append(p1)
    ps.append(p2)

    prompts = ps.get_prompts()

    gpt = OpenAiWrapper()
    print(gpt.complete_chat(prompts))

main()
