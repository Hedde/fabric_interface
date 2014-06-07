Todo's
------

# Base

* configuration views, models and templates, reverse urls configs
* further tweaking of formulae/fabfile views, models and templates
* raise non field form errors in templates

# Features

* fabfile rendering using configuration inheritance and mptt ordering logic
* fab execution (sub process) / logging / short polling
* supressing stdout / verbosity levels

# Release candidate requires

* reset passwords
* user row level permission interface
* check orphan permissions, e.g. 'can view stage' => if 'can view project'

# Stable candidate requires

* documentation

Known bugs
----------

# Migrations

* MPTT doesn't work with django's migrations yet. (NewBase issue), so we're using South and django 1.6.5 for the moment

# Translations

* Messages framework language awareness