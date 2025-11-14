# Deep Java Library (DJL)

## Install
```
mvn clean install
```

## Model Download Instructions

The `gpt-neo-1.3B` model was downloaded using the following Python command:

```python
python3 -c "from transformers import AutoModelForCausalLM; AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-neo-1.3B').save_pretrained('./models/gpt-neo-1.3B')"
```
