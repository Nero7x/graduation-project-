class ElementsFinder:
    
    def findActor(doc):
        actor1 = []
        actor2 = []
        for i, token in enumerate(doc):
            if token.pos_ == 'NOUN':
                # if the previous word to the noun is 'the'
                if i > 0 and doc[i-1].text.lower() == 'the':
                    actor1.append(token.text)
                # if the next word to the noun is of type 'VERB', 'AUX', or 'ADV'
                elif i < len(doc) - 1 and doc[i+1].pos_ in ['VERB', 'AUX', 'ADV']:
                    actor1.append(token.text)
            elif token.pos_ == 'VERB':
                for child in token.children:
                    if child.pos_ == 'NOUN':
                        actor2.append(child.text)
        finalActor = set(actor1) & set(actor2)
        return finalActor
    
    def findUsecase(doc, actors):
        usecase = []
        for i,token in enumerate(doc):
            if token.pos_ == 'VERB':
                for child in token.children:
                    if child.pos_ == 'NOUN':
                        for actor in actors:
                            if actor == child.text:
                                usecase.append(token.text)
                                if i+2 < len(doc) - 1 and (doc[i+1].text.lower() == 'and' or doc[i+1].text.lower() == 'or'):
                                    usecase.append(doc[i+2].text)

        usecase = list(dict.fromkeys(usecase))
        return usecase
    
    
    def findClass(doc):
        clas = ElementsFinder.findActor(doc)
        return clas
    

    def findAttributes(doc):
        attributes = []
        for i,token in enumerate(doc):
            if token.pos_ == 'NOUN' or token.pos_ == 'ADJ':
                if i < len(doc) - 1 and doc[i-1].pos_ in ['PRON', 'PART']:
                    attributes.append(token.text)
                    if i+2 < len(doc) - 1 and doc[i+1].text.lower() == 'and':
                        attributes.append(doc[i+2].text)
        return attributes
    
    def findMethod(doc, actor):
        method = ElementsFinder.findUsecase(doc, actor)
        return method
        

