import pickle


with open('big_optimal_model.pkl', 'rb') as model:
    optimal_model=pickle.load(model)

def get_topic_json(optimal_model):	#creates a file of the topics and keywords
        topic_obj = []

        for item in (optimal_model.print_topics()):
            word_lst = []
            topic_name, tmp = item
            word_freq = tmp.split(" + ")

            # print(word_freq)
            result_words = [i.split('*')[1] for i in word_freq]
            result_nums = [i.split('*')[0] for i in word_freq]
            #
            # print("words: ",result_words)
            # print("nums: ",result_nums)
            # print()
            dict_wordsfreq = dict(zip(result_words, result_nums))
            word_lst = []

            for word, freq in dict_wordsfreq.items():

                word_obj = Word(word=word, frequency=freq)
                # print(tmp)
                word_lst.append(word_obj)


            topic_obj = Topic(keywords=word_lst, topic=topic_name)

        topics_obj = Topics(document=filename, data=topic_obj)

        t

        # topics_obj.save()

get_topic_json(optimal_model)
