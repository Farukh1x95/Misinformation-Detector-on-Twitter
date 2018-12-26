#Detecting Misinformation on Twitter 

# Twitter Misinformation Detector
This algorithm is used to detect the fake and falsy tweets by authenticating it by Times of India new API.


# Working
1. It first filters the tweets which are out of the context of the reference news by matching the keywords which are configuralble stated as `SimilarityDegreeValue`.

2. It then apply a function to find the number of negative operations applied to a string and returns if the sentence is **Negative** of **Assertive**.

3. Now after all the tweets are gone through that function now `XOR` operation is applied on each tweet one by one with the news which gives result either one or zero. (Considering 0 as negative news and 1 as positive).

4. If the tweet is negative (0) and News  is positive (1) or vise-versa so their XOR returns 1 and means the tweet is contradicting to the  news so it is false.

# Dependencies

1. NLTK + NLTK Data -> https://www.nltk.org/
2. Pattern -> https://www.clips.uantwerpen.be/pattern

