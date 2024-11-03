from transformers import pipeline

def analyze_text(text):
    # Utilise un modèle de résumé ou de segmentation de texte
    print(text)
    summarizer = pipeline("summarization")
    scenes = summarizer(text, max_length=25, min_length=13, do_sample=False)
    return [scene['summary_text'] for scene in scenes]


import spacy

# Charger le modèle de langue française
nlp = spacy.load('en_core_web_sm')


def split_text_by_actions(text):
    doc = nlp(text)
    segments = []
    current_segment = []

    for sent in doc.sents:
        # Chercher les verbes dans la phrase
        verbs = [token for token in sent if token.pos_ == "VERB"]

        if verbs:
            # Si on trouve un verbe dans la phrase, on considère que c'est une action
            if current_segment:
                segments.append(' '.join(current_segment))
            current_segment = [sent.text]
        else:
            current_segment.append(sent.text)

    if current_segment:
        segments.append(' '.join(current_segment))

    return segments