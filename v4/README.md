# AutoFAQ v4

## Methodology
We evaluate F-scores on a small and large dataset based on the home automation bot dataset from [“Benchmarking Natural Language Understanding Services for Building Conversational Agents (2019)](http://arxiv.org/abs/1903.05566) - Their data is [available on github](https://github.com/xliuhw/NLU-Evaluation-Data).


The benchmark of Cognigy, DialogFlow, Microsoft LUIS and Watson was conducted between 2nd and 6th of July 2020. See more details in https://github.com/Cognigy/NLU-Evaluation-Scripts.

The benchmark of AutoFAQ was conducted in August 2021.

Full evaluation logs, with exact scores, timestamps, results, training and test sets are found in the large/ and small/ folders.

autofaq.ipynb notebook contains code to reproduce results using https://autofaq.ai/en platform.

## Small subset

640 Training Setences - ~10 Sentences per Intent

1076 Test Sentences

|            | AutoFAQ | Cognigy | DialogFlow | Microsoft LUIS | Watson |
|------------|---------|---------|------------|----------------|--------|
| Accuracy   | 0.808   |  0.751  | 0.656      | 0.655          | 0.69   |
| F1 (macro) | 0.785   |  0.748  | 0.657      | 0.641          | 0.686  |


## Large subset

1908 Training Setences - ~30 Sentences per Intent
5518 Test Sentences

|            | AutoFAQ |Cognigy  | DialogFlow | Microsoft LUIS | Watson |
|------------|---------|---------|------------|----------------|--------|
| Accuracy   | 0.854   | 0.846   | 0.761      | 0.788          | 0.81   |
| F1 (macro) | 0.846   | 0.827   | 0.758      | 0.776          | 0.804  |


# References

[1] Liu, Xingkun, Arash Eshghi, Pawel Swietojanski, and Verena Rieser. 2019. “Benchmarking Natural Language Understanding Services for Building Conversational Agents.” ArXiv:1903.05566 [Cs], March. http://arxiv.org/abs/1903.05566.

[2] Benchmarking NLU Engines: A Comparison of Market Leaders, https://www.cognigy.com/blog/benchmarking-nlu-engines-comparing-market-leaders

[3] AutoFAQ — AI-powered knowledge base service for employee and customer support via digital communication channels, https://autofaq.ai/en