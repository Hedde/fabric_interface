Todo's
------

# Base

* configuration views, models and templates, reverse urls configs
* formulae/recipes views, models and templates
* raise non field form errors in templates

# Features

* fabfile rendering using configuration inheritance and formulae ordering logic
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

* MPTT doesn't work with django's migrations yet. (NewBase issue)

# Translations

* Messages framework language awareness