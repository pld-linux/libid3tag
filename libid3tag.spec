Summary:	Library for reading and (eventually) writing ID3 tags
Summary(pl):	Biblioteka pozwalaj±ca na odczyt i zapis tagów ID3
Name:		libid3tag
Version:	0.15.0b
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
URL:		http://www.underbit.com/products/mad/
BuildRequires:	zlib-devel
Obsoletes:	mad-libs
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package devel
Summary:	Headers files for libid3tag
Summary(pl):	Pliki nag³ówkowe dla biblioteki libid3tag
Group:		Development/Libraries

%description devel
Headers files for libid3tag

%description devel -l pl
Pliki nag³ówkowe dla biblioteki libid3tag

%package static
Summary:	Static libid3tag library
Summary(pl):	Biblioteka statyczna libid3tag
Group:		Development/Libraries

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
# create directories if necessary
#install -d $RPM_BUILD_ROOT

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
