Summary:	K Desktop Environment - administrative tools
Summary(pl):	K Desktop Environment - narzêdzia administratora
Name:		kdeadmin
Version:	2.2.1
Release:	1
License:	GPL
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Vendor:		The KDE Team
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-nokdat.patch
Icon:		kde-icon.xpm
Requires:	kdelibs = %{version}, pam 
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	pam-devel 
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
KDE administrative tools. Package includes:
- KCron - KDE Cron daemon
- KDat - KDE tar-based tape archiver
- KUser - KDE user setup tool
- KSYSV - SYS V Init configuration
- KPackage - KDE support for RPM
- Kwuftpd - KDE ftp daemon

%description -l pl
Aplikacje administratorskie dla KDE. Pakiet zawiera:
- KCron - Program cron
- KDat - Program archiwizuj±cy
- KUser - Program do zarz±dzania kontami u¿ytkowników
- KSYSV - Program do konfiguracji startu systemu
- KPackage - Przegl±darka pakietów
- Kwuftpd - Demon FTP dla KDE

%package kcron
Summary:	KDE cron daemon
Summary(pl):	Program cron
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 2.1, kdelibs = %{version}

%description kcron
Kde version of "CRON"

%description -l pl kcron
Program "cron" w wersji dla KDE.

%package kdat
Summary:	KDE tar-based tape archiver
Summary(pl):	Program archiwizuj±cy
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 2.1, kdelibs = %{version}

%description kdat
KDat is a tar-based tape archiver, designed to work with multiple
archives on a single tape.

%description -l pl kdat
Program archiwizujacy oparty na programie tar.

%package kuser
Summary:	KDE User management tool
Summary(pl):	administracja kontami dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 2.1, kdelibs = %{version}

%description kuser
A simple tool for adding/removing users from system and changing user
information.

%description -l pl kuser
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o
nich.

%package kpackage
Summary:	RPM front-end KDE
Summary(pl):	Program do manipulacji pakietami.
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 2.1, kdelibs = %{version}

%description kpackage
Package front-end for KDE.

%description -l pl kpackage
Program do manipulowania pakietami w ¶rodowisku KDE.

%package ksysctrl
Summary:	KDE System configurator	
Summary(pl):	Konfigurator Systemudla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 2.1, kdelibs = %{version}

%description ksysctrl
A System configurator for KDE.

%description -l pl ksysctrl
Program do konfiguracji systemu.

%package ksysv
Summary:	KDE Sys V Init configurator	
Summary(pl):	Konfigurator Sys V Init dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 2.1, kdelibs = %{version}

%description ksysv
A Sys V Init configurator for KDE.

%description -l pl ksysv
Program do konfiguracji startu systemu wykorzystuj±cego Sys V Init

%package kwuftpd
Summary:	KDE FTP daemon
Summary(pl):	Wu-FTP daemon for KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 2.1, kdelibs = %{version}

%description kwuftpd
Wu-FTP daemon for KDE.

%description -l pl kwuftpd
Zamiennik demona wu-ftp dla KDE.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f Makefile.cvs
KDEDIR=%{_prefix}
CXXFLAGS="%{rpmcflags} -Wall"
CFLAGS="%{rpmcflags} -Wall"
export KDEDIR

%configure \
	--prefix=%{_prefix} \
	--with-qt-dir=%{_prefix} \
 	--with-install-root=$RPM_BUILD_ROOT \
	--with-quota \
	--with-shadow \
	--with-rpm \
 	--with-pam="yes" \
	--with-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
KDEDIR=%{_prefix} ; export KDEDIR
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KCRON
#################################################
%files kcron
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcron

%{_datadir}/doc/HTML/en/kcron/*
%{_applnkdir}/System/kcron.desktop
%{_datadir}/icons/locolor/*x*/apps/kcron.png

#################################################
#             KDAT
#################################################
%files kdat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdat

%{_datadir}/doc/HTML/en/kdat/*
%{_applnkdir}/Utilities/kdat.desktop
%{_datadir}/apps/kdat/icons

#################################################
#             KPACKAGE
#################################################
%files kpackage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackage*

%{_datadir}/doc/HTML/en/kpackage/*
%{_applnkdir}/Utilities/kpackage.desktop
%{_datadir}/apps/kpackage
%{_datadir}/icons/hicolor/*x*/apps/kpackage.png
%{_datadir}/icons/locolor/*x*/apps/kpackage.png
%{_datadir}/mimelnk/application/x-debian-package.kdelnk

#################################################
#             KSYSCONTROL
#################################################
%files ksysctrl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksysctrl
%attr(755,root,root) %{_bindir}/printversion

%{_applnkdir}/System/ksysctrl.desktop
%{_datadir}/apps/ksysctrl

#################################################
#             KSYSV
#################################################
%files ksysv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/secpolicy
%attr(755,root,root) %{_bindir}/ksysv

%{_datadir}/doc/HTML/en/ksysv/*
%{_datadir}/apps/ksysv
%{_datadir}/icons/hicolor/*x*/apps/ksysv.png
%{_datadir}/icons/locolor/*x*/apps/ksysv.png

#################################################
#             KUSER
#################################################
%files kuser
%defattr(644,root,root,755)
%attr(755, root, root) %{_bindir}/kuser

%{_datadir}/doc/HTML/en/kuser/*
%{_applnkdir}/System/kuser.desktop
%{_datadir}/apps/kuser
%{_datadir}/icons/hicolor/*x*/apps/kuser.png
%{_datadir}/icons/locolor/*x*/apps/kuser.png

#################################################
#             KWUFTPD
#################################################
%files kwuftpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwuftpd

%{_datadir}/doc/HTML/en/kwuftpd/*
%{_applnkdir}/System/kwuftpd.desktop
