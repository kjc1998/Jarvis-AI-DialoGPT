from transformers import AutoModelForCausalLM, AutoTokenizer
from jarvis.chatSpeech import chatSpeech
from jarvis.speechChat import speechChat

import keyboard
import torch
import beepy
import time


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/DialoGPT-large").to("cuda")

step = 0
chatSpeech("Hi there! How may I help you?")
print("DialoGPT: {}".format("Hi there! How may I help you?"))


def jarvisCHAT():
    while True:
        if keyboard.is_pressed("esc"):
            print("Shutting Down")
            chatSpeech("Shutting Down")
            break
        elif keyboard.is_pressed("enter"):
            beepy.beep(sound=1)
            userText = str(speechChat())
            if userText == "Errors":
                continue
            print("User: {}".format(userText))
            new_user_input_ids = tokenizer.encode(
                userText + tokenizer.eos_token, return_tensors='pt').to("cuda")

            if step > 0:
                bot_input_ids = torch.cat(
                    [chat_history_ids, new_user_input_ids], dim=-1)
            else:
                bot_input_ids = new_user_input_ids

            # generated a response while limiting the total chat history to 1000 tokens,
            chat_history_ids = model.generate(
                bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id).to("cuda")

            # pretty print last ouput tokens from bot
            botText = tokenizer.decode(
                chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
            print("DialoGPT: {}".format(botText))
            chatSpeech(botText)
        else:
            pass


jarvisCHAT()
