# dirpy
A little program that is ment to simplify the process of writing web 'hacking' tools for me.
I'm also using it to experiment with software design concepts and OOP programming, so some things are a bit funky as I am learning while I am making it.

## TODO:
* Add more modes:
    Would be nice with some that did alot of predifined things,
    like a 'quick_fuzz' mode that went through cookies, headers, and URL
    and fuzzed them with bad chars or somethingself.
    Should write more simple functionality first so modes that use several
    methods can use them (composition).
   
* Reformat/rewrite get_args.py:
    Should use subparsers for the different modes. Not sure how they work,
    so need to figure that out.
    Maybe make the subparsers classes or something to limit the need to
    rewrite similar parsers by inheriting from them instead.

* Save progress:
    Could implement it with pickle or something, just have to learn how
    that works first.
