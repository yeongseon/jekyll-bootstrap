---
layout: post
comments: true
title: "Install OpenCV2 and Python2 on Windows"
description: ""
category:
tags: [Python2, OpenCV2]
---
{% include JB/setup %}

## Python2에서 OpenCV2 설치하기 (Windows)

#### conda를 이용한 개발환경 생성
<pre>
<code>
conda create -n python2_opencv2 python=2
</code>
</pre>

#### 개발환경 활성화 화기
<pre>
<code>
activate python2_opencv2
</code>
</pre>

#### 개발환경 비활성화 화기
<pre>
<code>
deactivate python2_opencv2
</code>
</pre>

#### numpy 설치
python에서 opencv를 설치하기 위해서는 꼭 필요하다.

<pre>
<code>
conda install numpy
</code>
</pre>

#### opencv2 설치
<pre>
<code>
conda install -c https://conda.binstar.org/menpo opencv
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
