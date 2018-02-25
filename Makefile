SCRIPTS := noise.py
SCRIPTS += chi2.py

.PHONY: $(SCRIPTS)

all: $(SCRIPTS)

$(SCRIPTS):
	./$@

clean:
	rm -f *.png *.pyc
