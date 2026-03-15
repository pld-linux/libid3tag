#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Library for reading and writing ID3 tags
Summary(pl.UTF-8):	Biblioteka pozwalająca na odczyt i zapis znaczników ID3
Name:		libid3tag
Version:	0.16.4
Release:	2
License:	GPL v2+
Group:		Libraries
#Source0Download: https://codeberg.org/tenacityteam/libid3tag/releases
# TODO use release tarballs?
# https://codeberg.org/tenacityteam/libid3tag/releases/download/%{version}/id3tag-%{version}-source.tar.gz
Source0:	https://codeberg.org/tenacityteam/libid3tag/archive/%{version}.tar.gz
# Source0-md5:	6b4dcbc9e1746c9d76dcb0f1b9eb4c16
URL:		https://codeberg.org/tenacityteam/libid3tag
BuildRequires:	cmake >= 3.10
BuildRequires:	gperf
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
Obsoletes:	mad-libs < 0.15.0b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.

%description -l pl.UTF-8
libid3tag jest biblioteką do odczytu i zapisu znaczników ID3 - zarówno
w wersji ID3v1 jak też ID3v2.

%package devel
Summary:	Header files for libid3tag
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki libid3tag
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel
Obsoletes:	mad-devel < 0.15.0b

%description devel
Header files for libid3tag.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki libid3tag.

%package static
Summary:	Static libid3tag library
Summary(pl.UTF-8):	Biblioteka statyczna libid3tag
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	mad-static < 0.15.0b

%description static
Static libid3tag library.

%description static -l pl.UTF-8
Biblioteka statyczna libid3tag.

%prep
%setup -q -n libid3tag

%build
# .pc file generation requires relative CMAKE_INSTALL_LIBDIR
%cmake -B build \
	-DBUILD_SHARED_LIBS=ON \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make} -C build

%if %{with static_libs}
%cmake -B build-static \
	-DBUILD_SHARED_LIBS=OFF \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make} -C build-static
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT CREDITS README.md
%attr(755,root,root) %{_libdir}/libid3tag.so.*.*.*
%ghost %{_libdir}/libid3tag.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libid3tag.so
%{_includedir}/id3tag.h
%{_pkgconfigdir}/id3tag.pc
%{_libdir}/cmake/id3tag

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libid3tag.a
%endif
