# 🗼 Mobile Tower Components Detection

## Installation and Training

1. **Clone the Repository**
   
    ```bash
    https://github.com/mayurd8862/Mobile-Tower-Components-Detection.git
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Prepare data according to the following format**
   
   ![image](https://github.com/user-attachments/assets/cae4913c-a21c-46c5-9a97-8a3370852bfd)


4. **Run following command in CLI**
    ```bash
    yolo task=detect mode=train data=/data/data.yaml model=yolov8n.pt epochs=10 imgsz=640
    ```
5. **weights will be saved in directory**
    ```bash
    ./runs/detect/train/weights/last.pt
    ```
6. **Run the Streamlit Application**
    ```bash
    streamlit run app.py
    ```
    
        
