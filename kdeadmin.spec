%define		REV	20000418
Summary:	K Desktop Environment - administrative tools
Summary(pl):	K Desktop Environment - narzêdzia administratora
Name:		kdeadmin
Version:	2.0
Release:	1.pre_%{REV}
Copyright:	GPL
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Vendor:		The KDE Team
Source:		ftp.kde.org/pub/kde/snapshots/current/%{name}-%{REV}.tar.bz2
Requires:	qt >= 2.1, kdelibs = %{version}, pam
BuildRequires:	kdelibs-devel
BuildRequires:	rpm-devel >= 3.0.4
BuildRequires:	pam-devel >= 0.71
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix	/usr/X11R6

%description
KDE administrative tools.
Package includes:
  KCron - KDE Cron daemon
  KDat  - KDE tar-based tape archiver
  KUser - KDE user setup tool
  KSYSV - SYS V Init configuration
  KPackage - KDE support for RPM
  Kwuftpd - KDE ftp daemon
  

%description -l pl
Aplikacje administratorskie dla KDE.
Pakiet zawiera:
  KCron - Program cron
  KDat  - Program archiwizuj±cy 
  KUser - Program do zarz±dzania kontami u¿ytkowników
  KSYSV - Program do konfiguracji startu systemu
  KPackage - Przegl±darka pakietów
  Kwuftpd - Demon FTP dla KDE
  
%package kcron
Summary:     KDE cron daemon
Summary(pl): Program cron
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 2.1, kdelibs = %{version}

%description kcron
Kde version of "CRON"

%description -l pl kcron
Program "cron" w wersji dla KDE.

%package kdat
Summary:     KDE tar-based tape archiver
Summary(pl): Program archiwizuj±cy
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 1.44, kdelibs = %{version}

%description kdat
KDat is a tar-based tape archiver, designed to work with multiple archives
on a single tape.

%description -l pl kdat
Program archiwizujacy oparty na programie tar.

%package kuser
Summary:     KDE User management tool
Summary(pl): administracja kontami dla KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 1.44, kdelibs = %{version}

%description kuser
A simple tool for adding/removing users from system and changing
user information.

%description -l pl kuser
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o nich.

%package ksysv
Summary:     KDE Sys V Init configurator	
Summary(pl): Konfigurator Sys V Init dla KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 1.44, kdelibs = %{version}

%description ksysv
A Sys V Init configurator for KDE.

%description -l pl ksysv
Program do konfiguracji startu systemu wykorzystuj±cego Sys V Init

%prep
%setup -q -n %{name}

%build
make -f Makefile.cvs
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall"
CFLAGS="$RPM_OPT_FLAGS -Wall"
LDFLAGS="-s"
export CXXFLAGS CFLAGS LDFLAGS
%configure \
	--prefix=$KDEDIR \
	--with-qt-dir=%{_prefix} \
 	--with-install-root=$RPM_BUILD_ROOT \
	--with-rpm \
	--with-quota \
	--with-shadow \
 	--with-pam="yes"

make
#cd kdat
#make KDEDIR=$KDEDIR
#cd  ../ksysv
#make KDEDIR=$KDEDIR
#cd ../kuser
#make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=%{_prefix}
cd kuser
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install
cd ..
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

%find_lang kcron
%find_lang kdat
%find_lang kuser
%find_lang ksysv

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KCRON
#################################################
%files kcron -f kcron.lang
%defattr(644,root,root,755)
#################################################
#             KDAT
#################################################

%files kdat -f kdat.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Utilities/kdat.kdelnk

%attr(755, root, root) %{_bindir}/kdat

%{_datadir}/kde/icons/kdat.xpm
%{_datadir}/kde/icons/mini/kdat.xpm

#################################################
#             KUSER
#################################################

%files kuser -f kuser.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/System/kuser.kdelnk

%attr(755, root, root) %{_bindir}/kuser

%lang(en) %{_datadir}/kde/doc/HTML/en/kuser
%lang(ru) %{_datadir}/kde/doc/HTML/ru/kuser

%{_datadir}/kde/apps/kuser/

%{_datadir}/kde/icons/mini/kuser.xpm
%{_datadir}/kde/icons/kuser.xpm

#################################################
#             KSYSV
#################################################

%files ksysv -f ksysv.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/System/ksysv.kdelnk

%attr(755, root, root) %{_bindir}/ksysv

%lang(en) %{_datadir}/kde/doc/HTML/en/ksysv

%{_datadir}/kde/apps/ksysv/
%{_datadir}/kde/icons/ksysv.xpm
%{_datadir}/kde/icons/mini/ksysv.xpm
