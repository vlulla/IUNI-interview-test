## The next few lines from https://tech.davis-hansson.com/p/make/  "Your Makefiles are wrong"
##
## So that we can use brace expansion which is unavailable in sh! Sheesh!
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
.RECIPEPREFIX = >

MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.PHONY: all clean message cleanall
.DEFAULT_GOAL: all

PANDOC_OPTS=--from=gfm --standalone --highlight-style=tango --wrap=none
PANDOC_HTML_OPTS=--to=html5 --mathjax --email-obfuscation=references

all: $(patsubst %.md,%.html,$(wildcard *.md)) $(patsubst %.md,%.pdf,$(wildcard *.md))

%.pdf: %.md Makefile
> pandoc ${PANDOC_OPTS} --to=latex --output=$@ $<

%.html: %.md Makefile
> pandoc ${PANDOC_OPTS} ${PANDOC_HTML_OPTS} --output=$@ $<
> sed -i -e '/max-width: 36em/s@36em@ 60% @g' $@

clean: 
> rm -rf $(patsubst %.md,%.pdf,$(wildcard *.md)) $(patsubst %.md,%.html,$(wildcard *.md))

cleanall: clean
> @echo "Do some specialized cleaning here..."

