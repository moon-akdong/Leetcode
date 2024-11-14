class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 문자열 배열을 받아 애너그램 단위로 그룹핑하라. 
        # 알파벳이 동일하게 들어가 있는것들 

        # 문자는 그대로 유지하면서, 같은 것 끼리 묶어야 한다. 
        # 인덱스를 사용? 
        # words_group = collections.defaultdict(list)
        # for i in strs:
        #     word = sorted(i)
        #     if words_group not in words_group.keys(): # time Limit Exceeded
        #         words_group[''.join(word)].append(i)

        # return words_group.values()

        words_group = collections.defaultdict(list)
        for word in strs:
            words_group["".join(sorted(word))].append(word)
        return words_group.values()

        # defaultdict 사용법 , join
        # sort = 리스트 정렬에서는 사용되나 str에서는 안됨, 제자리 정렬 이기 떄문에 리턴값이 없다. list.sort()
        # sorted 문자정렬 가능 list1 = sorted(list)