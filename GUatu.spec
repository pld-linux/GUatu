Summary:	Comic book viewer
Summary(pl):	Przeglądarka komiksów
Name:		GUatu
Version:	0.872
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/guatu/%{name}-%{version}.tgz
# Source0-md5:	479252e88d36da14851510c425548375
Patch0:		%{name}-desktop.patch
URL:		http://guatu.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglext-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUatu is a GTK/OpenGL-based comic book viewer.

%description -l pl
GUatu jest bazującą na GTK/OpenGL przeglądarką komiksów.

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
