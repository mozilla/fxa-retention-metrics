SYSTEMPYTHON = `which python2 python | head -n 1`
VIRTUALENV = virtualenv --python=$(SYSTEMPYTHON)
ENV = ./local

# Hackety-hack around OSX system python bustage.
# The need for this should go away with a future osx/xcode update.
ARCHFLAGS = -Wno-error=unused-command-line-argument-hard-error-in-future

INSTALL = ARCHFLAGS=$(ARCHFLAGS) $(ENV)/bin/pip install

.PHONY: all
all: build

.PHONY: spark_install
spark_install:
	wget http://apache.mirror.gtcomm.net/spark/spark-1.3.1/spark-1.3.1-bin-hadoop2.6.tgz
	tar -xzf spark-1.3.1-bin-hadoop2.6.tgz
	export SPARK_HOME=$(pwd)/spark-1.3.1-bin-hadoop2.6;

.PHONY: install
install:
	make spark_install
	$(VIRTUALENV) --no-site-packages $(ENV)
	$(INSTALL) -r requirements.txt

.PHONY: build
build:
	./build.sh

.PHONY: spark
spark:
	SPARK_LOCAL_IP="127.0.0.1" IPYTHON_OPTS="notebook" ./spark-1.3.1-bin-hadoop2.6/bin/pyspark --packages com.databricks:spark-csv_2.10:1.2.0

.PHONY: test
test:
	./test.sh

.PHONY: clean
clean:
	rm -rf $(ENV)
