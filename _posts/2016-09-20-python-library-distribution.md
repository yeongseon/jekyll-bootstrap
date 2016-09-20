---
layout: post
title: "Distribute python library"
description: ""
category: python-general
tags: [Python3, setup.py, distutils]
---
{% include JB/setup %}

## Python에서 라이브러리 배포하는 방법

#### 디렉토리 구성
다음과 같이 디렉토리 구성이 되어 있다.
<pre>
py_test/
    LICENSE
    README.md
    testpkg/
    requirements.txt
</pre>

#### setup.py 생성

<pre>
<code>
from distutiles.core import setup

setup(
  name='py_test',
  version='0.0.1',
  pakages=['testpkg'],
  )
</code>
</pre>

#### setup.py 실행
<pre>
<code>
python setup.py sdist
</code>
</pre>

#### 결과확인
py_test/dist 디렉토리가 생성되며, 그 안에는 testpkg-0.0.1.tar.gz나 testpkg-0.0.1.zip이 생성됨을 알 수 있다.
