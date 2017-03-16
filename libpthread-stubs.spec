Summary:	Meta package for pthread symbols
Summary(pl.UTF-8):	Metapakiet zapewniający symbole pthread
Name:		libpthread-stubs
Version:	0.4
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	48c1544854a94db0e51499cc3afd797f
URL:		https://xcb.freedesktop.org/
Obsoletes:	libpthread-stubs-devel < 0.3
Obsoletes:	libpthread-stubs-static < 0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meta package for pthread symbols - defaults to heavyweight ones
(libpthread) if the C runtime does not provide lightweight ones.

%description -l pl.UTF-8
Metapakiet zapewniający symbole pthread - domyślnie cięższe
(libpthread), jeśli biblioteka uruchomieniowa C nie dostarcza lżejszej
wersji.

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
%doc COPYING README
%{_pkgconfigdir}/pthread-stubs.pc
