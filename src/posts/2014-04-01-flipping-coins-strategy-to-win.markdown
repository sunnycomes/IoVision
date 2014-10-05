---
layout: post
title: "抛硬币也能抛出人生大赢家"
date: 2014-04-01 23:25:39 +0800
comments: true
tags: Gamble 
---
抛硬币，玩家庄家概率对半开，怎么赢，关键看下注策略。资金管理领域，有两种不得不提的策略，等价鞅与反等价鞅，从表现形式看，使用等价鞅制度的资金管理方式，在出现亏损以后，倾向于使用增加投入金额的方式进行后来的游戏。一旦获得盈利后，资金投入比例会再次回到起始水平；使用反等价鞅制度的资金管理方式，在出现亏损以后，会倾向于减少投入金额的比例进行后来的游戏；而伴随盈利的增加，也会不断增加投入资金，更多相关的内容见[等价鞅和反等价鞅](http://bluema75.blog.163.com/blog/static/386767082007101710422663/)，写的很精彩，不做赘述。在这里，抛硬币属于古典概型，理解起来，相对简单直观。


游戏开始，你有10000块钱，资金翻倍后离场，不然一直到次数上限

等价鞅策略：

	1:如果前一次赢了，本次下注金额为1元。
	2:如果前一次输了，本次下注金额为之前两倍，这样做到本次赢了，能把之前输的都回本。
	3:第一次玩时，认为前一次是赢的，因此，开局赌注为1元。

<!-- more -->

代码：

	package com.iovi.flippingcoins;

	/**
 	  * @author sunnycomes
 	  *
 	*/
	public class FlippingCoins {
	
		public static final int INIT_FUNDS = 10000;
		public static final int PREFERED_FUNDS = INIT_FUNDS * 2;
		
		public static final int MAX_TEST_CASE_CNT = 100;

		// This value is related to PREFERED_FUNDS if you think carefully.
		public static final int MAX_FLIPPING_CNT_IN_ONE_TEST_CASE = 20000;
		
		public static void main(String[] args) {
			
			for(int testCnt = 0; testCnt < MAX_TEST_CASE_CNT; testCnt++) {
				
				int funds = INIT_FUNDS;
				int lastResult = 1;
				int lastChip = 1;
				int flipCnt = 0;
				
				while(funds <= PREFERED_FUNDS) {
					
					if(flipCnt >= MAX_FLIPPING_CNT_IN_ONE_TEST_CASE) {
						//System.err.print("Max flipping count in one test case reached#");
						break;
					}
					flipCnt ++;
					
					lastChip = lastResult == 1 ? 1 : lastChip * 2;
					if(funds < lastChip) {
						//System.err.print("No enough funds for next round#");
						break;
					}
					
					lastResult = getResult();
					funds = lastResult == 1 ? funds + lastChip : funds - lastChip;
				}
				
				if(funds > PREFERED_FUNDS) {
					System.out.println("flipCnt=" + flipCnt + "#funds=" + funds);
				}
				
				//System.out.println("flipCnt=" + flipCnt + "#funds=" + funds);
			}
		}
		
		/**
		 * The method is designed to create a random result simulating the coin flipping result.
		 * 
		 * @return a pseudorandom int either 1 or 0, 1 stands for win and vice versa.
		 */
		public static int getResult() {
			return (int) (Math.random() + 0.5);
		}
	}


听网友反馈，测试结果不理想，最后产生了亏损，这其实是可能发生的，要体现策略的效果，首先，初始资金要充足，而后，测试的用例必须保证充足。要理解一个概念，产生了一列随机数，测试次数远远不够，要搞清楚一个概念。概率和运气：概率是你抛1w次硬币，正反面对半开，而关于运气，则是前5k次是正面，后5k次是反面。你只测了一列随机数，不具有代表性。

另外，还推荐一篇比较不错的关于资金管理的文章[【干货】关于等价鞅、反等价鞅、剀利公式、赌徒输光定理](http://blog.sina.com.cn/s/blog_4b9aa4250101k4q5.html)
