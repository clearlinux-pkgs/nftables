#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD55D978A8A1420E4 (coreteam@netfilter.org)
#
Name     : nftables
Version  : 1.0.7
Release  : 65
URL      : https://www.netfilter.org/pub/nftables/nftables-1.0.7.tar.xz
Source0  : https://www.netfilter.org/pub/nftables/nftables-1.0.7.tar.xz
Source1  : https://www.netfilter.org/pub/nftables/nftables-1.0.7.tar.xz.sig
Summary  : Netfilter nf_tables user library
Group    : Development/Tools
License  : GPL-2.0
Requires: nftables-bin = %{version}-%{release}
Requires: nftables-data = %{version}-%{release}
Requires: nftables-lib = %{version}-%{release}
Requires: nftables-license = %{version}-%{release}
Requires: nftables-man = %{version}-%{release}
Requires: nftables-python = %{version}-%{release}
Requires: nftables-python3 = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : bison
BuildRequires : buildreq-distutils3
BuildRequires : docbook-utils
BuildRequires : flex
BuildRequires : gmp-dev
BuildRequires : jansson-dev
BuildRequires : ncurses-dev
BuildRequires : nftables-dev
BuildRequires : pkgconfig(libmnl)
BuildRequires : pkgconfig(libnftnl)
BuildRequires : pkgconfig(xtables)
BuildRequires : readline-dev
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the nftables package.
Group: Binaries
Requires: nftables-data = %{version}-%{release}
Requires: nftables-license = %{version}-%{release}

%description bin
bin components for the nftables package.


%package data
Summary: data components for the nftables package.
Group: Data

%description data
data components for the nftables package.


%package dev
Summary: dev components for the nftables package.
Group: Development
Requires: nftables-lib = %{version}-%{release}
Requires: nftables-bin = %{version}-%{release}
Requires: nftables-data = %{version}-%{release}
Provides: nftables-devel = %{version}-%{release}
Requires: nftables = %{version}-%{release}

%description dev
dev components for the nftables package.


%package doc
Summary: doc components for the nftables package.
Group: Documentation
Requires: nftables-man = %{version}-%{release}

%description doc
doc components for the nftables package.


%package lib
Summary: lib components for the nftables package.
Group: Libraries
Requires: nftables-data = %{version}-%{release}
Requires: nftables-license = %{version}-%{release}

%description lib
lib components for the nftables package.


%package license
Summary: license components for the nftables package.
Group: Default

%description license
license components for the nftables package.


%package man
Summary: man components for the nftables package.
Group: Default

%description man
man components for the nftables package.


%package python
Summary: python components for the nftables package.
Group: Default
Requires: nftables-python3 = %{version}-%{release}

%description python
python components for the nftables package.


%package python3
Summary: python3 components for the nftables package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nftables package.


%prep
%setup -q -n nftables-1.0.7
cd %{_builddir}/nftables-1.0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678803561
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static --with-xtables \
--with-json \
--with-cli=readline
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1678803561
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nftables
cp %{_builddir}/nftables-%{version}/COPYING %{buildroot}/usr/share/package-licenses/nftables/9b67937f4425456d36b29592838750ff8f0dceb3 || :
%make_install
## install_append content
make -C doc install DESTDIR=%{buildroot}
mv %{buildroot}/usr/lib/python3.11/site-packages/nftables-0.*-py3.11.egg/nftables %{buildroot}/usr/lib/python3.11/site-packages/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nft

%files data
%defattr(-,root,root,-)
/usr/share/nftables/all-in-one.nft
/usr/share/nftables/arp-filter.nft
/usr/share/nftables/bridge-filter.nft
/usr/share/nftables/inet-filter.nft
/usr/share/nftables/inet-nat.nft
/usr/share/nftables/ipv4-filter.nft
/usr/share/nftables/ipv4-mangle.nft
/usr/share/nftables/ipv4-nat.nft
/usr/share/nftables/ipv4-raw.nft
/usr/share/nftables/ipv6-filter.nft
/usr/share/nftables/ipv6-mangle.nft
/usr/share/nftables/ipv6-nat.nft
/usr/share/nftables/ipv6-raw.nft
/usr/share/nftables/netdev-ingress.nft

%files dev
%defattr(-,root,root,-)
/usr/include/nftables/libnftables.h
/usr/lib64/libnftables.so
/usr/lib64/pkgconfig/libnftables.pc
/usr/share/man/man3/libnftables.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/nftables/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnftables.so.1
/usr/lib64/libnftables.so.1.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nftables/9b67937f4425456d36b29592838750ff8f0dceb3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/libnftables-json.5
/usr/share/man/man8/nft.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
