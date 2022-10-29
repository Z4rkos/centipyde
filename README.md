# dirpy
A little program that is ment to simplify the process of writing web 'hacking' tools for me.
I'm also using it to experiment with software design concepts and OOP programming, so some things are a bit funky as I am learning while I am making it.

## TODO:
* Add more modes:
    Would be nice with some that did alot of predifined things,
    like a 'quick_fuzz' mode that went through cookies, headers, and URL
    and fuzzed them with bad chars or something.
    Should write more simple functionality first so modes that use several
    methods can use them (composition).

* Make things prettier:
    Add some color to the output and a banner of some kind. Should also include 
    information about the current settings. and process.

* Reformat/rewrite get_args.py:
    Should use subparsers for the different modes. Not sure how they work,
    so need to figure that out.
    Maybe make the subparsers classes or something to limit the need to
    rewrite similar parsers by inheriting from them instead.

* Save progress:
    Could implement it with pickle or something, just have to learn how
    that works first.

* Make a setup.py:
    Stuff to put things where they should be (like putting 'dirpy' in /bin/).

* Fix/setup a file structure:
    * request_handler.py should be seperated into two or three files and be put into their own directory.
    * A folder for docs.
    * A folder for tests.
    * A folder or file for utility functions and classes.
    
