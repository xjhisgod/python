#列表，初始化后，可以修改其内容
students = ["小明", "小花", "小李", "小云", "小梅"];
print(students[3]);

students[3] = "小鞋";
print(students[3]);

#元组，定义后，不可修改其内容
teachers = ("张老师", "姚老师", "王老师", "陈老师", "段老师");
print(teachers[3]);

#集合
a = set("hello");
b = set("world!");
#交集
x = a & b;
print(x);
#并集
y = a | b;
print(y);
#差集
z = a - b
print(z);
#去除重复元素
new = set(a);
print(new);

#字典
Dictionaries = {"name":"xjh", "home":"gaozhou", "hobby":"music"};
print(Dictionaries["name"]);
#添加字典里面的项
Dictionaries["work"] = "Coder";
print(Dictionaries["home"]);
print(Dictionaries["work"]);
