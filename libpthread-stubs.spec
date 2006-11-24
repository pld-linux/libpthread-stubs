Summary:	pthread library helper
Name:		libpthread-stubs
Version:	0.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	774eabaf33440d534efe108ef9130a7d
URL:		http://xcb.freedesktop.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides weak aliases for pthread functions not provided
in libc or otherwise available by default. Libraries like libxcb rely
on pthread stubs to use pthreads optionally, becoming thread-safe when
linked to libpthread, while avoiding any performance hit when running
single-threaded. libpthread-stubs supports this behavior even on
platforms which do not supply all the necessary pthread stubs. On
platforms which already supply all the necessary pthread stubs, this
package ships only the pkg-config file pthread-stubs.pc, to allow
libraries to unconditionally express a dependency on pthread-stubs and
still obtain correct behavior.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_pkgconfigdir}/*.pc
