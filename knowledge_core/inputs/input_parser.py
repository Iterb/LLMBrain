from langchain.text_splitter import Language, RecursiveCharacterTextSplitter

class Splitter():
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        
    def split(self, text):
        for chunk in self.text_splitter.split_text(text):
            yield chunk