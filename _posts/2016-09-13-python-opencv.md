---
layout: post
comments: true
title: "Python OpenCV"
description: ""
category:
tags: [Python3, OpenCV3]
---
{% include JB/setup %}

## Python3에서 OpenCV 설치하기 (Windows)

#### conda를 이용한 개발환경 생성
<pre>
<code>
conda create -n python_opencv Python3
</code>
</pre>

#### 개발환경 활성화 화기
<pre>
<code>
activate python_opencv
</code>
</pre>

#### numpy 설치
python에서 opencv를 설치하기 위해서는 꼭 필요하다

<pre>
<code>
conda install numpy
</code>
</pre>

#### opencv3 설치
<pre>
<code>
conda install -c https://conda.binstar.org/menpo opencv3
</code>
</pre>

##### 참고자료
* <http://nixeneko.hatenablog.com/entry/2016/01/20/012509>
