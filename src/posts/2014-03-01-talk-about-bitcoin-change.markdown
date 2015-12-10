---
layout: post
title: "聊一聊比特币找零"
date: 2014-03-01 15:43:56 +0800
comments: true
published: true
categories: 
tags: Bitcoin
---

刚开始接触比特币的时候，一定很多人困惑于比特币的找零，幸好资料很多，随手从网上找了一篇，很详尽[《详解比特币的找零机制》](http://jingyan.baidu.com/article/19192ad84bcd54e53e570729.html)，大家可以做一个入门导读. 当然,要更加详细比特币的技术原理,推荐一本书[《Master Bitcoin》](http://files.brendafernandez.com/Mastering%20Bitcoin/Mastering%20Bitcoin.pdf),这本书从技术人员的角度,探讨比特币究竟是什么,通俗易懂,适合想进一步了解比特币技术实现的人员.当然,要深入挖掘,还是推荐阅读比特币源码.

好了, 针对原文的一些概念, 这里我做一些我的理解. 

原文中, 

>比特币钱包交易100次以上时再次交易后要重新备份钱包. 

值得一提的是, 这里的交易指的是支出, 而不包含接收. 其实, 这只是客户端的技术实现问题, 因为客户端将找零的比特币发送到了私钥池中的某一个相关公钥地址, 而私钥池大小只有一百个, 因此, 一旦多于100个, 就可能产生问题. 其实, 客户端也可以设计成将找零的比特币发送回原来的地址. 如blockchain. info网站的钱包, 就是将找零的货币原路返回, 这样做的好处就是交易过程清晰明朗. 不知道大家有没有注意到，原文中始终没有提到为什么要创建新地址接收余额，为什么？理论上，新地址和旧地址(支付地址)接收余额性质是一样的，技术上实现也是没有问题的，聪明的你不知道有没有注意到一个问题，比特币是匿名币，非常注重**隐私**，匿名不止体现在比特币地址上，还体现在找零机制,引用比特币[官网](https://en.bitcoin.it/wiki/Securing_your_wallet)上的一段话:

>This is an anonymity feature – it makes tracking Bitcoin transactions much more difficult.

<!-- more -->

这里再额外的说明下比特币中非常重要的一个概念`UTXO`, Unspent Transaction Output, 这对理解比特币余额非常有意义, 一个钱包地址有多少钱, 是通过计算所有UTXO之和得到的结果. 这里首先明白另外一个概念[Transaction](https://en.bitcoin.it/wiki/Transaction), 可理解为交易, 结构如下:

<script src="https://code.csdn.net/snippets/680184.js"></script>

里面有两个比较重要的知识点: `Input`和`Output`, `Input`写明这个地址的钱来自哪一次Transaction的哪一个`Output`, 如果有兴趣, 可以不断的往前回溯, 最终发现来自叫做[Coinbase](https://en.bitcoin.it/wiki/Coinbase)的东西; 而`Output`表示这个钱转移的地址, 并且, `scriptPubKey`中申明了如果要使用这部分钱, 得满足这些条件. 

再回到UTXO, 上面提到, `Input`写明这个地址的钱来自哪一次Transaction的哪一个`Output`中来的, 这个Output如果是UTXO, 则这笔钱是Unspent状态, 未被使用, 则可用于支付. 假如你有一个新钱包地址ADDR, 张三给你发了1BTC, 这就是一次交易, 记作TXa;李四给你发了2BTC, 记作TXb, 那么如果你没有消费掉这两笔钱, 则你的钱包地址相关的UTXO有两个, 一个在TXa中, 记为UTXOa, 另外一个在TXb中, 记为UTXOb, 则钱包最终余额为`UTXOa + UTXOb = 3BTC. 另外, 如果你有兴趣, 可以去[blockexplorer.com](blockexplorer.com)查一下, 在blockchain中, [Genesis Block](http://blockexplorer.com/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)的挖矿奖励是unspent状态, 这笔钱最后会是什么状态, 耐人寻味, 如果我是那个拥有者, 或许我会一直保留. 当然, 如果这笔钱被消费掉, 也是意义非凡. 

原文中举了一个买棒棒糖的例子, 

>新创建的货币金额与被销毁的货币金额是完全一样的. 

这种说法其实很符合比特币中的做法. 再次提到上面的UTXO的, 假如某个Transactionx中的Input引用了UTXOa, 并且Transactionx已经记录到blockchain, 即总账簿(ledger), 并且已经有多个确认, 一般是6个, 则UTXOa状态变为Spent.　这其实也是比特币网络记账的奥秘所在, 与常规的记账系统有明显的区别, 即不修改已有的Block记录, 而是往账本[Ledger]追加, 这也体现比特币极高的安全特征. 这里提一句, `output`在blockchain中不会有spent或unspent状态, 得通过计算得到, 这里, spent状态对应销毁UTXOa. 而新建的货币, 则通过Output记录的形式, 成为新的UTXO, 当然, 大部分情况, 大于Output总和, 这是由于需要支付Transaction Fee, 当然, 也可不支付手续费, 比特币有史以来[最大的Transaction](https://blockchain.info/tx/1c12443203a48f42cdf7b1acee5b4b1c1fedc144cb909a3bf5edbffafb0cd204)就没有手续费. 这里, 矿工会综合Transaction Fee和Transaction Size进行优先级排序, 但一般来说, Transaction Fee为0的Transaction最终也会被确认. 

我们之前经常提到确认(Confirmation)`这个概念, 这到底是什么意思呢? 是blockx被多少矿工收到? 非也, 其实是blockx相对最新的block_latest的深度, 假如在blockx被计算出来并且广播后, 在它后面有几个block, 就表示被确认了几次. 

还有一个`Transaction Fee`的问题, 矿工是如何收到这笔钱的, 为什么你的Transaction没有写这部分的去向? 其实, 旷工是通过将一个block中所有Transaction Fee加起来, 并且加上此次挖矿的奖励(如25BTC, 当前2014年3月), 单独创建一个Transaction, 转移到自己的钱包地址, 这笔Transaction位于每一个block的第一条记录, 如这次[交易](http://blockexplorer.com/block/0000000000000000bc7b8f8b4a60aeb73c05de005797af3b78e84d61c93f3d15). 你肯定很好奇, 矿工挖矿的比特币, 需要几个确认才能使用, 能立马花掉吗? 答案是否定的, 在比特币程序里面, 明确定义了, 矿工的收益需要100个Confirmation之后, 才能使用, 这也是为什么, 从Genesis Block到后面的100个blcok之间, 都没有任何人为的Transaction, 只有挖矿产生的Transaction. 

>同时为了防止双重支付和伪造, 必须确保在任何时候, 新创建的货币金额与被销毁的货币金额是完全一样的. 

UTXO一旦被引用, 并且Transactionx得到Confirmation, 则UTXO变为spent状态, 即被销毁, 那么, 另外一个Transactiony要引用UTXO, 则被认为不合法, 及双重支付将变得难以实现. 但是并不是说, 不可能发生, 如果你在比特币里听过`Fork`这个词汇, 则双重支付存在一定的可能性, 但是极小, 为了安全起见, 一般要求6个Confirmation, 才算Transaction真正被blockchain认可. 

关于`Fork`, 由于是分布式账本(ledger), 可能会因为延时等原因, 造成信息不同步, 同一个block height有两个block, 即两个block的previous block hash指向同一个block. 后期, 其中一个会成为[Orphaned Block](https://blockchain.info/orphaned-blocks). 那么Orphaned Block中的Transaction呢? 一旦一个block成为Orphaned Block, 其中所有的Transaction都会被释放, 重新计算, 这也造成了double spends难以实现, 除非某个矿工拥有51%的全网算力, 这也就是我们常说的[51% Attack](http://learncryptography.com/51-attack/). 

###References

[1. Transaction](https://en.bitcoin.it/wiki/Transaction)  
[2. Example of multi input address](https://blockchain.info/tx/9da25d3d2ad74e264bcaf4c1cbd810799e9da36d061eceaeb2b1da1fbd0924e2)  
[3. How to convert bitcoin public key to address](http://gobittest.appspot.com/Address)
