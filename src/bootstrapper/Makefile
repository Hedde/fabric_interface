# Todo make sure the static dirs exist.

PROJECT_DIR = ..

BOOTSTRAP_LESS = ./less/bootstrap.less
BOOTSTRAP_LESS_THEME = ./less/theme.less

bootstrap:
	mkdir -p ${PROJECT_DIR}/static
	mkdir -p ${PROJECT_DIR}/static/css
	mkdir -p ${PROJECT_DIR}/static/js
	mkdir -p ${PROJECT_DIR}/static/fonts
	cat js/affix.js js/alert.js js/button.js js/carousel.js js/collapse.js js/dropdown.js js/modal.js js/tooltip.js js/popover.js js/scrollspy.js js/tab.js js/transition.js > ${PROJECT_DIR}/static/js/bootstrap.js
	uglifyjs -nc ${PROJECT_DIR}/static/js/bootstrap.js > ${PROJECT_DIR}/static/js/bootstrap.min.js
	rm ${PROJECT_DIR}/static/js/bootstrap.js
	lessc --compile --compress ${BOOTSTRAP_LESS} > ${PROJECT_DIR}/static/css/bootstrap.min.css
	lessc --compile --compress ${BOOTSTRAP_LESS_THEME} > ${PROJECT_DIR}/static/css/bootstrap-theme.min.css
	cp -r fonts/* ${PROJECT_DIR}/static/fonts/