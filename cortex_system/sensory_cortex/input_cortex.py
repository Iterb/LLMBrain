from langchain.text_splitter import RecursiveCharacterTextSplitter


class InputSplitter:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    def split(self, text):
        yield from self.text_splitter.split_text(text)
