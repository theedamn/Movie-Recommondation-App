try:
    import pinecone
    import pandas as pd
    import numpy as np
    from sentence_transformers import SentenceTransformer, util
    from sklearn.metrics.pairwise import cosine_similarity
    from annoy import AnnoyIndex

except Exception as e:
    print("Some Modules are Missing :{}".format(e))


"""**Pinecone Things**"""

pinecone.init(api_key="81947d7f-36e6-4e07-88a7-3d58ff7208b4",environment="asia-southeast1-gcp-free")
index_name = pinecone.Index("try")


"""**Kaggle API to Download dataset**"""

#kaggle datasets download -d kayscrapes/movie-dataset  # should run it in terminal

"""**Loading the Dataset**"""

df=pd.read_csv("Hydra-Movie-Scrape.csv")
df.head()

"""**Importing the Embedding Models from ST And loading Our DataSet to the Model**"""

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
#q1 = model.encode(df['Summary'].tolist())

"""**Once Data is Vectorized we can save to Pinecone database or we can save it locally**"""

# Save the vectors to a file
#np.save("vectors1.npy", q1)

"""**With this command we can directly load local vectors to the program**"""

q1 = np.load("vectors1.npy")


def similarity_search_Cos_Sim(inp,k):
    if len(inp) in range(2):
        return "No Results"
    query = inp
    query_vector = model.encode([query])
    similarity_scores = cosine_similarity(query_vector.reshape(1, -1),q1).flatten()
    sorted_indices = similarity_scores.argsort()[::-1] #This function is used to get index of the vectors so the original data are accessed
    matching_data_title = [df['Title'].tolist()[i] for i in sorted_indices]
    matching_data_summary = [df['Summary'].tolist()[i] for i in sorted_indices]

    # Print the top-k matching data
    top_k = k

    return matching_data_title[:top_k],matching_data_summary[:top_k]


"""**************Below code helps to upload data into the pinecone database**************"""
"""ids = list(str(x) for x in range(len(q1)))  # Generate sequential IDs

    def upload():
        question_list = []
        for i,row in df.iterrows():
          question_list.append(
              (
                str(i),
                q1[i].tolist(),
                {
                    "Title":row['Title'],
                    "Summary": row['Summary']
                }
              )
          ) 
          index_name.upsert(question_list[:580]) #Only this much of data is allowed to upload in DB"""

#upload()

def similarity_search_pinecone(inp,k):
    if len(inp) in range(2):
        return "No Results"
    que=inp
    que=model.encode(que).tolist()
    res=index_name.query(que,top_k=k,include_metadata=True)

    res['matches'][2]['metadata']['Summary']
    id=0
    Title=[]
    summ=[]

    for x in res['matches']:
      Title.append(x['metadata']['Title'])
      summ.append(x['metadata']['Summary'])

    """for x in Title:
      print("Title",Title[id])
      print("Summary",summ[id])
      id+=1"""

    return Title,summ



def similarity_search_ANN(inp,k):
    vector_dim = len(q1[0])
    annoy_index = AnnoyIndex(vector_dim, 'angular')


    for i, vector in enumerate(q1):
        annoy_index.add_item(i, vector)
    num_trees = 100
    annoy_index.build(num_trees)
    query = inp
    query_vector = model.encode([query])[0]
    num_neighbors = k  
    nearest_neighbors = annoy_index.get_nns_by_vector(query_vector, num_neighbors)
    nearest_documents_title = [df['Title'][i] for i in nearest_neighbors]
    nearest_documents_summary = [df['Summary'][i] for i in nearest_neighbors]

    return nearest_documents_title,nearest_documents_summary

    # Print the search results
    """print("Search Results:")
    for i in range(len(nearest_documents_summary)):
        print("Title",nearest_documents_title[i],end=" /n ")
        #print(""nearest_documents_summary[i],end=" /n ")
        print()"""


print("ALL OK")

