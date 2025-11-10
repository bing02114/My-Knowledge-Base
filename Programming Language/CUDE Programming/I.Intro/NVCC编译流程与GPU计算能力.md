### 1.NVCC编译流程

1. 分离代码为host和device代码
2. host是c/c++语法，device是c/c++扩展语言编写
3. nvcc先将设备代码编译为PTX代码，再将PTX代码编译为2进制cubin目标代码