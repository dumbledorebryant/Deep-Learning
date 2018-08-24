R-CNN
	Object Detection & Recognition:
(一)Selective Search  /  Exhaustive Search
		shape
		scale
		color
		texture(纹理)
	过分割->保持多样性
	Hierarchical Grouping Algorithm
		1. 色彩空间变换
		2. 多样式距离计算 
		   {
			   a. 颜色距离
			   b. 纹理距离
			   c. 优先合并小的区域(more Weight)
			   d. 区域吻合度(合并后形状规则)
		   }
		输出所有存在过的区域
		即为————(候选区域)
(二)Feature Extraction
	


	    



