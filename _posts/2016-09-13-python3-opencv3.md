---
layout: post
comments: true
title: "Install OpenCV3 and Python3 on Windows"
description: ""
category: python-opencv
tags: [Python3, OpenCV3]
---
{% include JB/setup %}

## Python3에서 OpenCV3 설치하기 (Windows)

#### conda를 이용한 개발환경 생성
<pre>
<code>
conda create -n python3_opencv3 python=3
</code>
</pre>

#### 개발환경 활성화 화기
<pre>
<code>
activate python3_opencv3
</code>
</pre>

#### 개발환경 비활성화 화기
<pre>
<code>
deactivate python3_opencv3
</code>
</pre>

#### numpy 설치
python에서 opencv를 설치하기 위해서는 꼭 필요하다.

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

#### 설치 확인
cv 버전 정보 확인
<pre>
<code>
import cv2
cv2.__version__
</code>
</pre>

##### 참고자료
* <http://nixeneko.hatenablog.com/entry/2016/01/20/012509>
