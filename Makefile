SYSTEMPYTHON = `which python2 python | head -n 1`
VIRTUALENV = virtualenv --python=$(SYSTEMPYTHON)
ENV = ./local

# Hackety-hack around OSX system python bustage.
# The need for this should go away with a future osx/xcode update.
ARCHFLAGS = -Wno-error=unused-command-line-argument-hard-error-in-future

INSTALL = ARCHFLAGS=$(ARCHFLAGS) $(ENV)/bin/pip install

.PHONY: all
all: build

.PHONY: build
build: | $(ENV)/COMPLETE
$(ENV)/COMPLETE: requirements.txt
    $(VIRTUALENV) --no-site-packages $(ENV)
    $(INSTALL) -r requirements.txt
    touch $(ENV)/COMPLETE

.PHONY: clean
clean:
    rm -rf $(ENV)
