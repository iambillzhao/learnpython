'''
功能：输入两个整数，按照从大到小的顺序排列
重点：使用split方法切分字符串、把字符串转换成整数、多重赋值、简单分支结构
作者：薛景
最后修改于：2019/05/24
'''

a,b = input("请输入两个整数，用逗号分割：").split(",")
# split方法的功能是使用参数中指定的字符串切割待处理的字符串

a,b = int(a),int(b)
# 因为上一条语句切割完毕后得到的a和b依然是字符串类型的数据，所以需要转换成整数

if b>=a:        # if语句的功能是判定后面的式子是否成立，如果成立则执行包含的语句块
    a,b = b,a   # 通过交换变量a和b的值，保证a一定大于等于b
    '''
    这是Python独有的多重赋值方法，表示把变量b和a中的值同时拿出来赋给a和b
    绝对不能写成以下的形式：
    a = b       # 先将变量b的值赋给a
    b = a       # 再将变量a的值赋给b，因为此时a的值已经被b的值覆盖，所以交换失败
    '''

print("%d >= %d" % (a, b))
# 格式化字符串中“%d”表示该位置应该是一个整数

'''
思考题：若把题目改成输入三个整数，按照从大到小的顺序排列，应该如何修改程序？
'''