# Amazon ML Challenge 2024  
**Rank: 90 (TOP 0.1%)**  

**Note:** Our approach was completely dependent on Kaggle's free-tier GPUs, with no access to external servers or dedicated computational resources, unlike many top performers.  

---

## **Table of Contents**  
- [Introduction](#introduction)  
- [Approach](#approach)  
  - [Pre-trained Model Selection](#pre-trained-model-selection)  
  - [Strategy Development](#strategy-development)  
  - [Parallel Processing](#parallel-processing)  
  - [Output Refinement](#output-refinement)  
  - [Post-processing](#post-processing)  
- [Methodology](#methodology)  
- [Folder Structure](#folder-structure)  
- [Conclusion](#conclusion)  

---

## **Introduction**  
The Amazon ML Challenge was a 3-day event, requiring efficient solutions due to constraints on time and resources. Our team utilized pre-trained multimodal models, distributed computing, and advanced post-processing to achieve a high rank.  

---

## **Approach**  

### **Pre-trained Model Selection**  
- Tested multiple multimodal models on training data samples.  
- Chose the quantized **Mini-CPM** model for its superior performance and resource efficiency.  

### **Strategy Development**  
1. Avoided fine-tuning to reduce computational overhead.  
2. Emphasized **prompt engineering** and **post-processing** for optimal results.  

### **Parallel Processing**  
- Dataset split into smaller parts for parallel processing using Kaggle accounts.  
- Merged partial results to accelerate computations and minimize resource usage.  

### **Output Refinement**  
- Introduced the **Gemma 2** model for refining predictions.  
- Customized prompts improved alignment with competition requirements.  

### **Post-processing**  
- Cleaned and formatted predictions to meet submission standards.  
- Final output prepared as a **CSV file**.  

---

## **Methodology**  

The solution pipeline was executed in the following steps:  
1. **Data Segmentation**: Split the dataset into 100 parts.  
2. **Parallel Processing**: Processed 20 segments at a time using Mini-CPM for initial predictions.  
3. **Refinement**: Sent predictions to the Gemma 2 model for further improvement.  
4. **Merging and Formatting**: Combined outputs and formatted them for submission.  

---

## **Folder Structure**  

| **File Name**            | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| `data_analysis.py`        | Performs analysis on the training dataset.                                      |
| `merge_files.py`          | Merges all CSV files into a single file.                                        |
| `split_files.py`          | Splits a CSV file into smaller parts.                                           |
| `amazon_ml_1.ipynb`       | Implements Mini-CPM for visual question answering and initial prediction.       |
| `amazon_llm_1.ipynb`      | Implements Gemma 2 for refining the Mini-CPM output.                           |
| `post_processing.py`      | Processes refined predictions for final submission.                             |  

---

## **Conclusion**  

By leveraging pre-trained models, distributed computing, and effective post-processing, our team successfully managed limited resources while achieving a top 0.1% rank. The Amazon ML Challenge was an excellent platform for innovation and learning.  

**Acknowledgment:** Thank you, Amazon ML Challenge team, for organizing this event!  

---

### **Contact**  
For any queries, feel free to reach out or raise an issue.  
