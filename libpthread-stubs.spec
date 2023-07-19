Summary:	Meta package for pthread symbols
Summary(pl.UTF-8):	Metapakiet zapewniający symbole pthread
Name:		libpthread-stubs
Version:	0.5
Release:	2
License:	MIT
Group:		Libraries
Source0:	https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
# Source0-md5:	d42052cb343c3e050ff40adc1675e79f
URL:		https://xcb.freedesktop.org/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	libpthread-stubs-devel < 0.3
Obsoletes:	libpthread-stubs-static < 0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no binaries, but not noarch (contains arch-dependent path)
%define		_enable_debug_packages	0

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
