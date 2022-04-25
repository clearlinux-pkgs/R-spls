#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spls
Version  : 2.2.3
Release  : 41
URL      : https://cran.r-project.org/src/contrib/spls_2.2-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spls_2.2-3.tar.gz
Summary  : Sparse Partial Least Squares (SPLS) Regression and
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-pls
BuildRequires : R-pls
BuildRequires : buildreq-R

%description
partial least squares (SPLS) regression and classification

%prep
%setup -q -c -n spls
cd %{_builddir}/spls

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641131157

%install
export SOURCE_DATE_EPOCH=1641131157
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spls
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spls
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spls
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc spls || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spls/DESCRIPTION
/usr/lib64/R/library/spls/INDEX
/usr/lib64/R/library/spls/Meta/Rd.rds
/usr/lib64/R/library/spls/Meta/data.rds
/usr/lib64/R/library/spls/Meta/features.rds
/usr/lib64/R/library/spls/Meta/hsearch.rds
/usr/lib64/R/library/spls/Meta/links.rds
/usr/lib64/R/library/spls/Meta/nsInfo.rds
/usr/lib64/R/library/spls/Meta/package.rds
/usr/lib64/R/library/spls/Meta/vignette.rds
/usr/lib64/R/library/spls/NAMESPACE
/usr/lib64/R/library/spls/R/spls
/usr/lib64/R/library/spls/R/spls.rdb
/usr/lib64/R/library/spls/R/spls.rdx
/usr/lib64/R/library/spls/data/datalist
/usr/lib64/R/library/spls/data/lymphoma.RData
/usr/lib64/R/library/spls/data/mice.RData
/usr/lib64/R/library/spls/data/prostate.RData
/usr/lib64/R/library/spls/data/yeast.RData
/usr/lib64/R/library/spls/doc/index.html
/usr/lib64/R/library/spls/doc/spls-example.R
/usr/lib64/R/library/spls/doc/spls-example.Rnw
/usr/lib64/R/library/spls/doc/spls-example.pdf
/usr/lib64/R/library/spls/help/AnIndex
/usr/lib64/R/library/spls/help/aliases.rds
/usr/lib64/R/library/spls/help/paths.rds
/usr/lib64/R/library/spls/help/spls.rdb
/usr/lib64/R/library/spls/help/spls.rdx
/usr/lib64/R/library/spls/html/00Index.html
/usr/lib64/R/library/spls/html/R.css
/usr/lib64/R/library/spls/tests/tspls.R
/usr/lib64/R/library/spls/tests/tspls.Rout.save
