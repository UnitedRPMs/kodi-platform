#globals for kodi-platform-16.0-20160305-15edaf7.tar.xz
%global gitdate 20160305
%global gitversion 15edaf7
%global snapshot %{gitdate}-%{gitversion}
%global gver .%{gitdate}git%{gitversion}

Name:           kodi-platform
Version:        16.0
Release:    	4%{?gver}%{dist}
Summary:        Kodi platform environment for compiling cmake binary addons

Group:          Applications/Multimedia

License:        GPLv3 and GPLv2+ and LGPLv2+ and MIT
URL:            https://github.com/xbmc/kodi-platform
Source:		%{name}-%{version}-%{snapshot}.tar.xz
Source1:	%{name}-snapshot.sh
Patch1:     	p8-platform.patch

BuildRequires:	cmake
BuildRequires:	tinyxml-devel
BuildRequires:  libcec-devel
BuildRequires:	platform-devel
BuildRequires: 	git
BuildRequires:	kodi-devel >= 16.0

%description
Kodi platform environment for compiling cmake binary addons.

%package devel
Summary:        Kodi platform environment devel files
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}-%{release}

%description devel
Kodi platform environment devel files

%prep
%setup -n kodi-platform 
%patch1 -p1


%build
%cmake .
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%check
ctest -V %{?_smp_mflags}

%files 
%{_includedir}/kodi/util/XMLUtils.h
%{_libdir}/libkodiplatform.so
%{_libdir}/libkodiplatform.so.*


%files devel
%{_libdir}/pkgconfig/kodiplatform.pc
%{_libdir}/kodiplatform/kodiplatform-config.cmake


%changelog

* Fri Jul 08 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 16.0-4-20160305-15edaf7
- Massive rebuild

* Tue Jun 07 2016 David Vasquez <davidjeremias82 at gmail dot com> - 16.0-3-20160305-15edaf7
- Changed incoherent release
- Patches thanks to Sergio Basto

* Wed May 11 2016 David Vasquez <davidjeremias82 at gmail dot com> - 16.0-2-20160305-15edaf7
- Built with platfom-compat

* Sat Mar 05 2016 David Vasquez <davidjeremias82 at gmail dot com> - 16.0-20160305-15edaf7-1
- Updated to 16.0-20160305-15edaf7


* Tue Oct 20 2015 David Vasquez <davidjeremias82 at gmail dot com> - 1.0-2-20151020-45d6ad1
- Updated to 1.0-20151020-45d6ad1

* Wed May 20 2015 David Vasquez <davidjeremias82 at gmail dot com> - 1.0-1-20150520-33b6390
- Initial build rpm
