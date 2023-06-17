def makeDict(payload):
    if 'words' in payload:
        if isinstance(payload['words'], list):
            output = {}
            for word in payload['words']:
                # total sum of vowels in each word 
                count = sum(list(map(word.lower().count, 'aeiou')))
                # add to dict
                output[f"{word}"] = f"{count}"
        else:
            output = {"Error": "Missing words list"}
    else:
        output = {"Error": "Missing words object"}
    return output

def makeArray(payload):
    if 'words' in payload:
        if isinstance(payload['words'], list):
            output = {}
            # default order value = asc
            order = 'asc'
            if payload['order'] == 'desc':
                order = 'desc'
            # check order status
            if order == 'asc':
                payload['words'].sort()
            else:
                payload['words'].sort(reverse=True)

            for word in payload['words']:
                output = payload['words']
        else:
            output = {"Error": "Missing words list"}
    else:
        output = {"Error": "Missing words object"}

    return output