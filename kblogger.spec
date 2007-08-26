
%define		_beta	beta2

Summary:	KBlogger - kicker applet for quick blogging
Summary(de.UTF-8):	KBlogger - ein Kickerapplet fürs schnelle bloggen
Summary(pl.UTF-8):	KBlogger - aplet kickera do szybkiego blogowania
Name:		kblogger
Version:	0.7
Release:	0.%{_beta}.1
License:	GPL
Group:		X11/Applications
Source0:	http://kblogger.pwsp.net/files/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	05f7dbc27ae264b849ea40e6a705edc8
Patch0:		kde-ac260-lt.patch
URL:		http://www.kde-apps.org/content/show.php?content=29552
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 9:3.0
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBlogger is a kicker-applet for quick blogging, like gnome-blog. Just
push the blog button and blog! It currently supports the
Meta-Weblog-Api, which is supported by most blogs, and Blogger API
1.0. Support for Atom API is planned.

%description -l de.UTF-8
KBlogger ist ein Kickerapplet fürs schnelle bloggen, so wie
gnome-blog. Drück einfach den Knopf und blog loss. Es unterstützt zur
Zeit die Meta-Weblog-API, welche bei den meinsten Blogs verwendet wird
und Blogger API 1.0. Unterstützung für Atom API ist geplant.

%description -l pl.UTF-8
KBlogger jest apletem kickera do szybkiego blogowania, podobny do
gnome-bloga. Wystarczy, że wciśniesz przycisk i blogujesz. Aktualnie
wspiera Meta-Weblog-Api, używane przez większość blogów, oraz Bloger
API 1.0. Wsparcie dla Atom API jest planowane.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%patch0 -p1

%build
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
 	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
 	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

#%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/kde3/kblogger_panelapplet.so
%{_libdir}/kde3/kblogger_panelapplet.la
%{_datadir}/apps/kicker/applets/kblogger.desktop
%{_datadir}/config.kcfg/kblogger.kcfg
%dir %{_iconsdir}/crystalsvg/*/apps/kblogger
%{_iconsdir}/crystalsvg/*/apps/kblogger/warning.png
%{_iconsdir}/crystalsvg/*/apps/kblogger.png
#%{_iconsdir}/crystalsvg/scalable/apps/kblogger.svg
