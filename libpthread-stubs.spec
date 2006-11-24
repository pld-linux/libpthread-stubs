Summary:	pthread library helper
Summary(pl):	Pakiet pomocniczy biblioteki pthread
Name:		libpthread-stubs
Version:	0.1
Release:	1
License:	MIT
Group:		Development/Libraries
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

%description -l pl
Ta biblioteka udostêpnia s³abe aliasy dla funkcji pthread nie
dostarczane domy¶lnie przez libc lub w inny sposób. Biblioteki takie
jak libxcb polegaj± na za¶lepkach pthread, aby opcjonalnie u¿ywaæ
w±tków pthread i zachowywaæ siê bezpiecznie w przypadku zlinkowania z
libpthread, a unikaæ narzutu czasowego przy dzia³aniu jednow±tkowym.
libpthread-stubs obs³uguje to zachowanie nawet na platformach nie
udostêpniaj±cych wszystkich potrzebnych za¶lepek pthread. Na
platformach udostêpniaj±cych wszystkie potrzebne za¶lepki pthread ten
pakiet dostarcza jedynie plik pkg-configa pthread-stubs.pc pozwalaj±cy
bibliotekom bezwarunkowo zawieraæ zale¿no¶æ od pthread-stubs i nadal
zachowywaæ siê prawid³owo.

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
