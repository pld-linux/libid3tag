Summary:	Library for reading and writing ID3 tags
Summary(pl):	Biblioteka pozwalaj±ca na odczyt i zapis tagów ID3
Name:		libid3tag
Version:	0.15.0b
Release:	1.96
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
# Source0-md5:	a625307d2cda4f3c609b79c1e3a93d87
URL:		http://www.underbit.com/products/mad/
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zlib-devel
Obsoletes:	mad-libs < 0.15.0b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2

%description -l pl
libid3tag jest biblioteka do odczytu i zapisu tagów ID3 - zarówno w
wersji ID3v1 jak te¿ ID3v2

%package devel
Summary:	Headers files for libid3tag
Summary(pl):	Pliki nag³ówkowe dla biblioteki libid3tag
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	mad-devel < 0.15.0b

%description devel
Headers files for libid3tag

%description devel -l pl
Pliki nag³ówkowe dla biblioteki libid3tag

%package static
Summary:	Static libid3tag library
Summary(pl):	Biblioteka statyczna libid3tag
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	mad-static < 0.15.0b

%description static
Static libid3tag library

%description static -l pl
Biblioteka statyczna libid3tag

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES TODO CREDITS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
