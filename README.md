# Fer2013plus-Facial-Emotion-Recognition-Pytorch
This work is the final project of the Affective Computing Course of UCAS.

## Usage
First, you should download the official Fer2013 dataset and Fer+ annotation, then place it in the outmost folder with the following folder structure `data/fer2013/fer2013.csv` and `data/fer2013/fer2013new.csv`

To get the Fer+ dataset, run the following:
```
python data_process.py
```

To train your own model, run the following:
```
python train.py --name='your_version'
```

To evaluate the model, run the following:
```
python evaluate.py --checkpoint='xxx/best_checkpoint.tar'
```

## Result
![实验结果](https://img1.imgtp.com/2023/06/05/xOPjHrZN.png)

## Reference
[1]. Barsoum, Emad and Zhang, Cha and Canton Ferrer, Cristian and Zhang, Zhengyou. Training Deep Networks for Facial Expression Recognition with Crowd-Sourced Label Distribution. ACM International Conference on Multimodal Interaction (ICMI)

[2]. Khaireddin, Yousif, and Zhuofa Chen. "Facial Emotion Recognition: State of the Art Performance on FER2013." arXiv preprint arXiv:2105.03588 (2021).


