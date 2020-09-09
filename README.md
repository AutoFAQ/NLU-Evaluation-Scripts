Cognigy NLU evaluation benchmarks.

# v4

Using data [Benchmarking Natural Language Understanding Services for Building Conversational Agents (2019)](http://arxiv.org/abs/1903.05566), for details and reproduction see folder `v4`.

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



# v3

Using data [Evaluating Natural Language Understanding Services for Conversational Question Answering Systems by Braun, Daniel  and  Hernandez-Mendez, Adrian  and  Matthes, Florian  and  Langen, Manfred (2017)](http://www.aclweb.org/anthology/W17-5522), for details and reproduction see `v3`.

| Platform\Corpus | Chatbot | Ask Ubuntu | Web Applications | Overall |
|-----------------|---------|------------|------------------|---------|
| Cognigy NLU 2.0 | 0.97    | 0.91       | 0.92             | 0.93    |
| DialogFlow      | 0.93    | 0.85       | 0.80             | 0.87    |
| LUIS            | 0.98    | 0.90       | 0.81             | 0.91    |
| Watson          | 0.97    | 0.92       | 0.83             | 0.92    |
