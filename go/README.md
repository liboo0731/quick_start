### go学习进阶

### 包

`os/user` user包允许通过名称或ID查询用户帐户

`os/exec` exec包执行外部命令。它包装了os.StartProcess函数以便更容易的修正输入和输出，使用管道连接I/O，以及作其它的一些调整。

`os`

`net/http`

`io/ioutil`

`fmt`

`sync` sync包提供了基本的同步基元，如互斥锁。除了Once和WaitGroup类型，大部分都是适用于低水平程序线程，高水平的同步使用channel通信更好一些。

`github.com/gin-gonic/gin` web框架

`github.com/jinzhu/gorm` orm框架

### 函数

`panic` 捕获异常，终止执行

`defer` 延迟执行，程序结束或者异常退出时

`recover` defer方法中接收panic入参，保证程序正常往下执行

  
