# md-to-html-tree
Creates a whole markdown documentation based on markdown files

## If you want to make some change, always pass the unittest:

```
python -m unittest
```

## Relationship to the project markdown_html_converter

The project [markdown_html_converter](https://github.com/AumitLeon/markdown_html_converter) from Github user [AumitLeon](https://github.com/AumitLeon) is a benchmark project.

Supposedly, this project offered exact what I needed, as the one project that was the easiest to search in Google, written in Python, to make such task.

But there are things that bore me a little:

* The need always to provide an output name to the output file instead to use the own file name.
* The lack of features for facilitate the directory navigation if there are more tha one file to convert.

Flaws already also been catched by my personal experience:

* Do not have intelligence to loop through list numbered sequence. Even when the sequence was correct in the markdown, the sequence number is not looped.
* Also does not treat block code.

## A better way to achieve a nice markdown lecture?

Check this out: https://github.com/rust-lang/mdBook

## Disclaimer
This project uses the [mistune library](https://github.com/lepture/mistune) for parsing markdown into html. Disclaimer below: 

> Copyright (c) 2014, Hsiaoming Yang
>
> All rights reserved.
>
> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
>
> * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
>
> * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
>
> * Neither the name of the creator nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
>
> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
