%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d


Summary:	OpenGL image compositing library
Name:		glitz
Version:        0.5.6
Release:        %mkrel 2
License:	BSD
Group:		System/Libraries
Source0:	http://cairographics.org/snapshots/%name-%version.tar.bz2
Patch0:		glitz-0.4.0-libtool.patch
URL:		http://cairographics.org/
BuildRequires:	XFree86-devel
BuildRequires: automake1.7
BuildRoot:	%_tmppath/%name-%version-root

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

%package -n %{libnamedev}
Summary:	Development files for glitz library
Group:		Development/C
Requires:	%{libname} = %version
Provides:	%{name}-devel = %version-%release
Provides:	lib%{name}-devel = %version-%release

%description -n %{libnamedev}
Development files for glitz library.

%package -n %{libname}-static-devel
Summary:	Static glitz library
Group:		Development/C
Requires:	%{libnamedev} = %version

%description -n %{libname}-static-devel
Static glitz library.

%prep
%setup -q
aclocal-1.7
autoheader
autoconf
cp %_datadir/automake-1.7/mkinstalldirs config
automake-1.7
libtoolize --copy --force
%patch0 -p1 -b .libtool

%build
%configure2_5x
%make

%install

%makeinstall_std
#fix libtool library:
perl -pi -e "s°-L$RPM_BUILD_DIR/%name-%version/src°°" %buildroot%_libdir/*.la


%clean
rm -rf $RPM_BUILD_ROOT

%post	-n %{libname} -p /sbin/ldconfig
%postun	-n %{libname} -p /sbin/ldconfig


%files -n %{libname}
%defattr(644,root,root,755)
%doc AUTHORS COPYING README NEWS TODO
%_libdir/lib*.so.*

%files -n %{libnamedev}
%defattr(644,root,root,755)
%_libdir/lib*.so
%_libdir/lib*.la
%_includedir/*
%_libdir/pkgconfig/*.pc

%files -n %{libname}-static-devel
%defattr(644,root,root,755)
%_libdir/lib*.a


