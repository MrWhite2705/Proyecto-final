from ultralytics import YOLO

model = YOLO("yolo26n.yaml")  # build a new model from YAML
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n.yaml").load("yolo26n.pt")  # build from YAML and transfer weights

dataset = model(img_path=r"C:\Users\datasets\coco8\images\train", data={"names": {0: "cars"}}, task="detect")
dataset.get_labels()