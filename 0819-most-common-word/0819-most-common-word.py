class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
        # 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.

        # # , 구두점 무시
        # paragraph = re.sub("[^\w]",' ',paragraph) # [^a-zA-Z ]
        # # 대소문자 구분 하지 않는다.
        # words = paragraph.lower().split()

        # words_counter = collections.Counter(words)
        
        # max_words = ""
        # counter = 0
        # for word,count in words_counter.items():
        #     if word not in banned and counter < count:
        #         counter = count
        #         max_words = word
        # return max_words

        words = [word for word in re.sub("[\w]"," ",paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

        