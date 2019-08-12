## Robots协议

好的网络爬虫，首先需要遵守**Robots协议**。Robots协议（也称为爬虫协议、机器人协议等）的全称是“网络爬虫排除标准”（Robots Exclusion Protocol），网站通过Robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取。

在网站根目录下放一个robots.txt文本文件（如 https://www.taobao.com/robots.txt ），里面可以指定不同的网络爬虫能访问的页面和禁止访问的页面，指定的页面由正则表达式表示。网络爬虫在采集这个网站之前，首先获取到这个robots.txt文本文件，然后解析到其中的规则，然后根据规则来采集网站的数据。

### 1. Robots协议规则

```
User-agent: 指定对哪些爬虫生效
Disallow: 指定不允许访问的网址
Allow: 指定允许访问的网址
```

注意: 一个英文要大写，冒号是英文状态下，冒号后面有一个空格，"/"代表整个网站

### 2. Robots协议举例

```
禁止所有机器人访问
	User-agent: *
	Disallow: /
允许所有机器人访问
	User-agent: *
	Disallow: 
禁止特定机器人访问
	User-agent: BadBot
	Disallow: /
允许特定机器人访问
	User-agent: GoodBot
	Disallow: 
禁止访问特定目录
	User-agent: *
	Disallow: /images/
仅允许访问特定目录
	User-agent: *
	Allow: /images/
	Disallow: /
禁止访问特定文件
	User-agent: *
	Disallow: /*.html$
仅允许访问特定文件
	User-agent: *
	Allow: /*.html$
	Disallow: /
```