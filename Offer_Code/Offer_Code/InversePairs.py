# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 15:27
# @Author  : Shajiu
# @FileName: InversePairs.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""题目:
       在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
       输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
       即输出P%1000000007
"""
"""第一种做法"""
class Solution:
    def InversePairs(self,data):
        count=0
        for i in range(len(data)):
            tmp=data[i]
            for j in range(i,len(data)):
                if tmp>data[j]:
                    count+=1
        result=count%1000000007

        return result

data=[364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
if __name__ == '__main__':
    result=Solution()
    print(result.InversePairs(data))


"""
题目:
    第二种方法：
    
"""
class Solution:
    def InversePairs(self,data):
        count = 0
        global count

        def MergeSort(lists):
            global count
            if len(lists)<=1:
                return lists

            num=int(len(lists)/2)
            left=MergeSort(lists[:num])
            right=MergeSort(lists[num:])
            r,l=0,0
            result=[]
            while l<len(left) and r<len(right):
                if left[l]<right[r]:
                    result.append(left[l])
                    l+=1
                else:
                    result.append(right[r])
                    r+=1
                    count+=len(left)-l
            result+=right[r:]
            result+=left[l:]
            return result
        MergeSort(data)
        return count%1000000007

