Summary:	Library for reading and writing ID3 tags
Summary(pl):	Biblioteka pozwalaj±ca na odczyt i zapis znaczników ID3
Name:		libid3tag
Version:	0.15.1b
Release:	4
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
# Source0-md5:	e5808ad997ba32c498803822078748c3
Patch0:		%{name}-id3v23.patch
URL:		http://www.underbit.com/products/mad/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
Obsoletes:	mad-libs < 0.15.0b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.

%description -l pl
libid3tag jest bibliotek± do odczytu i zapisu znaczników ID3 - zarówno
w wersji ID3v1 jak te¿ ID3v2.

%package devel
Summary:	Header files for libid3tag
Summary(pl):	Pliki nag³ówkowe dla biblioteki libid3tag
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel
Obsoletes:	mad-devel < 0.15.0b

%description devel
Header files for libid3tag.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki libid3tag.

%package static
Summary:	Static libid3tag library
Summary(pl):	Biblioteka statyczna libid3tag
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	mad-static < 0.15.0b

%description static
Static libid3tag library.

%description static -l pl
Biblioteka statyczna libid3tag.

%prep
%setup -q
%patch0 -p1

# Create an additional pkgconfig file
%{__cat} > id3tag.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: id3tag
Description: ID3 tag library
Requires:
Version: %{version}
Libs: -L%{_libdir} -lid3tag -lz
Cflags: -I%{_includedir}
EOF

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
install id3tag.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT CREDITS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/id3tag.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
