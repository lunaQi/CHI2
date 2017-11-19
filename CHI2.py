# !/usr/bin/python
# -*- coding: utf-8 -*-

#每个类别下，每个词在多少个文章中出现
dict_1 = {}
with open("wordtimes\\sougou_all" + '\\' + "aoyun_classtimes.txt", 'r') as df1:
    for kv in [d.strip().split('\t') for d in df1]:
        dict_1[kv[0].decode('utf-8')] = kv[1]

dict_2 = {}
with open("wordtimes\\sougou_all" + '\\' + "aoyun_classtimes.txt", 'r') as df2:
    for kv in [d.strip().split('\t') for d in df2]:
        dict_2[kv[0].decode('utf-8')] = kv[1]

dict_3 = {}
with open("wordtimes\\sougou_all" + '\\' + "aoyun_classtimes.txt", 'r') as df3:
    for kv in [d.strip().split('\t') for d in df3]:
        dict_3[kv[0].decode('utf-8')] = kv[1]

dict_4 = {}
with open("wordtimes\\sougou_all" + '\\' + "aoyun_classtimes.txt", 'r') as df4:
    for kv in [d.strip().split('\t') for d in df4]:
        dict_4[kv[0].decode('utf-8')] = kv[1]

dict_5 = {}
with open("wordtimes\\sougou_all" + '\\' + "aoyun_classtimes.txt", 'r') as df5:
    for kv in [d.strip().split('\t') for d in df5]:
        dict_5[kv[0].decode('utf-8')] = kv[1]

dict_6 = {}
with open("wordtimes\\sougou_all" + '\\' + "aoyun_classtimes.txt", 'r') as df6:
    for kv in [d.strip().split('\t') for d in df6]:
        dict_6[kv[0].decode('utf-8')] = kv[1]

dict_7 = {}
with open("wordtimes\\sougou_all" + '\\' + "aoyun_classtimes.txt", 'r') as df7:
    for kv in [d.strip().split('\t') for d in df7]:
        dict_7[kv[0].decode('utf-8')] = kv[1]

dict_8 = {}
with open("wordtimes\\sougou_all" + '\\' + "aoyun_classtimes.txt", 'r') as df8:
    for kv in [d.strip().split('\t') for d in df8]:
        dict_8[kv[0].decode('utf-8')] = kv[1]

dict_9 = {}
with open("wordtimes\\sougou_all" + '\\' + "aoyun_classtimes.txt", 'r') as df9:
    for kv in [d.strip().split('\t') for d in df9]:
        dict_9[kv[0].decode('utf-8')] = kv[1]

dict_10 = {}
with open("wordtimes\\sougou_all" + '\\' + "aoyun_classtimes.txt", 'r') as df10:
    for kv in [d.strip().split('\t') for d in df10]:
        dict_10[kv[0].decode('utf-8')] = kv[1]

for class_num in range(1, 11):  # 这里注意才是1到10  用于遍历每个class词典
    dictname = locals()['dict_' + str(class_num)]  # 超级棒的一个locals()[]，可以这样得到变量的名字
    CHI_dic = {}  # 用于记录这个class中每个词的卡方检验值
    for kv in dictname:  # 遍历这个类别下的每个词，把这个类别下每个词的CHI值比较一下，取前100个
        # print kv  #记录这个单词名称
        kv_out_class = 0  # 统计一个新词时，初始化本类别外用到这个词的文档数目为0  相当于b
        not_kv_out_class = 0  # 统计一个新词时，初始化本类别外没有用到这个词的文档数目为0  相当于d
        kv_in_class = int(dictname[kv])  # 记录在这个分类下包含这个词的文档的数量  相当于a
        # print type(kv_in_class)  #注意这里得到的是str型的，一会儿做减法要类型转换
        ?not_kv_in_class = (locals()['class' + str(class_num) + '_num']) - kv_in_class  ##记录在这个分类下不包含这个词的文档的数量  相当于c
        for class_compare in range(1, 11):
            if class_compare != class_num:
                comparename = locals()['dict_' + str(class_compare)]
                if comparename.has_key(kv):
                    kv_out_class += int(comparename[kv])
                    not_kv_out_class += (locals()['class' + str(class_compare) + '_num']) - kv_in_class

        CHI_dic[kv] = ((kv_in_class * not_kv_out_class - kv_out_class * not_kv_in_class) ** 2) / ((kv_in_class + kv_out_class) * (not_kv_in_class + not_kv_out_class))
        # print kv,CHI_dic[kv]
    # print sys.getdefaultencoding()
    CHI_order = open("CHIorder" + '\\' + 'class' + str(class_num) + "_CHIorder.txt", 'w')
    CHI_order.write(('\n'.join(sorted(CHI_dic, key=CHI_dic.get, reverse=True))).encode('utf-8')) #倒序排列

    fin = open("CHIorder" + '\\' + 'class' + str(class_num) + "_CHIorder.txt", 'r')
    N = int(0.015 * len(locals()['dict_' + str(class_num)]))  # 只取CHI值较大的前0.015个单词
    print "从第%d类中选出%d个关键词" % (class_num, N)
    CHI_order_select = open("CHIorder" + '\\' + 'class' + str(class_num) + "_CHIorder_select.txt", 'w')
    for line in fin.readlines()[0:N]:  # 得到CHI值较大的N个单词作为当前的特征词，N和本类别的单词的数量有关
        CHI_order_select.write(line.strip() + '\n')

