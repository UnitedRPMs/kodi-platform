%global commit0 e8574b883ffa2131f2eeb96ff3724d60b21130f7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20170524
%global gver .git%{shortcommit0}

Name:           kodi-platform
Version:        18.0
Release:    	6%{?gver}%{dist}
Summary:        Kodi platform environment for compiling cmake binary addons

Group:          Applications/Multimedia

License:        GPLv3 and GPLv2+ and LGPLv2+ and MIT
URL:            https://github.com/xbmc/kodi-platform
Source0:        https://github.com/xbmc/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	tinyxml-devel
BuildRequires:  libcec-devel
BuildRequires:	platform-devel
BuildRequires:  git
BuildRequires:	kodi-devel >= 18

%description
Kodi platform environment for compiling cmake binary addons.

%package devel
Summary:        Kodi platform environment devel files
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}-%{release}

%description devel
Kodi platform environment devel files

%prep
%autosetup -n %{name}-%{commit0}
#%setup -n kodi-platform 
#patch1 -p1


%build

%cmake CMAKE_PREFIX_PATH=%{_libdir}/kodi/ .
make %{?_smp_mflags} VERBOSE=0


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

* Sun Feb 03 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-6.gite8574b8  
- Automatic Mass Rebuild

* Sat Oct 13 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-5.gite8574b8  
- Automatic Mass Rebuild

* Wed Sep 05 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-4.gite8574b8  
- Automatic Mass Rebuild

* Thu Jun 28 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-3.gite8574b8  
- Automatic Mass Rebuild

* Wed Apr 25 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-2.gite8574b8  
- Automatic Mass Rebuild

* Wed Mar 21 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 18.0-1.gite8574b8
- Updated to 18.0-1.gite8574b8

* Sun Oct 22 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 17.5-1.git36fb493
- Updated to 17.5-1.git36fb493

* Wed Oct 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 17.4-2.01.git36fb493  
- Automatic Mass Rebuild

* Fri Sep 01 2017 David Vásquez <davidva AT tutanota DOT com> - 17.4-2.git36fb493
- Rebuilt for Kodi cmake

* Wed May 24 2017 David Vásquez <davidva AT tutanota DOT com> - 17.2-1.git36fb493
- Updated 17.2-1.git36fb493

* Tue Jan 10 2017 Pavlo Rudyi <paulcarroty at riseup.net> - 17.0-2
- Rebuild
- Added sources

* Sun Oct 16 2016 David Vásquez <davidva AT tutanota DOT com> - 17.0-1-20161016gitc8188d8
- Updated

* Fri Jul 08 2016 David Vásquez <davidva AT tutanota DOT com> - 16.0-4-20160305-15edaf7
- Massive rebuild

* Tue Jun 07 2016 David Vasquez <davidva AT tutanota DOT com> - 16.0-3-20160305-15edaf7
- Changed incoherent release
- Patches thanks to Sergio Basto

* Wed May 11 2016 David Vasquez <davidva AT tutanota DOT com> - 16.0-2-20160305-15edaf7
- Built with platfom-compat

* Sat Mar 05 2016 David Vasquez <davidva AT tutanota DOT com> - 16.0-20160305-15edaf7-1
- Updated to 16.0-20160305-15edaf7


* Tue Oct 20 2015 David Vasquez <davidva AT tutanota DOT com> - 1.0-2-20151020-45d6ad1
- Updated to 1.0-20151020-45d6ad1

* Wed May 20 2015 David Vasquez <davidva AT tutanota DOT com> - 1.0-1-20150520-33b6390
- Initial build rpm
