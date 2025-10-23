### 1.cv2.BFMatcher

#### 1.1 Goal

>The primary goal of the `cv2.BFMatcher` is to find the best matches between two sets of feature descriptors using a **brute-force**, or exhaustive, search.
>
>The "brute-force" method is very straightforward: for each descriptor in the first set (the "query" set), it iterates through **all** descriptors in the second set (the "train" set) and calculates the distance between them. It then identifies which descriptor in the second set is the closest (i.e., the best match).

#### 1.2 Input

>The input is not provided to the `BFMatcher` object itself during creation, but rather to its matching methods (`.match()` or `.knnMatch()`).

#### 1.3 Parameter Settings

``` python
bf = cv2.BFMatcher(normType, crossCheck)
```

- **`normType`:** This specifies the distance measurement to be used. The choice depends on the type of descriptor.
    
    - **`normType`：** 这个参数指定了要使用的距离度量方式。具体选择取决于描述符的类型。
        
    - **`cv2.NORM_L2`:** The Euclidean distance (L2​ norm). This is the standard choice for continuous descriptors like **SIFT** and **SURF**.
        
        - **`cv2.NORM_L2`：** 欧几里得距离（L2​范数）。这是像 **SIFT** 和 **SURF** 这类连续型描述符的标准选择。
            
    - **`cv2.NORM_L1`:** The Manhattan distance (L1​ norm).
        
        - **`cv2.NORM_L1`：** 曼哈顿距离（L1​范数）。
            
    - **`cv2.NORM_HAMMING`:** The Hamming distance. This should be used for binary descriptors like **ORB, BRIEF, and BRISK**. It counts the number of differing bits between two binary strings.
        
        - **`cv2.NORM_HAMMING`：** 汉明距离。这个应该用于像 **ORB、BRIEF 和 BRISK** 这样的二进制描述符。它计算两个二进制字符串之间不同位的数量。
            
    - **`cv2.NORM_HAMMING2`:** Another variant of the Hamming distance.
        
        - **`cv2.NORM_HAMMING2`：** 汉明距离的另一种变体。
            
- **`crossCheck`:** A boolean value ( `True` or `False` ). Default is `False`.
    
    - **`crossCheck`：** 一个布尔值（`True` 或 `False`）。默认为 `False`。
        
    - If set to `True`, it activates a **consistency check**. A match between descriptor `A` (from the query set) and descriptor `B` (from the train set) is only returned if `B` is the best match for `A` **AND** `A` is the best match for `B`. This is a very effective way to filter out a significant number of false matches. It's a cleaner alternative to the ratio test but can be more restrictive.
        
    - 如果设为 `True`，它会激活一个**交叉检查**。查询集中的描述符`A`和训练集中的描述符`B`之间的匹配，只有在`B`是`A`的最佳匹配 **并且** `A`也是`B`的最佳匹配时，才会被返回。这是一种非常有效的过滤错误匹配的方法。它比率测试更简洁，但也可能更严格。

#### 1.4 Output

##### **Output of `.match(des1, des2)`**

- It returns a **list of `cv2.DMatch` objects**. The number of objects in the list is equal to the number of query descriptors (`N`).
    
- Each `cv2.DMatch` object contains information about a single best match:
    
    - `.queryIdx`: The index of the descriptor in the `queryDescriptors` array.
        
    - `.trainIdx`: The index of the descriptor in the `trainDescriptors` array that it matched with.
        
    - `.distance`: The calculated distance between the two descriptors. **A lower value means a better match.**
        
- **返回一个 `cv2.DMatch` 对象的列表**。列表中对象的数量等于查询描述符的数量 (`N`)。
    
- 每个 `cv2.DMatch` 对象包含一次最佳匹配的信息：
    
    - `.queryIdx`：查询描述符在 `queryDescriptors` 数组中的索引。
        
    - `.trainIdx`：与之匹配的训练描述符在 `trainDescriptors` 数组中的索引。
        
    - `.distance`：两个描述符之间计算出的距离。**值越小，匹配越好。**
        

##### **Output of `.knnMatch(des1, des2, k)`**

- This method is used to find the `k` nearest neighbors for each query descriptor. For the NNDR (Lowe's ratio test), you would set `k=2`.
    
- It returns a **list of lists of `cv2.DMatch` objects**. The outer list has a length of `N`.
    
- Each inner list contains `k` `DMatch` objects, sorted by their distance from best to worst.
    
    - For example, if `k=2`, `matches[i][0]` is the best match (nearest neighbor) for the `i`-th query descriptor, and `matches[i][1]` is the second-best match (second-nearest neighbor).
        
- 这个方法用于为每个查询描述符找到 `k` 个最近邻。对于NNDR（Lowe的比率测试），您需要设置 `k=2`。
    
- **返回一个由 `cv2.DMatch` 对象列表组成的列表**。外层列表的长度为 `N`。
    
- 每个内层列表包含 `k` 个 `DMatch` 对象，按距离从好到坏排序。
    
    - 例如，如果 `k=2`，那么 `matches[i][0]` 就是第 `i` 个查询描述符的最佳匹配（最近邻），而 `matches[i][1]` 则是次佳匹配（次近邻）。