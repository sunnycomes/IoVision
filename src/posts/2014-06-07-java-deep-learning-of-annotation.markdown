---
layout: post
title: "打破沙锅问到底－－Java的@符号"
date: 2014-06-07 14:23:59 +0800
comments: true
tags: Java
---
刚接触Java变成，就经常碰到“@”这个符号，所谓的Java中的annotation。很多时候它都是跟@Override，@Deprecated，@SuppressWarnings，或者更见多识广一些，还有@Retention，@Target，@Documented，@Inherieted，但是，大多数情况下，很少会有人去过问为什么这么去写，只知道这是一种理所当然的写法，在这里推荐一篇非常详细的关于Java注解的博文[Java注解annotation用法和自定义注解处理器](http://computerdragon.blog.51cto.com/6235984/1210969)。

读完上面那篇文章，相信大家应该对Java的注解有了比较初步的认识，当然，光看别人的不行，没有自己的总结体会，等于没有学到太多。

原文中提到“**自定义注解是以@interface为标志的**”，那么，“注释”到底是不是一个interface呢？答案可以从[官方文档](http://docs.oracle.com/javase/tutorial/java/annotations/declaring.html)中找到，“`Annotation types are a form of interface`”，如是写道。

<!-- more -->

原文中定义了一个Constraints的Annotation，当其他Annotation引用它时，却有两种不同的用法，我从原文中复制了这样一段代码

	@Target(ElementType.FIELD)
	@Retention(RetentionPolicy.RUNTIME)
	public @interface SQLString {
    	int value() default 0;
    	String name() default "";
    	Constraints constraints() default @Constraints;
	}
	
想必大家应该注意到了，`Constraints constraints() default @Constraints;
`，这一行中，前一个Constraints是不加“@”，而后面加了，再回忆下最初我们接触到的Override，Deprecated，SupressWarnings，前面都有“@”，这是为什么？目前猜测不加表示“类型”，而加了之后，表示“实例”，有兴趣的读者可以深究下。

看了这么多代码，从头到尾都觉得Annotation type element(官网原话)定义特别怪异，如`int value() default 0;`，自开始学习java编程以来，还从未接触过这种写法，有兴趣的读者可以试着把这段代码放到一个普通的类内部，会是什么效果，肯定报错！[官网](http://docs.oracle.com/javase/7/docs/technotes/guides/language/annotations.html)有这样一段原话,
	
	Annotation type declarations are similar to normal interface declarations. 
	
	An at-sign (@) precedes the interface keyword. Each method declaration defines an element of the annotation type. Method declarations must not have any parameters or a throws clause. 
	
	Return types are restricted to primitives, String, Class, enums, annotations, and arrays of the preceding types. Methods can have default values. 
	
相信已经解答大家的疑惑了。

再啰嗦一句，在Annotation里面，有一个接口很少抛头露面，但有重要到不得不提的地步，它就是`java.lang.annotation.Annotation`，默认的，Override，Deprecated等annotation类型都继承于它，跟java.lang.Object类似。更多详细资料见官网[Interface Annotation](http://docs.oracle.com/javase/7/docs/api/java/lang/annotation/Annotation.html). 值得注意的是，你要是自己写个接口Intf，实现`java.lang.annotation.Annotation`，并不能使Intf成为`java.lang.annotation.Annotation`类型。

最后，可以尝试做下官网提供的小测验，巩固下知识，[地址](http://docs.oracle.com/javase/tutorial/java/annotations/QandE/questions.html)
