### 1.Thresholding

>The simplest strategy is to set a distance threshold and accept all matches within this distance. However, it's difficult to set a good universal threshold

### 2.Nearest Neighbour

>A keypoint is matched to its nearest neighbor in the feature space. This is better but can still produce incorrect matches for non-distinctive features

### 3.Nearest Neighbour Distance Ratio (NNDR)

>For a key point, find the distance to its nearest neighbor (d1) and its second-nearest neighbor (d2)
>
>Calculate the ratio NNDR = d1/d2
>
>If the ratio is close to 1, the match is ambiguous and should be reject. If the ratio is low, it is a distinctive, correct match


