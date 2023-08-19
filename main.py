from knowledge_core.inputs.input_parser import Splitter
from knowledge_core.llm.models import Model
from knowledge_core.llm.reason import ReasonUnit
def main():
    # Sample flow:
    splitter = Splitter()
    model = Model().load_model("cpu")
    reasoning_unit = ReasonUnit()
    
    with open("wikipedia_page.txt", "r") as f:
        text = f.read()
    chunks = splitter.split(text)
    
    # print(len(list(chunks)))
    for chunk in chunks:
        print(chunk)
        # response = reasoning_unit.top_level_reason(chunk, model)
        # print(response)
        # response = reasoning_unit.middle_level_reason(chunk, model, "Research")
        # print(response)
        # response = reasoning_unit.middle_level_reason(chunk, model, "Artificial Intelligence")
        # print(response)
        # response = reasoning_unit.middle_level_reason(chunk, model, "Technology")
        # print(response)
        # response = reasoning_unit.middle_level_reason(chunk, model, "Development")
        # print(response)
        response = reasoning_unit.bottom_level_reason(chunk, model, "Machine learning")
        print(response)
        response = reasoning_unit.bottom_level_reason(chunk, model, "Elon Musk")
        print(response)
        response = reasoning_unit.bottom_level_reason(chunk, model, "Coffe")
        print(response)
        response = reasoning_unit.bottom_level_reason(chunk, model, "Autonomous Systems")
        print(response)
        response = reasoning_unit.bottom_level_reason(chunk, model, "OpenAI")
        print(response)
        break
    
    # # 1. Ingest document and segment into chunks
    # doc = "Sample Wikipedia page about Albert Einstein. He was a physicist. He developed the theory of relativity."
    # chunks = doc.split(". ")  # Simple splitting, just for this example

    # # 2. Add chunks to the database
    # db = KnowledgeDatabase()
    # for chunk in chunks:
    #     kc = KnowledgeChunk(chunk, 'Mid-Level')  # As an example, we're considering all as Mid-Level
    #     db.add_chunk(kc)

    # # 3. Sample query and retrieval
    # query_text = "Tell me about Einstein."
    # query_embedding = KnowledgeChunk(query_text, 'Fine-Grained').embedding  # Just a placeholder
    # closest_chunk = db.search(query_embedding)

    # # 4. Interface with LLM
    # llm = LLMInterface()
    # response = llm.query(closest_chunk.text)
    # print(response)
if __name__ == "__main__":
    main()