1. Training:
 
python3 ./run_summarization.py \
    --model_name_or_path google/mt5-small\
    --do_train \
    --do_eval \
     --train_file  ./data/train.jsonl \
      --validation_file  ./data/public.jsonl \
    --source_prefix "summarize: " \
    --output_dir /./summarization \
    --per_device_train_batch_size=1 \
    --per_device_eval_batch_size=1 \
--eval_accumulation_steps=128 \
    --overwrite_output_dir \
    --predict_with_generate \
  --text_column maintext \
  --summary_column title \
 --learning_rate 1e-3 \
  --warmup_ratio 0.1 \

parameter:
train_file: train file location
validation_file: valid file location
output_dir: where to store the model and other data
eval_accumulation_step: to accelerate
text_column: the name column about all text
summary_column : the name column about summary
learning_rat: the rate of learning


2. Predicting:
  
python3 run_summarization.py \
  --do_predict \
  --model_name_or_path  ./summarization  \
  --test_file ./data/public.jsonl  \
  --output_dir ./ \
  --predict_with_generate \
  --text_column maintext \
  --per_device_eval_batch_size 4 \

parameter:
model_name_or_path: assign the model location
test_file : the location off test_file
text_column: the column name about all text
the predicted data will be stored in './generated_predictions.txt'

3. combine the predicted data with label and assign the outputfile name
Ex: 
python3  ./data/public.jsonl ./output.jsonl 

4. eval the prediction performance
Ex:
python3 eval.py -r ./data/public.jsonl -s ./output.jsonl



