# AXI2S寄存器规划 #

0. Base Address 0
1. Size 256字节
1. 32位寄存器
2. 方向问题：假设Q7是无线收发器，T对应输出，R对应输入
3. 输入使能 Ien/Ren
4. 输出使能 Oen/Ten
5. 输入缓冲区起始地址
6. 输出缓冲区起始地址
7. 输入缓冲区长度
8. 输出缓冲区长度
9. TDD/TDMA 模式
10. Frame 长度
11. 时间调整
12. TStart/TEnd
13. RStart/REnd



----------

* AXI2S_EN	`0`	
>     bit 0：Ien高有效
>     bit 1：Oen高有效
>     bit 2：TDD/TDMA模式，高有效
>     --------------	
>     只写,缺省值全0


* AXI2S_IBASE	`10`	
>     输入缓冲区起始地址，32位地址，32bit对齐，最好是4K对齐	
>     --------------	
>     只写，缺省值0xfffc0000


* AXI2S_ISIZE	`14`	
>     输入缓冲区长度，32位，低6位全零，高8位全0	
>     --------------	
>     只写，缺省值0x10000

* AXI2S_OBASE	`18`
>     输出缓冲区起始地址，32位地址，32bit对齐，最好是4K对齐	
>     --------------	
>     只写，缺省值0xfffd0000

* AXI2S_OSIZE	`1C`	
>     输出缓冲区长度32位，低6位全零，高8位全0	
>     --------------	
>     只写，缺省值0x10000

** 注：TDD部分没有实现 **
* FRAME_LEN	`20`	
>     帧长度，单位chip数，有效长度24位	
>     --------------	
>     只写，缺省值1920

* FRAME_ADJ	`24`
>     单位chip数	
>     --------------	
>     只写

* TSTART	`30`	
>     单位chip数	
>     --------------	
>     只写

* TEND	`34`	
>     单位chip数	
>     --------------	
>     只写

* RSTART	`38`
>     单位chip数	
>     --------------	
>     只写

* REND	`3C`	
>     单位chip数	
>     --------------	
>     只写

* AXI2S_STATE	`0`	
>     bit 0：Ien
>     bit 1：Oen
>     bit 2：TDD/TDMA模式
>     bit 4: 0,TDD模式下帧调整完成|1，调整pending	
>     --------------	
>     只读

* AXI2S_IACNT	`10`
>     AXI写地址，低6位全0	
>     --------------	
>     只读

* AXI2S_IBCNT	`14`	
>     写计数	
>     --------------	
>     只读

* AXI2S_OACNT	`18`	
>     AXI读地址，低6位全0	
>     --------------	
>     只读

* AXI2S_OBCNT	`1C`	
>     读计数	
>     --------------	
>     只读
 

# AD9361寄存器规划 #

0. Base Address 0x100
1. Size 256字节
1. 32位寄存器
2. 复位
3. 使能

----------

* AD9361_RST	`0`	
>     bit 0：低复位
>     --------------	
>     只写,缺省值0x1


* AD9361_EN	`10`	
>     bit 0：高使能
>     --------------	
>     只写,缺省值0x0

* AD9361 TX_RX	`20`	
>     bit 0：0-Rx 1-Tx
>     When using FDD (register 0x013[0] = 1), FDD TXON/RXON Independent Control mode allows the receive chain and transmit chain to be enabled independently. This mode is enabled by setting register 0x015[7] =1. Note, SPI writes must be used to move the ENSM into the FDD state. The ENABLE and TXNRX pins are remapped to RXON and TXON, respectively. 
>     --------------	
>     只写,缺省值0x0

* AD9361 EN_AGC	`30`	
>     bit 0：1-AGC 0-MGC
>     --------------	
>     只写,缺省值0x0

* RF CNTL IN	`40`	
>     bit 3-0：
>     --------------	
>     只写,缺省值0x0