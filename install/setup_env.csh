#!/bin/tcsh

# store_dir is the directory where the miniconda install is placed
setenv store_dir ${HOME}/store
#setenv MINICONDA_VERSION "2" #${MINICONDA_VERSION:-"latest"}
setenv CACHE_DIR "${store_dir}/miniconda.tarball"
setenv CACHE_DIR_TMP "$CACHE_DIR.tmp"
setenv CACHE_TARBALL_NAME "miniconda.tar.gz"
setenv CACHE_TARBALL_PATH "$CACHE_DIR/$CACHE_TARBALL_NAME"
setenv PATH "${store_dir}/miniconda/bin:$PATH"
rehash
