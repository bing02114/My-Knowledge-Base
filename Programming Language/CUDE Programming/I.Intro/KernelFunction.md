### 1.定义

>核函数在 **GPU** 上进行 **并行** 执行

### 2.形式

``` c++
__global__ void kernel_function(argument arg)
{
	printf("hello world\n");
}

```

### 3.注意

* 必须使用__global__
* 返回值必须是void, 和global的位置可以互换
* 不可以使用C++的iostream

1. 核函数只能访问GPU内存
2. 核函数不能使用变长参数
3. 核函数不能使用静态变量
4. 核函数不能使用函数指针
5. 核函数具有异步性

### 4.核函数的异步性

```c++
//核函数调用
kernel_function<<<1,1>>>();
//需要和主机代码进行同步
cudaDeviceSynchronize();
```