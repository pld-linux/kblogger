%define		_beta	beta2
Summary:	KBlogger - kicker applet for quick blogging
SUmmary(de):	KBlogger - ein Kickerapplet fürs schnelle bloggen
Summary(pl):	KBlogger - aplet kickera do szybkiego blogowania
Name:		kblogger
Version:	0.6
Release:	0.%{_beta}.1
License:	GPL
Group:		Applications
Source0:	http://kblogger.pwsp.net/files/%{name}-%{version}%{_beta}.tar.gz
# Source0-md5:	e25c92bec7d116b1e229f02c1da582ed
URL:		http://www.kde-apps.org/content/show.php?content=29552
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBlogger is a kicker-applet for quick blogging, like gnome-blog. Just
push the blog button and blog! It currently supports the
Meta-Weblog-Api, which is supported by most blogs, and Blogger API
1.0. Support for Atom API is planned.

%description -l de
KBlogger ist ein Kickerapplet fürs schnelle bloggen, so wie
gnome-blog. Drück einfach den Knopf und blog loss. Es unterstützt zur
Zeit die Meta-Weblog-API, welche bei den meinsten Blogs verwendet wird
und Blogger API 1.0. Unterstützung für Atom API ist geplant.

%description -l pl
KBlogger jest apletem kickera do szybkiego blogowania, podobny do
gnome-bloga. Wystarczy, ¿e wci¶niesz przycisk i blogujesz. Aktualnie
wspiera Meta-Weblog-Api, u¿ywane przez wiêkszo¶æ blogów, oraz Bloger
API 1.0. Wsparcie dla Atom API jest planowane.

%prep
%setup -q -n %{name}-%{version}%{_beta}

%build
%{__make} -f Makefile.cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/kde3/kblogger_panelapplet.so
%{_libdir}/kde3/kblogger_panelapplet.la
%{_datadir}/apps/kicker/applets/kblogger.desktop
%{_datadir}/config.kcfg/kblogger.kcfg
%{_iconsdir}/crystalsvg/128x128/apps/kblogger.png
%{_iconsdir}/crystalsvg/16x16/apps/kblogger.png
%{_iconsdir}/crystalsvg/22x22/apps/kblogger.png
%{_iconsdir}/crystalsvg/32x32/apps/kblogger.png
%{_iconsdir}/crystalsvg/48x48/apps/kblogger.png
%{_iconsdir}/crystalsvg/64x64/apps/kblogger.png
%{_iconsdir}/crystalsvg/scalable/apps/kblogger.svg
%{_datadir}/doc/HTML/en/kblogger/*
%{_datadir}/doc/HTML/en/src/*
