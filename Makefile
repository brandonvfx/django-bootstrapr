BOOTSTRAP_REPO = git://github.com/twitter/bootstrap.git

build:
	@git clone git://github.com/twitter/bootstrap.git
	@cd bootstrap && npm install && make bootstrap
	@cp -r bootstrap/bootstrap/* django_bootstrapr/static/
	@rm -r ./bootstrap