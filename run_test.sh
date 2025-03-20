python prompt_batch.py --prompt-type demo --model gpt-4.5-preview --auto-query --always-save --template_version v0.1
python prompt_batch.py --prompt-type demo --model gpt-4o --auto-query --always-save --template_version v0.1
python prompt_batch.py --prompt-type demo --model gpt-4-1106-preview --auto-query --always-save --template_version v0.1

# Zeroscope (horizontal videos)
python generate.py --model gpt-4-1106-preview --run-model lvd_zeroscope --prompt-type lvd --save-suffix weak_guidance --template_version v0.1 --seed_offset 0 --repeats 10 --loss_scale 2.5 --loss_threshold 350. --max_iter 1 --max_index_step 10 --fg_top_p 0.25 --bg_top_p 0.25 --fg_weight 1.0 --bg_weight 2.0 --num_frames 24