import json
import os
from utils.llm import get_parsed_layout
from utils.parse import parsed_layout_to_condition, show_video_boxes

def generate_conditions_and_boxes(data, output_prefix="img_generations/cache_lvd_v0.1_gpt-4-1106-preview"):
    """Generate box condition images based on parsed layout data."""
    os.makedirs(output_prefix, exist_ok=True)

    for prompt_id, (prompt, results) in enumerate(data.items()):
        for result_idx, result in enumerate(results):
            parsed_layout, _ = get_parsed_layout(
                prompt,
                max_partial_response_retries=1,
                override_response=result,
                json_template=False,
            )
            print("\nparsed_layout: ", parsed_layout)

            box_H, box_W = 500, 500
            condition = parsed_layout_to_condition(
                parsed_layout,
                height=box_H,
                width=box_W,
                num_condition_frames=6
            )
            print('\nCondition: ', condition)

            box_save_path = os.path.join(output_prefix, f"boxes_{prompt_id}_{result_idx}.gif")
            show_video_boxes(condition, save_path=box_save_path, save=True)
            print(f"Saved boxes image to: {box_save_path}")

if __name__ == "__main__":
    json_file = "cache/cache_lvd_v0.1_gpt-4-1106-preview.json"
    with open(json_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    generate_conditions_and_boxes(json_data)