# Methodology
We reproduce analysis from [Evaluating Natural Language Understanding Services for Conversational Question Answering Systems by Braun, Daniel  and  Hernandez-Mendez, Adrian  and  Matthes, Florian  and  Langen, Manfred (2017)](http://www.aclweb.org/anthology/W17-5522), 

We use our own split for the chat corpus provided in `TransportCorpusSplit.json` as the author's split has not been published and this is the most transparent and reproducible approach. The Ubuntu and Web App corpora use the split from the paper. Note results are therefore not directly comparable to the original paper.

Forking their [NLU-Evaluation-Scripts](https://github.com/sebischair/NLU-Evaluation-Scripts), results are obtained by running the converter scripts, importing and setting up respective bots and finally running the analysis scripts.

We have benchmarked Microsoft LUIS and Google's Dialogflow as of November 2018.

| corpus           | num of intents | train | test |
| ---------------- | -------------- | ----- | ---- |
| Chatbot          | 2              | 100   | 106  |
| Ask Ubuntu       | 5              | 53    | 109  |
| Web Applications | 8              | 30    | 59   |


# Results

The necessary Zip/JSON files to import flows and full annotation and result files are provided in respective folders.

F1-Scores for Cognigy AI, LUIS and DialogFlow as computed in Braun et al.:

| Platform\Corpus | Chatbot | Ask Ubuntu | Web Applications | Overall |
|-----------------|---------|------------|------------------|---------|
| Cognigy NLU 2.0 | 0.97    | 0.91       | 0.92             | 0.93    |
| DialogFlow      | 0.93    | 0.85       | 0.80             | 0.87    |
| LUIS            | 0.98    | 0.90       | 0.81             | 0.91    |
| Watson          | 0.97    | 0.92       | 0.83             | 0.92    |
