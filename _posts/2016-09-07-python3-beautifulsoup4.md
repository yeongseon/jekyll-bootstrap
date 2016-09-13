---
layout: post
title: "Install Beautiful Soup and Python3 on Windows"
description: ""
category: python3-beautifulsoup4
tags: [Python3 beautifulsoup]
---
{% include JB/setup %}

## Python3에서 beautifulsoup 설치하기 (Windows)

#### conda를 이용한 개발환경 생성
<pre>
<code>
conda create -n python3_bs4 python=3
</code>
</pre>

#### 개발환경 활성화 화기
<pre>
<code>
activate python3_bs4
</code>
</pre>

#### 개발환경 비활성화 화기
<pre>
<code>
deactivate python3_bs4
</code>
</pre>

#### beautifulsoup4 설치
<pre>
<code>
conda install beautifulsoup4
</code>
</pre>

#### lxml 설치
beautifulsoup4의 html parser 필요
<pre>
<code>
conda install lxml
</code>
</pre>

#### 설치 확인
<pre>
<code>
import beautifulsoup4
</code>
</pre>

##### 참고자료
* <>
