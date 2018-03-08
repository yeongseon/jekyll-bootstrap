---
layout: post
comments: true
title: "Alembic"
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
from sqlalchemy.sql import table, column
from sqlalchemy import String
from alembic import op

connection = op.get_bind()

account = table('account',
	        column('name', String))
op.execute(
	accout.update().\
            where(account.c.name == op.inline_liternal('acount 1')).\
	    values({'name':op.inline_liternal('account 2')})	
	)
~~~

### Reference
[1] http://alembic.zzzcomputing.com/en/latest/ops.html
