# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 16:30
# @Author  : shajiu
# @FileName: idf.py
# @Software: PyCharm
import codecs
import os
import math
import operator
import jieba
import re

"""
功能:计算一个文件夹下的所有文本中词汇的TF-IDF算法
     输入：多个文本和哈工大的停顿词汇库
     输出:每个文件对应的词汇的TF-IDF值
"""

"""
获取停动词表
"""
def read_file(file):
    F=codecs.open(file,"r",encoding="utf-8")
    stop_word_list=[]
    for v in F:
        v=v.strip().rstrip()
        word_list = jieba.cut(v)
        v=" ".join(word_list)
        v=re.sub(" +"," ",v)
        for t in v.split(" "):
            outsw = str(t).replace('\n', '')
            stop_word_list.append(outsw)           #词存储
    return stop_word_list                          #返回停动词表


"""获取文件列表"""
def filelist(filepath):
    filelist_arr=[]
    for root, dirs,files in os.walk(filepath):
        for file in files:
            filelist_arr.append(root+"//"+file)   #存储文件路径
    return filelist_arr


"""
构建语料库
"""

"""去除文章中的停用词"""
def getridofsw(lis, swlist):
    afterswlis=[]
    for v in lis:
        if str(v) in swlist:
            continue
        else:
            afterswlis.append(str(v))
    return afterswlis

""""词汇表"""
def read_corpus(files,stop_word_list):
    alllist=[]
    for file in files:
        wordlist=read_file(file)                #词表
        afterswlis=getridofsw(wordlist,stop_word_list)

        alllist.append(afterswlis)
    return alllist

def freqword(wordlst):
    freword={}
    for v in wordlst:
        if v in freword:
            count=freword[str(v)]
            freword[str(v)]=count+1
        else:
            freword[str(v)]=1
    return freword

"""查出包含该次的文档库"""
def wordinfilecount(v,corpuslst):
    count=0
    for i in corpuslst:
        for j in i:
            if v in set(j): # 只要文档出现该词，这计数器加1，所以这里用集合
                count+=1
            else:
                continue
    return count



"""计算tf_idf"""
def tf_idf(wordlst,files,corpuslst):
    outdic = {}
    dic=freqword(wordlst)  #计算词汇表中的词的个数
    """只要一个即可"""

    for v in set(wordlst):
        tf = dic[str(v)] / len(wordlst)  # 计算TF：某个词在文章中出现的次数/文章总词数

        # 计算IDF：log(语料库的文档总数/(包含该词的文档数+1))
        idf=math.log(len(files)/int(wordinfilecount(str(v),corpuslst)+1))

        tfidf = tf * idf  # 计算TF-IDF
        outdic[str(v)]=tfidf

    orderdic = sorted(outdic.items(), key=operator.itemgetter(1), reverse=True)  # 给字典排序
    return orderdic

def befwry(tfidfdic):
    outall=''
    for i  in tfidfdic:
        ech = str(i).replace("('", '').replace("',", '\t').replace(')', '')
        outall = outall + '\t' + ech + '\n'
    return outall

def wry(txt, path):  # 写入结果txt文件
    f = codecs.open(path, 'w', 'utf8')
    f.write(txt)
    f.close()
    return path

if __name__ == '__main__':
    """获取停动词表"""
    swlist=read_file("./corpus/stopwords-master/hit_stopwords.txt")

    """获取文件列表"""
    filepath = r'./corpus/data'
    files= filelist(filepath)  # 获取文件列表

    corpuslist = read_corpus(files, swlist)  # 建立语料库
    outall=''
    """文件循环"""
    for fl in files:
        tmplst=read_file(fl)
        afterswlis=getridofsw(tmplst,swlist)   #获取每一篇文章
        """传入:文本内容、文件名称、全文内容"""
        tfidfdic = tf_idf(afterswlis, files, corpuslist)  # 计算TF-IDF
        titleary = str(fl).split('\\')
        title = str(titleary[-1]).replace('utf8.txt', '')
        echout = title + '\n' + befwry(tfidfdic)

        print(title + ' is ok!')
        outall = outall + echout

    wrypath = r'./corpus/result/TFIDF.txt'
    print(wry(outall, wrypath) + ' is ok!')