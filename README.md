# AutoFAQ NLU - https://autofaq.ai/en evaluation benchmarks.

This repo contains evaluation of Autofaq.ai, Cognigy, DialogFlow, Microsoft LUIS and Watson NLU services.

# Data

Data from [Benchmarking Natural Language Understanding Services for Building Conversational Agents (2019)](http://arxiv.org/abs/1903.05566), for details and reproduction see folder [v4](v4/README.md).

## Small subset

640 Training Setences - 10 Sentences per Intent

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
