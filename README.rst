==================================
Markdown-Magic for Python-Markdown
==================================

A `Python-Markdown`_ plugin for autocreating memes and finding
the best-fitting gifs for your posts.

**Why?**

In most blogging platforms, putting memes or gifs in your posts is a bit
of a bother. You have to manually search for them, download/generate them, 
then upload them back, or search and paste the url.

This Markdown extension was created to make this process simpler, 
less time-consuming, and more fun!

Installation
------------

Install it using pip::

    $ pip install markdown-magic


Usage
-----

**For memes**

Simply do :code:`[magic] meme: top_text | bottom_text [/magic]`
for whichever meme template you want to use, and markdown-magic
will detect which template to use on its own.

The markdown-magic currently supports the following meme templates:

* Lord of the Rings Boromir - "One does not simply"
* The Most Interesting Man in the World - "I don't always... when I do"
* Ancient Aliens History Channel Guy
* Grumpy Cat
* Buzz Lightyear and Woody from Toy Story - "X, X everywhere"
* Futurama Fry - "Not sure if..."
* Y U NO Guy
* Ned Stark from Game of Thrones - "Brace yourself/yourselves..."
* X all the Y
* Bill Lumburgh from Office Space - "...that would be great"
* The rent is too damn high
* The Big Lebowski - "Am I the only one around here..."
* Matrix Morpheus - "What if I told you..."
* Ain't nobody got time for that
* Heath Ledger Joker - "Nobody bats an eye... everyone loses their minds"

More to be added soon!

**For gifs**

Just type in :code:`[magic] gif: <list of space-separated search parameters> [/magic]`
and markdown-magic will search and use the appropriate gif
according to the given search parameters.

Here's an example on the Python interpreter::

    >>> import markdown
    >>> text = """
    ... [magic] meme: rains | y u no happen during summers [/magic]
    ... Some text here.
    ... [magic] gif: spongebob squarepants [/magic]
    ... """
    >>> print(markdown.markdown(text, extensions=['magic']))
    <p><img alt="meme: rains | y u no happen during summers " src="http://i.imgflip.com/sytk1.jpg" title="meme: rains | y u no happen during summers " />
    Some text here.
    <img alt="gif: spongebob squarepants " src="http://media4.giphy.com/media/acEFQYr6ljKDu/200.gif" title="gif: spongebob squarepants " /></p>


Todo
----

* Expand list of supported memes 
* Find a way to search for xkcd comics and other webcomics efficiently using keywords
* Find more cool things to implement in the [magic] tag


Copyright
---------

Copyright 2015 Radhika Ghosal, all rights reserved.

This software is released under the MIT license.


.. _Python-Markdown: https://github.com/waylan/Python-Markdown
