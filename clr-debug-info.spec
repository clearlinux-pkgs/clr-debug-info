#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-debug-info
Version  : 52
Release  : 76
URL      : https://github.com/clearlinux/clr-debug-info/archive/52/clr-debug-info-52.tar.gz
Source0  : https://github.com/clearlinux/clr-debug-info/archive/52/clr-debug-info-52.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: clr-debug-info-autostart = %{version}-%{release}
Requires: clr-debug-info-bin = %{version}-%{release}
Requires: clr-debug-info-config = %{version}-%{release}
Requires: clr-debug-info-data = %{version}-%{release}
Requires: clr-debug-info-license = %{version}-%{release}
Requires: clr-debug-info-services = %{version}-%{release}
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(systemd)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package autostart
Summary: autostart components for the clr-debug-info package.
Group: Default

%description autostart
autostart components for the clr-debug-info package.


%package bin
Summary: bin components for the clr-debug-info package.
Group: Binaries
Requires: clr-debug-info-data = %{version}-%{release}
Requires: clr-debug-info-config = %{version}-%{release}
Requires: clr-debug-info-license = %{version}-%{release}
Requires: clr-debug-info-services = %{version}-%{release}

%description bin
bin components for the clr-debug-info package.


%package config
Summary: config components for the clr-debug-info package.
Group: Default

%description config
config components for the clr-debug-info package.


%package data
Summary: data components for the clr-debug-info package.
Group: Data

%description data
data components for the clr-debug-info package.


%package license
Summary: license components for the clr-debug-info package.
Group: Default

%description license
license components for the clr-debug-info package.


%package services
Summary: services components for the clr-debug-info package.
Group: Systemd services

%description services
services components for the clr-debug-info package.


%prep
%setup -q -n clr-debug-info-52
cd %{_builddir}/clr-debug-info-52

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672256181
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1672256181
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-debug-info
cp %{_builddir}/clr-debug-info-%{version}/COPYING %{buildroot}/usr/share/package-licenses/clr-debug-info/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install
## service_restart content
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -s /usr/lib/systemd/system/clr_debug_fuse.service %{buildroot}/usr/share/clr-service-restart/clr_debug_fuse.service
## service_restart end
## Remove excluded files
rm -f %{buildroot}*/usr/bin/clr_debug_prepare
## install_append content
mkdir %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../clr_debug_fuse.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/clr_debug_fuse.service
mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../clr_debug_daemon.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/clr_debug_daemon.socket
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/clr_debug_fuse.service
/usr/lib/systemd/system/sockets.target.wants/clr_debug_daemon.socket

%files bin
%defattr(-,root,root,-)
/usr/bin/clr_debug_daemon
/usr/bin/clr_debug_fuse

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/debuginfo.conf

%files data
%defattr(-,root,root,-)
/usr/share/clr-service-restart/clr_debug_fuse.service

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-debug-info/4cc77b90af91e615a64ae04893fdffa7939db84c

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/clr_debug_fuse.service
%exclude /usr/lib/systemd/system/sockets.target.wants/clr_debug_daemon.socket
/usr/lib/systemd/system/clr_debug_daemon.service
/usr/lib/systemd/system/clr_debug_daemon.socket
/usr/lib/systemd/system/clr_debug_fuse.service
