---
layout: post
comments: true
title: "Sqlalchmey"
description: ""
category:
tags: []
---
{% include JB/setup %}

Title
============

How to install
------------
~~~
  pip install
~~~

How to use
------------

~~~python
from enum import Enum
from sqlalchemy.ext.declarative import declarative_base

from
Base = declarative_base()

Class Process(Base):
  class Status(Enum):
    new = 'new'
    ready = 'ready'
    running = 'running'
    waiting = 'waiting'
    terminated = 'terminated'

  status = Column(db.Enum(Status), default=Status.new.value)

~~~

### Reference
