---
layout: post
title: "聊一聊不一样的比特币找零机制"
date: 2014-03-01 15:43:56 +0800
comments: true
published: true
categories: 
tags: Bitcoin
---

刚开始接触比特币的时候，一定很多人困惑于比特币的找零，幸好资料很多，随手从网上找了一篇，很详尽[《详解比特币的找零机制》](http://jingyan.baidu.com/article/19192ad84bcd54e53e570729.html)，大家可以做一个入门导读。
当然,要更加详细比特币的技术原理,推荐一本书[《Master Bitcoin》](http://files.brendafernandez.com/Mastering%20Bitcoin/Mastering%20Bitcoin.pdf),这本书从技术人员的角度,探讨比特币究竟是什么,通俗易懂,适合想进一步了解比特币技术实现的人员.当然,要深入挖掘,还是推荐阅读比特币源码.

好了，针对原文的一些概念，这里我做一些我的理解。

<!-- more -->

原文中，

>比特币钱包交易100次以上时再次交易后要重新备份钱包。

值得一提的是，这里的交易指的是支出，而不包含接收。其实,这只是客户端的技术实现问题,因为客户端将找零的比特币发送到了私钥池中的某一个相关公钥地址,而私钥池大小只有一百个,因此,一旦多于100个,就可能产生问题. 其实,客户端也可以设计成将找零的比特币发送回原来的地址.如blockchain.info网站的钱包,就是将找零的货币原路返回,这样做的好处就是交易过程清晰明朗. 

	这里再额外的说明下比特币中非常重要的一个概念`UTXO`, Unspent Transaction Output, 这对理解比特币余额非常有意义,一个钱包地址有多少钱,是通过计算所有UTXO之和得到的结果. 

这里首先明白另外一个概念[Transaction](https://en.bitcoin.it/wiki/Transaction), 可理解为交易, 结构如下:

<script src="https://code.csdn.net/snippets/680184.js"></script>

里面有两个比较重要的知识点: `Input`和`Output`, `Input`写明这个地址的钱来自哪一次Transaction的哪一个`Output`,如果有兴趣,可以不断的往前回溯,最终发现来自叫做[Coinbase](https://en.bitcoin.it/wiki/Coinbase)的东西; 而`Output`表示这个钱转移的地址,并且,`scriptPubKey`中申明了如果要使用这部分钱,得满足这些条件.

在回到UTXO, 上面提到,`Input`写明这个地址的钱来自哪一次Transaction的哪一个`Output`中来的, 这个Output如果是UTXO,则这笔钱是Unspent状态, 未被使用, 则可用于支付.

假如你有钱包地址ADDR,张三给你发了1btc, 这就是一次交易,记作TXa;李四给你发了2btc,记作TXb, 那么如果你没有消费掉这

假如你有一个比特币地址,别人分别分两次给你发送

矿工如何获得报酬.

原文中举了一个买棒棒糖的例子，

>新创建的货币金额与被销毁的货币金额是完全一样的。

这种说法其实不对，这里根本没有销毁和创建一说，无非是原地址比特币数字归零，余额赋值到新地址，正是因为原文中的说法，导致很多人以为比特币是完整不可分割。

原文中，

>同时为了防止双重支付和伪造，必须确保在任何时候，新创建的货币金额与被销毁的货币金额是完全一样的。

“销毁”和“创建”金额相同，跟双重支付和伪造够不成因果关系，确认交易和防止双重支付主要是有PROOF-OF-WORK机制保证的，就是常说的PoW。

不知道大家有没有注意到，原文中始终没有提到为什么要创建新地址接收余额，为什么？理论上，新地址和旧地址(支付地址)接收余额性质是一样的，技术上实现也是没有问题的，聪明的你不知道有没有注意到一个问题，比特币是匿名币，非常注重**隐私**，匿名不止体现在比特币地址上，还体现在找零机制,引用比特币[官网](https://en.bitcoin.it/wiki/Securing_your_wallet)上的一段话:

>This is an anonymity feature – it makes tracking Bitcoin transactions much more difficult.
