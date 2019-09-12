TALK = mock-library-talk

# Presentation
all: pdf view clean

pdf:
	TEXMFHOME=texmf pdflatex $(TALK).tex
	TEXMFHOME=texmf pdflatex $(TALK).tex

view:
	xdg-open "$(TALK).pdf" 2> /dev/null || \
	open -a firefox "$(TALK).pdf" 2> /dev/null || \
	open "$(TALK).pdf" 2> /dev/null || \
	echo Cannot find a program to open file.

deps:
	rm -rf texmf texmfvar ~/Library/texlive
	TEXMFHOME=texmf tlmgr init-usertree
	TEXMFHOME=texmf tlmgr --usermode install fontawesome textpos || :
	TEXMFHOME=texmf TEXMFVAR=texmf updmap-user

venv: FORCE
	rm -rf ~/.venv/$(TALK)
	python3 -m venv ~/.venv/$(TALK)
	echo . ~/.venv/$(TALK)/bin/activate > venv
	. ./venv && pip install requests pylama pylama-pylint

# Test code
examples: FORCE
	. ./venv && python3 examples/ex1/app.py Makefile venv
	. ./venv && python3 examples/ex2/app.py python cpython
	. ./venv && python3 examples/ex3/app.py python cpython
	. ./venv && python3 examples/ex4/app.py python cpython

test:
	. ./venv && cd examples/ex1 && python3 -m unittest -v testapp
	. ./venv && cd examples/ex1 && python3 -m unittest -v testbad \
	    && exit 1 || exit 0
	. ./venv && cd examples/ex2 && python3 -m unittest -v testapp1
	. ./venv && cd examples/ex2 && python3 -m unittest -v testapp2
	. ./venv && cd examples/ex3 && python3 -m unittest -v testapp1
	. ./venv && cd examples/ex3 && python3 -m unittest -v testapp2
	. ./venv && cd examples/ex4 && python3 -m unittest -v testapp
	@echo
	echo DONE
	@echo

lint:
	$(MAKE) linters DIR=examples/ex1
	$(MAKE) linters DIR=examples/ex2
	$(MAKE) linters DIR=examples/ex3
	$(MAKE) linters DIR=examples/ex4

linters:
	. ./venv && cd $(DIR) && isort --quiet --diff
	. ./venv && cd $(DIR) && pylama \
	    -l pycodestyle,pyflakes,mccabe,pylint,isort \
	    -i C0102,C0111,C0103,R0201

checks: examples test lint
	@echo
	@echo DONE
	@echo

# Cleanup
clean:
	rm -rf *.aux *.log *.nav *.out *.snm *.toc *.vrb
	find . -name ".DS_Store" -exec rm {} +

FORCE:
