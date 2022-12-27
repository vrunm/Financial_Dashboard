# Financial_Dashboard

**Sentiment Analysis**

The RoBERTa, FinBERT and DistilBERT models were fine-tuned for sentiment analysis. The best results were obtained using the fine-tuned DistilBERT model. It achieved an Accuracy of 91.11% and an ROC-AUC Score of 0.972.

**Summarization**

The T5, DistilPEGASUS and DistilBART models were fine-tuned for summarization. The best results were obtained using the fine-tuned DistilBART model. It achieved an ROUGE-L Score of 67.7%.

**Identifying Important Keywords**
RAKE NLTK was used to identify important keywords from the generated summaries.



A financial dashboard that consolidates all of a business's critical observations in one place using the information obtained from the annual 10K Filings of the companies.
The financial dashboard contains:
- **Insights and summaries** for different sections from annual corporate filings.
- Identification of **important topics and named entities** mentioned in the report.
- **Sentiment-based score** that measures the company's performance over a certain time period.

The Financial Dashboard for Market Intelligence has been deployed on Streamlit.

The app can be viewed here: [Financial Dashboard](https://vrunm-financial-dashboard-app-05vytr.streamlit.app/)


