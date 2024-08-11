
# Image Reconstruction of Functional Near-Infrared Spectroscopy (fNIRS) Signals

This project aims to enhance the functionality of Functional Near-Infrared Spectroscopy (fNIRS) by developing an advanced learning model to remove motion artifacts from fNIRS signals. By utilising unsupervised learning techniques, specifically autoencoders, the project significantly improves the quality of reconstructed brain images, making fNIRS a more reliable tool for neuroimaging in dynamic environments.


## Introduction

Functional Near-Infrared Spectroscopy (fNIRS) is a non-invasive neuroimaging technique used to monitor brain activity by measuring changes in blood oxygen levels. Unlike traditional methods such as fMRI, fNIRS is portable and cost-effective, making it ideal for studying brain activity during real-world tasks. However, fNIRS data are often affected by motion artifacts, which can degrade data quality. This project addresses this challenge by developing a robust learning model to remove such artifacts and enhance the data quality.

## Features

- **Artifact Removal:** Utilises an advanced autoencoder model to effectively remove motion artifacts from fNIRS signals.
- **Synthetic Data Generation:** Generates synthetic data to replicate real-world characteristics for training and validation.
- **Improved Image Quality:** Enhances the quality of reconstructed brain images from fNIRS signals.
- **Statistical Parametric Mapping:** Uses statistical techniques to infer brain activity and produce high-quality brain maps.

## Installation

To get started, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/KrishnaPavaniMunta/Professional-Project.git
cd Professional-Project
pip install -r requirements.txt
```

## Model Architecture

The model employs an autoencoder with the following architecture:

- **Encoder:** Consists of convolutional layers to compress the input data.
- **Decoder:** Reconstructs the data, preserving the signal's texture and nature.
- **Loss Function:** Custom loss functions to minimize motion artifacts and enhance data quality.

## Results

The model demonstrates significant improvements in removing motion artifacts compared to traditional methods, as evidenced by lower mean squared error (MSE) values and improved t-statistic maps for brain activity visualization.

## References

- MNE-Python. (n.d.). fNIRS processing. Retrieved from [MNE-Python fNIRS Processing](https://mne.tools/stable/auto_tutorials/preprocessing/70_fnirs_processing.html)
- Gao, Y. (n.d.). fNIRS_denoise_pytorch_3.py. Retrieved from [fNIRS Denoise by Deep Learning](https://github.com/YuanyuanGao216/fNIRS_denoise_by_DL/blob/master/fNIRS_denoise_pytorch_3.py)

## Acknowledgments

I extend my sincere gratitude to my supervisor, Prof. Shufan Yang, for her guidance and support throughout this project. Special thanks to my friend Adesh for his valuable feedback and encouragement.

## Contact

For questions or collaboration opportunities, please contact me at krishnapavanimunta@gmail.com.

