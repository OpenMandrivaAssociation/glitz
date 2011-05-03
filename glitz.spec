%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d

Summary:	OpenGL image compositing library
Name:		glitz
Version:	0.5.6
Release:	%mkrel 9
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
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post	-n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun	-n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS TODO
%{_libdir}/libglitz*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/lib*.a
