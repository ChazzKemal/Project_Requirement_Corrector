import openai
openai.api_key = "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"
model_engine = "text-davinci-003"
answers=[]
with open("statementlar.txt", "r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            print(line)
            prompt_start="Do you think this requirement is ambiguous according to system engineering with one word?"
            prompt = prompt_start + line
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )

            answer = completion.choices[0].text
            print(answer)
            answers.append(answer)
with open("prompt_answer.txt", "w",encoding="utf-8") as f:
    for text in answers:
        f.write(text + "\n")