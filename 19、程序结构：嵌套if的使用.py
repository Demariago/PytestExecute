# demaria
#时间:2023/4/27 15:16
#外分支  内分支

#if 条件1：
#    if 内置条件1;
#       执行内置1
#    else：
#       执行2
#else:
#    执行条件2

#电商，会员的话，200以上打八折，100-200打9折，100以下不打折；非会员，200以上打95折，200以下不打折
print('-----嵌套分支-----')
is_vip=int(input('是会员请按1,非会员请按0:'))
money=int(input('请输入消费金额'))
if is_vip==1:
    if money>=200:
        print('请您支付',money*0.8)
    elif money>=100:#注意，这里不需要再写money<200了，因为大于等于200会执行上面的分支
        print('请您支付',money*0.9)
    else:
        print('请您支付',money)
else:
    if money>=200:
        print('请您支付',money*0.95)
    else:
        print('请您支付',money)
