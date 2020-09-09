# Cognigy v4

## Methodology
We evaluate F-scores on a small and large dataset based on the home automation bot dataset from [“Benchmarking Natural Language Understanding Services for Building Conversational Agents (2019)](http://arxiv.org/abs/1903.05566) - Their data is [available on github](https://github.com/xliuhw/NLU-Evaluation-Data).


The benchmarked was conducted between 2nd and 6th of July 2020.

Full evaluation logs, with exact scores, timestamps and results are found in the logs folder and excel sheet.

## Small

640 Training Setences - 10 Sentences per Intent

1076 Test Sentences

|            | Cognigy | DialogFlow | Microsoft LUIS | Watson |
|------------|---------|------------|----------------|--------|
| Accuracy   | 0.751   | 0.656      | 0.655          | 0.69   |
| F1 (macro) | 0.748   | 0.657      | 0.641          | 0.686  |


## Large

1908 Training Setences - ~30 Sentences per Intent
5518 Test Sentences

|            | Cognigy | DialogFlow | Microsoft LUIS | Watson |
|------------|---------|------------|----------------|--------|
| Accuracy   | 0.846   | 0.761      | 0.788          | 0.81   |
| F1 (macro) | 0.827   | 0.758      | 0.776          | 0.804  |


# References

[1] Liu, Xingkun, Arash Eshghi, Pawel Swietojanski, and Verena Rieser. 2019. “Benchmarking Natural Language Understanding Services for Building Conversational Agents.” ArXiv:1903.05566 [Cs], March. http://arxiv.org/abs/1903.05566.
