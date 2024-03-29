# from src.models.pipeline.mlsd.train import TrainingPipeline
import torch

from src.models.networks.mobilev2_mlsd_tiny_net import MobileV2_MLSD_Tiny
from src.models.pipeline.mlsd.inference import InferencePipeline
from src.utils.placeholder import Box
from config import cfg

if __name__ == "__main__":
    box = Box()
    box.update(
        box.from_yaml(
            filename=cfg.model_config_file
        )
    )
    # training_pipeline = TrainingPipeline(cfg=cfg)
    # score = training_pipeline.run()
    # print(score)
    model = MobileV2_MLSD_Tiny()
    model_path = box.model.weight_path
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    inference_pipeline = InferencePipeline(
        model=model, device=device, model_weight_path=model_path
    )
    output = inference_pipeline.run(
        image_path="src/data/v1.1/train/00030077.jpg",
        image_save_name="00030077_output1",
        save_dir="src/workdir/experiments/output",
        is_saving=True,
    )
    print(output[1].shape)
