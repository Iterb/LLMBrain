from cortex_system.association_cortex.cortical_column import CorticalColumn
from cortex_system.association_cortex.neocortex import Neocortex
from cortex_system.learning.synaptic_learner import SynapticLearner
from cortex_system.reasoning.models import Model
from cortex_system.reasoning.reasoning_tools import MessageBank, ReasoningLevel
from cortex_system.reasoning.reasoning_unit import ReasonUnit
from cortex_system.sensory_cortex.input_cortex import InputSplitter


def main():
    # Sample flow:
    splitter = InputSplitter()
    model = Model().load_model("cuda")
    mb = MessageBank()
    reasoning_unit = ReasonUnit(model, mb)
    neocortex = Neocortex()
    learner = SynapticLearner(reasoning_unit)
    with open("wikipedia_page.txt") as f:
        text = f.read()
    chunks = splitter.split(text)
    for chunk_nr, chunk in enumerate(chunks):
        print(chunk)
        top_level_representation = learner.create_input_representation(
            ReasoningLevel.TOP_LEVEL, chunk
        )
        print(top_level_representation)

        top_level_kus_knowledge = learner.process_input(top_level_representation)
        for high_level_knowledge in top_level_kus_knowledge:
            top_ku = CorticalColumn(high_level_knowledge, parent=None)
            print(top_ku)
            neocortex.add_cortical_column(top_ku)

            mid_level_representation = learner.create_input_representation(
                ReasoningLevel.MID_LEVEL, chunk, high_level_knowledge
            )
            print(mid_level_representation)

            mid_level_kus_knowledge = learner.process_input(mid_level_representation)
            for mid_level_id, mid_level_knowledge in enumerate(mid_level_kus_knowledge):
                mid_ku = CorticalColumn(mid_level_knowledge, parent=top_ku)
                print(mid_ku)
                neocortex.add_cortical_column(mid_ku)

                low_level_representation = learner.create_input_representation(
                    ReasoningLevel.FINE_GRAINED, chunk, mid_level_knowledge
                )
                print(low_level_representation)
                low_ku = CorticalColumn(low_level_representation, parent=mid_ku)
                neocortex.add_cortical_column(low_ku)
                print(low_ku)
                if mid_level_id > 2:
                    break
        break

    print("\nFinal base\n")
    neocortex.display
    # response = reasoning_unit.middle_level_reason(chunk, model, "Artificial Intelligence")
    # print(response)
    # response = reasoning_unit.middle_level_reason(chunk, model, "Technology")
    # print(response)
    # response = reasoning_unit.middle_level_reason(chunk, model, "Development")
    # print(response)

    # response = reasoning_unit.middle_level_reason(chunk, model, "Research")
    # print(response)
    # response = reasoning_unit.middle_level_reason(chunk, model, "Artificial Intelligence")
    # print(response)
    # response = reasoning_unit.middle_level_reason(chunk, model, "Technology")
    # print(response)
    # response = reasoning_unit.middle_level_reason(chunk, model, "Development")
    # print(response)
    # response = reasoning_unit.fine_grained_reason(chunk, model, "Machine learning")
    # print(response)
    # response = reasoning_unit.fine_grained_reason(chunk, model, "Elon Musk")
    # print(response)
    # response = reasoning_unit.fine_grained_reason(chunk, model, "Coffe")
    # print(response)
    # response = reasoning_unit.fine_grained_reason(chunk, model, "Autonomous Systems")
    # print(response)
    # response = reasoning_unit.fine_grained_reason(chunk, model, "OpenAI")
    # print(response)
    # break

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
