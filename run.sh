python3 run_summarization.py \
--do_predict \
--model_name_or_path  ./summarization  \
--test_file "${1}"  \
--output_dir ./ \
--predict_with_generate \
--text_column maintext \
--per_device_eval_batch_size 4 \
--num_beams 5 

python3 combine.py  "${1}"  "${2}"
