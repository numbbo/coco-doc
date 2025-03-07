#!/bin/bash
# The first argument is the folder where the repository folder
#   coco-experiment can be found, typically it may be ".."

python "$1"/coco-experiment/scripts/fabricate

touch "$1"/coco-experiment/build/python/example/__init__.py
pydoctor --docformat=restructuredtext --make-html --html-output='apidocs/example' "$1"/coco-experiment/build/python/example > err-pydoc-example.txt
# after checking: apidocs/example/index.html
echo "  to catch new files execute 'git add apidocs/example'"

mkdir tmp
cp -r "$1"/coco-experiment/build/python/src/cocoex tmp
pydoctor --docformat=restructuredtext --make-html --html-output='apidocs/cocoex' tmp/cocoex > err-pydoc-cocoex.txt
echo "  to catch new files execute 'git add apidocs'"
echo "  then execute 'git commit'"
rm -r tmp
