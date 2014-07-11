%define major	1
%define libname %mklibname %{name} %{major}
%define libglx %mklibname %{name}-glx %{major}
%define devname %mklibname %{name} -d

Summary:	OpenGL image compositing library
Name:		glitz
Version:	0.5.6
Release:	18
License:	BSD
Group:		System/Libraries
Url:		http://cairographics.org/
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.bz2
Patch0:		glitz-0.4.0-libtool.patch
Patch1:		glitz-0.5.6-wformat.patch

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(x11)

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

%package -n %{libglx}
Summary:	OpenGL image compositing library
Group:		System/Libraries
Conflicts:	%{_lib}glitz1 < 0.5.6-12

%description -n %{libglx}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Development files for glitz library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libglx} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}glitz-static-devel < 0.5.6-12

%description -n %{devname}
Development files for glitz library.

%prep
%setup -q
%apply_patches

%build

%configure2_5x \
	--disable-static
%make LDFLAGS+=-ldl

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libglitz.so.%{major}*

%files -n %{libglx}
%{_libdir}/libglitz-glx.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING README NEWS TODO
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

