# Methodology
We reproduce analysis from [Evaluating Natural Language Understanding Services for Conversational Question Answering Systems by Braun, Daniel  and  Hernandez-Mendez, Adrian  and  Matthes, Florian  and  Langen, Manfred (2017)](http://www.aclweb.org/anthology/W17-5522), 

We use our own split for the chat corpus provided in `TransportCorpusSplit.json` as the author's split has not been published and this is the most transparent and reproducible approach. Note results are not directly comparable to the original paper.

Forking their [NLU-Evaluation-Scripts](https://github.com/sebischair/NLU-Evaluation-Scripts), results are obtained by running the converter scripts, importing and setting up respective bots and finally running the analysis scripts.

We have benchmarked Microsoft LUIS and Google's Dialogflow as of June 2018.

| corpus           | num of intents | train | test |
| ---------------- | -------------- | ----- | ---- |
| Chatbot          | 2              | 100   | 106  |
| Ask Ubuntu       | 5              | 53    | 109  |
| Web Applications | 8              | 30    | 59   |


# Results

The necessary Zip/JSON files to import flows and full annotation and result files are provided in respective folders.

F1-Scores for Cognigy AI, LUIS and DialogFlow as computed in Braun et al.:

| Platform\Corpus  | Chatbot | Ask Ubuntu | Web Applications | Overall |
| ---------------- | ------- | ---------- | ---------------- | ------- |
| Cognigy          | 1.00    | 0.86       | 0.83             | 0.88    |
| Luis             | 1.00    | 0.88       | 0.78             | 0.87    |
| DialogFlow       | 1.00    | 0.80       | 0.76             | 0.83    |
