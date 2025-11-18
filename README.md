数据集已上传至https://huggingface.co/datasets/chencongxi/20251111


1.Install dependencies:
It is recommended to create a virtual environment using conda and then install the required libraries from requirements.txt.
pip install -r requirements.txt

1. Training

Modify the dataset path (data:) in default.yaml (or a config file in the cfg/ directory) and set the desired hyperparameters.

# Start training
python train.py --config your_config.yaml


2. Validation

Evaluate your trained model weights (.pt file) on the validation set.

# Evaluate the model on the validation set
python val.py --weights path/to/your/best.pt --config your_config.yaml


3. Inference

Use the detect.py script to perform waterbird detection on new images or videos.

# Detect on a single image or video
python detect.py --weights path/to/your/best.pt --source /path/to/image.jpg


4. Heatmap Generation

You can use the heatmap.py script to visualize the model's attention regions.

# Generate heatmap
python heatmap.py --weights path/to/your/best.pt --source /path/to/image.jpg
