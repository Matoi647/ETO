# python -m vllm.entrypoints.openai.api_server \
# --model ../facebook-opt-125m

# python -m vllm.entrypoints.openai.api_server \
# --model ../Meta-Llama-3-8B-Instruct-hf
# --port 8000

export CUDA_VISIBLE_DEVICES=1
python -m vllm.entrypoints.openai.api_server \
--model ../LLaMA-Factory/models/llama3_lora_sft_eto_alfworld_sft_demo_100 \
--port 8000