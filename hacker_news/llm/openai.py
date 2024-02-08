import tiktoken

import config


def sanitize_for_openai(text, overhead):
    text = text.replace('```', ' ').strip()  # in case of prompt injection

    # one token generally corresponds to ~4 characters, from https://platform.openai.com/tokenizer
    if len(text) > 4096 * 2:
        enc = tiktoken.encoding_for_model(config.openai_model)
        tokens = enc.encode(text)
        if len(tokens) > 4096 - overhead:  # 4096: model's context limit
            text = enc.decode(tokens[:4096 - overhead])
    return text.strip(".").strip()
