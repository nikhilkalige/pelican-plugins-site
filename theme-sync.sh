#!/bin/bash

# Copy css files
cp -r theme/stylesheets/* templates/static/css
# Copy js
cp -r theme/js/* templates/static/js
cp theme/bower_components/foundation/js/foundation.min.js templates/static/js/
cp theme/bower_components/jquery/dist/jquery.min.js templates/static/js/
cp theme/bower_components/modernizr/modernizr.js templates/static/js/

cp -r theme/images/ templates/static/
