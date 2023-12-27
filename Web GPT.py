import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a particle physicist"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Q&A with Particle Physicist")

demo.launch(share=True)