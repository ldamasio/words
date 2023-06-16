def makeDict(payload):
    if 'words' in payload:
        if isinstance(payload['words'], list):
            output = {}
            for word in payload['words']:
                count = sum(list(map(word.lower().count, "aeiou")))
                output[f"{word}"] = f"{count}"
        else:
            output = {"Error": "Missing words list"}
    else:
        output = {"Error": "Missing words object"}

    return output
