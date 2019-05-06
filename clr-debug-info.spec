#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-debug-info
Version  : 48
Release  : 69
URL      : https://github.com/clearlinux/clr-debug-info/archive/48/clr-debug-info-48.tar.gz
Source0  : https://github.com/clearlinux/clr-debug-info/archive/48/clr-debug-info-48.tar.gz
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
%setup -q -n clr-debug-info-48

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557164905
export LDFLAGS="${LDFLAGS} -fno-lto"
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557164905
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-debug-info
cp COPYING %{buildroot}/usr/share/package-licenses/clr-debug-info/COPYING
%make_install
## install_append content
mkdir %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../clr_debug_fuse.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/clr_debug_fuse.service
mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../clr_debug_daemon.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/clr_debug_daemon.socket
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/clr_debug_fuse.service %{buildroot}/usr/share/clr-service-restart/clr_debug_fuse.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/clr_debug_fuse.service
/usr/lib/systemd/system/sockets.target.wants/clr_debug_daemon.socket

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/clr_debug_prepare
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
/usr/share/package-licenses/clr-debug-info/COPYING

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/clr_debug_fuse.service
%exclude /usr/lib/systemd/system/sockets.target.wants/clr_debug_daemon.socket
/usr/lib/systemd/system/clr_debug_daemon.service
/usr/lib/systemd/system/clr_debug_daemon.socket
/usr/lib/systemd/system/clr_debug_fuse.service
