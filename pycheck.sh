#!/bin/bash

setup_environment() {
  IGNORE_ERRORS=E221,E701,E202
}

main() {
  setup_environment

  # pyenv required
  # which $PYENV_ROOT/shims/pyflakes > /dev/null || exit 254
  # which $PYENV_ROOT/shims/flake8 > /dev/null || exit 254
  # which $PYENV_ROOT/shims/pep8 > /dev/null || exit 254

  # which pyflakes > /dev/null || exit 254
  which flake8 > /dev/null || exit 254
  which pep8 > /dev/null || exit 254

  # $PYENV_ROOT/shims/pyflakes $*
  # $PYENV_ROOT/shims/flake8 $*
  # $PYENV_ROOT/shims/pep8 --ignore=$IGNORE_ERRORS --repeat $*

  # /usr/bin/env pyflakes $*
  /usr/bin/env flake8 $*
  /usr/bin/env pep8 --ignore=$IGNORE_ERRORS --repeat $*

  exit 0
}

main $*
