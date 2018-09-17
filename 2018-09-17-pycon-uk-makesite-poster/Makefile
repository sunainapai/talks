MAIN_POSTER = makesite-main-poster
CODE_POSTER = makesite-code-poster

all: poster clean view

poster:
	TEXMFHOME=texmf pdflatex $(MAIN_POSTER).tex
	TEXMFHOME=texmf pdflatex $(CODE_POSTER).tex

view:
	if command -v xdg-open > /dev/null; then \
	    xdg-open "$(MAIN_POSTER).pdf"; \
	    xdg-open "$(CODE_POSTER).pdf"; \
	elif command -v open > /dev/null; then \
	    open "$(MAIN_POSTER).pdf"; \
	    open "$(CODE_POSTER).pdf"; \
	else \
	    echo Cannot find xdg-open or open.; \
	fi

deps:
	rm -rf texmf ~/Library/texlive
	TEXMFHOME=texmf tlmgr init-usertree
	TEXMFHOME=texmf tlmgr --usermode install a0poster titlesec || :

clear:
	rm -rf *.pdf

clean:
	rm -rf *.aux *.log *.nav *.out *.snm *.toc *.vrb
	find . -name ".DS_Store" -exec rm {} +
