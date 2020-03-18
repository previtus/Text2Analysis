import nlp_tools

class AnalysisHandler(object):
    """
    Main class for the analysis ...
    """

    def __init__(self, settings):
        self.settings = settings
        self.input_text = None

        self.nlp_tools = nlp_tools.NLPTools(self.settings)

    def load_text(self, text):
        self.input_text = text
        print("Loaded text with", len(text), "characters!")

    def call_analysis_raw_text(self):
        self.nlp_tools.load_splitting_by_sentences(self.input_text)
        #return self.nlp_tools.analyze_full_bak() # older
        return self.nlp_tools.analyze_raw_text()


"""
# v1a
if __name__ == '__main__':
    settings = None
    testAnalysis = AnalysisHandler(settings)

    text = 'lorem ipsum'
    testAnalysis.load_text(text)
    reply = testAnalysis.call_analysis()

    print(reply)
"""

"""
if __name__ == '__main__':
    settings = None
    testAnalysis = AnalysisHandler(settings)

    #### no dots > DATASET = "_stackvTEST_questions14k"
    DATASET = "_stackvTEST_questions14kSKIPPREP"

    import numpy as np
    data = np.load("data/documents" + DATASET + ".npz")['a']
    #reply1 = testAnalysis.nlp_tools.analyze(data)

    print("documents data shape:", np.asarray(data).shape)
    print("documents [0] data shape:", np.asarray(data[0]).shape)
    print("documents [0] :", np.asarray(data[0]))

    text_joined = " ".join(np.asarray(data))
    print("joined as text: len, shape - ", len(text_joined))
    testAnalysis.load_text(text_joined)
    reply2 = testAnalysis.call_analysis()

    print(reply2)

# TODO:
#   - input from textarea / from one textfile = RAW TEXT
#   - input from CSV, each document is one row = LIST OF TEXTS
#   - (optional) input from CSV in [text,caption] per row  = LIST OF TEXTS+CAPTIONS
"""