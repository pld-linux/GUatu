Summary:	Comic book viewer
Summary(pl):	Przegl�darka komiks�w
Name:		GUatu
Version:	0.872
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/guatu/%{name}-%{version}.tgz
# Source0-md5:	479252e88d36da14851510c425548375
Patch0:		%{name}-desktop.patch
URL:		http://guatu.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglext-devel
BuildRequires:	OpenGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUatu is a GTK/OpenGL-based comic book viewer.

%description -l pl
GUatu jest bazuj�c� na GTK/OpenGL przegl�dark� komiks�w.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*