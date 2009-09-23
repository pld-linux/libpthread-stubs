Summary:	pthread library helper
Summary(pl.UTF-8):	Pakiet pomocniczy biblioteki pthread
Name:		libpthread-stubs
Version:	0.2
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	2ba9ce2d46da0a2a1090384ece3387ff
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

%description -l pl.UTF-8
Ta biblioteka udostępnia słabe aliasy dla funkcji pthread nie
dostarczane domyślnie przez libc lub w inny sposób. Biblioteki takie
jak libxcb polegają na zaślepkach pthread, aby opcjonalnie używać
wątków pthread i zachowywać się bezpiecznie w przypadku zlinkowania z
libpthread, a unikać narzutu czasowego przy działaniu jednowątkowym.
libpthread-stubs obsługuje to zachowanie nawet na platformach nie
udostępniających wszystkich potrzebnych zaślepek pthread. Na
platformach udostępniających wszystkie potrzebne zaślepki pthread ten
pakiet dostarcza jedynie plik pkg-configa pthread-stubs.pc pozwalający
bibliotekom bezwarunkowo zawierać zależność od pthread-stubs i nadal
zachowywać się prawidłowo.

%package devel
Summary:	Header files and develpment documentation for libpthread-stubs
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do libpthread-stubs
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and documentation for libpthread-stubs.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libpthread-stubs.

%package static
Summary:	Static libpcap library
Summary(pl.UTF-8):	Biblioteka statyczna libpcap
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains the static library used for development.

%description static -l pl
Biblioteka statyczna libpthread-stubs.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*.pc
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
