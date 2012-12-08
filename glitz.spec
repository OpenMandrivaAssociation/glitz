%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d

Summary:	OpenGL image compositing library
Name:		glitz
Version:	0.5.6
Release:	%mkrel 11
License:	BSD
Group:		System/Libraries
URL:		http://cairographics.org/
Source0:	http://cairographics.org/snapshots/%name-%version.tar.bz2
Patch0:		glitz-0.4.0-libtool.patch
Patch1:		glitz-0.5.6-wformat.patch
BuildRequires:	libx11-devel
BuildRequires:	GL-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Glitz is an OpenGL image compositing library. Glitz provides
Porter/Duff compositing of images and implicit mask generation for
geometric primitives including trapezoids, triangles, and rectangles.

The semantics of glitz are designed to precisely match the
specification of the X Render extension. Glitz does not only implement
X Render features like component alpha and image transformations, but
also support for additional features like convolution filters and color
gradients, which are not currently part of the X Render specification.

The performance and capabilities of glitz are much dependent on
graphics hardware. Glitz does not in any way handle software
fall-backs when graphics hardware is insufficient. However, glitz
will report if any requested operation cannot be carried out by
graphics hardware, hence making a higher level software layer
responsible for appropriate actions.

%package -n %{libname}
Summary:	OpenGL image compositing library
Group:		System/Libraries
Provides:	glitz = %{version}-%{release}

%description -n %{libname}
Glitz is an OpenGL image compositing library. Glitz provides
Porter/Duff compositing of images and implicit mask generation for
geometric primitives including trapezoids, triangles, and rectangles.

The semantics of glitz are designed to precisely match the
specification of the X Render extension. Glitz does not only implement
X Render features like component alpha and image transformations, but
also support for additional features like convolution filters and color
gradients, which are not currently part of the X Render specification.

The performance and capabilities of glitz are much dependent on
graphics hardware. Glitz does not in any way handle software
fall-backs when graphics hardware is insufficient. However, glitz
will report if any requested operation cannot be carried out by
graphics hardware, hence making a higher level software layer
responsible for appropriate actions.

%package -n %{develname}
Summary:	Development files for glitz library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d %{name} 1

%description -n %{develname}
Development files for glitz library.

%package -n %{staticname}
Summary:	Static glitz library
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Obsoletes:	%mklibname -s -d %{name} 1

%description -n %{staticname}
Static glitz library.

%prep
%setup -q
%patch0 -p1 -b .libtool
%patch1 -p1 -b .wformat

%build

%configure2_5x
%make LDFLAGS+=-ldl

%install
%makeinstall_std

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS TODO
%{_libdir}/libglitz*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/lib*.a


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-9mdv2011.0
+ Revision: 664853
- mass rebuild

* Fri Feb 04 2011 Funda Wang <fwang@mandriva.org> 0.5.6-8
+ Revision: 635844
- rebuild
- tighten BR

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-7mdv2011.0
+ Revision: 605460
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-6mdv2010.1
+ Revision: 521129
- rebuilt for 2010.1

* Wed Aug 12 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5.6-5mdv2010.0
+ Revision: 415382
- fix -Wformat warnings

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-4mdv2009.1
+ Revision: 301466
- rebuilt against new libxcb

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.5.6-3mdv2009.0
+ Revision: 264553
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jun 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.6-2mdv2009.0
+ Revision: 215162
- fix underlinking
- spec file clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Wed Oct 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.6-2mdv2008.1
+ Revision: 101739
- new devel name


* Thu Mar 01 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.5.6-2mdv2007.0
+ Revision: 130764
- Import glitz

* Thu Mar 01 2007 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.6-2mdv2007.1
- do not package big ChangeLog

* Sat May 27 2006 Sebastien Savarin <plouf@mandriva.org> 0.5.6-1mdv2007.0
- New release 0.5.6

* Fri May 05 2006 Jerome Soyer <saispo@mandriva.org> 0.5.3-1mdk
- New release 0.5.3

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.4.4-2mdk
- Rebuild

* Fri Aug 12 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.4-1mdk
- New release 0.4.4

* Tue Jun 28 2005 Götz Waschk <waschk@mandriva.org> 0.4.3-1mdk
- reenable libtoolize
- New release 0.4.3

* Fri Feb 11 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.4.0-2mdk
- fix build ex nihilo

* Fri Jan 28 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.4.0-1mdk
- New release 0.4.0

* Fri Nov 05 2004 Marcel Pol <mpol@mandrake.org> 0.2.3-1mdk
- 0.2.3
- use %%configure macro

* Sat Sep 18 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2.2-1mdk
- from Tigrux <tigrux@ximian.com> : 
	- First RPM, based on Cairo rpm
- use mklibname macros
- do not use the %%configure

