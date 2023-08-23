import logging

import torch
import transformers
from auto_gptq import AutoGPTQForCausalLM
from langchain.llms import HuggingFacePipeline
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    GenerationConfig,
    LlamaForCausalLM,
    LlamaTokenizer,
    pipeline,
)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s",
    level=logging.INFO,
)


class Model:
    MODEL_ID = "TheBloke/Llama-2-7b-Chat-GPTQ"  # "TheBloke/Llama-2-7b-Chat-GPTQ"
    MODEL_BASENAME = "model"  # "gptq-4bit-128g-actorder_True"

    # MODEL_ID = "TheBloke/Llama-2-13b-Chat-GPTQ" #"TheBloke/Llama-2-7b-Chat-GPTQ"
    # MODEL_BASENAME = "gptq_model-4bit-128g"
    # model_basename = "gptq_model-4bit-128g"

    # def __init__(self, save_directory = "models/llama2"):
    #     self.save_directory = save_directory
    #     self.bnb_config = BitsAndBytesConfig(
    #         load_in_4bit=True,
    #         bnb_4bit_compute_dtype=torch.bfloat16,
    #     )

    def load_model(self, device_type):
        """Select a model for text generation using the HuggingFace library. If you are running
        this for the first time, it will download a model for you. subsequent runs will use the
        model from the disk.

        Args:
            device_type (str): Type of device to use, e.g., "cuda" for GPU or "cpu" for CPU.
            model_id (str): Identifier of the model to load from HuggingFace's model hub.
            model_basename (str, optional): Basename of the model if using quantized models.
                Defaults to None.

        Returns:
            HuggingFacePipeline: A pipeline object for text generation using the loaded model.

        Raises:
            ValueError: If an unsupported model or device type is provided.
        """
        logging.info(f"Loading Model: {self.MODEL_ID}, on: {device_type}")
        logging.info("This action can take a few minutes!")

        if self.MODEL_BASENAME is not None:
            # The code supports all huggingface models that ends with GPTQ and have some variation
            # of .no-act.order or .safetensors in their HF repo.
            logging.info("Using AutoGPTQForCausalLM for quantized models")

            if ".safetensors" in self.MODEL_BASENAME:
                # Remove the ".safetensors" ending if present
                self.MODEL_BASENAME = self.MODEL_BASENAME.replace(".safetensors", "")

            print(self.MODEL_ID)
            tokenizer = AutoTokenizer.from_pretrained(self.MODEL_ID)
            logging.info("Tokenizer loaded")

            model = AutoGPTQForCausalLM.from_quantized(
                self.MODEL_ID,
                model_basename=self.MODEL_BASENAME,
                use_safetensors=True,
                trust_remote_code=True,
                device="cuda:0",
                use_triton=False,
                quantize_config=None,
            )
        elif (
            device_type.lower() == "cuda"
        ):  # The code supports all huggingface models that ends with -HF or which have a .bin
            # file in their HF repo.
            logging.info("Using AutoModelForCausalLM for full models")
            tokenizer = AutoTokenizer.from_pretrained(self.MODEL_ID)
            logging.info("Tokenizer loaded")

            model = AutoModelForCausalLM.from_pretrained(
                self.MODEL_ID,
                device_map="auto",
                torch_dtype=torch.float16,
                low_cpu_mem_usage=True,
                trust_remote_code=True,
                # max_memory={0: "15GB"} # Uncomment this line with you encounter CUDA out of memory errors
            )
            model.tie_weights()
        else:
            logging.info("Using LlamaTokenizer")
            tokenizer = LlamaTokenizer.from_pretrained(self.MODEL_ID)
            model = LlamaForCausalLM.from_pretrained(self.MODEL_ID)

        # Load configuration from the model to avoid warnings
        generation_config = GenerationConfig.from_pretrained(self.MODEL_ID)
        # see here for details:
        # https://huggingface.co/docs/transformers/
        # main_classes/text_generation#transformers.GenerationConfig.from_pretrained.returns

        # Create a pipeline for text generation
        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_length=2048,
            temperature=0,
            top_p=0.95,
            repetition_penalty=1.15,
            generation_config=generation_config,
        )

        local_llm = HuggingFacePipeline(pipeline=pipe)
        logging.info("Local LLM Loaded")

        return local_llm
