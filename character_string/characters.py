#单引号、双引号、三引号
print('hello "python"');
print("hello 'python'");

print('''123
456
789''');
print("""123
456
789""");

#自然字符串r/R
print("hello pyrhon!\nhello world!");
print(R"hello pyrhon!\nhello world!");

#重复运算符
print("hello py!\n"*5);

#子字符串
c = "abcdefghijklnmopqrst";
#索引运算符，从0开始索引
c1 = c[0];
c2 = c[1];
print(c1,c2);
#切片运算符，下标从0~n-1
c3 = c[0:3];
c4 = c[:3];
c5 = c[-3:];
print(c3,c4,c5);