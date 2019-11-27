1.css 选择器优先级
	>计算权重确定
	>！important
	>写在dom上的样式
	>同样的优先级，后写的生效。
2.雪碧图作用：
	>利用background/background-position 将图标定位在图片上，减少http请求数，提高加载性能。
3.base64的使用：
	>用于减少http请求
	>适用于小图片
	>base64图片的体积会增大1/3 
4.如何美化checkbox:
	>label[for]和id
	>隐藏原生input
	> :checked + label
	