import pandas as pd
df = pd.read_csv("/content/drive/MyDrive/Documents/Market Intelligence/datasets/final_combined_dataset.csv")
df = df.iloc[:,1:]
df.head()


from transformers import pipeline
summarizer = pipeline('summarization')

def text_summarizer(text):
  sumr = summarizer(text, max_length=100, min_length=5, do_sample=False, truncation=True)
  
  return sumr[0]['summary_text']


classifier = pipeline('sentiment-analysis')

def text_classifier(text):
  res = classifier(df.iloc[0,2], padding=True, truncation=True)
  
  return res[0]
  
#Question Answering

from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

model = TFAutoModelForQuestionAnswering.from_pretrained(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)

question = pipeline('question-answering', model=model_name, tokenizer=model_name)



QA_input = {
    'question': 'How many Holders were there?',
    'context': df.iloc[0,2]
}

answer = question(QA_input)
answer

#Zero Shot Classification
zero_shot_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


sequence_to_classify = df.iloc[0,2]

candidate_labels = ['environmental', 'fraud', 'regulations']

zero_shot_classifier(sequence_to_classify, candidate_labels)


def change_name_year(df, name, year_list, columns):
  arr = df.to_numpy()

  for row in range(len(arr)):
    for col in range(len(arr[0])):
      if col == 0:
        arr[row][col] = name
      if col == 1:
        arr[row][col] = year_list[row]     

  return pd.DataFrame(arr, columns = columns)  
  
# Returns combined dataset
def combine_dataset(PATH, raw_data_files, company_names_list, year_list):
  for i, (file, company) in enumerate(zip(raw_data_files, company_names_list)):
    df = pd.read_csv(PATH + file)
    df = df.iloc[:,1:]
    # Setting up appropriate names and year
    df = change_name_year(df, company, year_list, columns)

    # Skipping concatenation in the first iteration
    if i == 0:
      arr = df.to_numpy()
    else:
      arr1 = df.to_numpy()
      arr = np.concatenate((arr, arr1), axis = 0)

  return pd.DataFrame(arr, columns = columns)

