Summary:     K Desktop Environment - administrative tools
Summary(pl): K Desktop Environment - narzêdzia administratora
Name:        kdeadmin
Version:     1.1.1
Release:     2
Copyright:   GPL
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Vendor:      The KDE Team
#ftp:	     ftp.kde.org/
#patch:      pub/kde/stable/%{version}/distribution/tar/generic/source/bz2/
Source:      %{name}-%{version}.tar.bz2
Requires:    qt >= 1.44, kdelibs = %{version}
BuildRoot:   /tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
KDE administrative tools.
Package includes:
  KDat  - KDE tar-based tape archiver
  KUser - KDE user setup tool
  KSYSV - SYS V Init configuration

%description -l pl
Aplikacje administratorskie dla KDE.
Pakiet zawiera:
  KDat  - Program archiwizuj±cy 
  KUser - Program do zarz±dzania kontami u¿ytkowników
  KSYSV - Program do konfiguracji startu systemu

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
%setup -q

%build
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall -fno-rtti -fno-exceptions" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"

cd kdat
make KDEDIR=$KDEDIR
cd  ../ksysv
make KDEDIR=$KDEDIR
cd ../kuser
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=%{_prefix}
cd kuser
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install
cd ..
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

%find_lang kdat
%find_lang kuser
%find_lang ksysv

%clean
rm -rf $RPM_BUILD_ROOT

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

%changelog
* Tue May 25 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.1.1-2]
- fixes package,
- fixes file locations.

* Tue May 18 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.1.1-1]
- update to version 1.1.1,
- added Group(pl) description,
- added kdat package,
- fixes Group description.
 
* Wed Dec  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-7]
- recompiled against libstdc++.so.2.9.

* Fri Oct 16 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-4]
- created new spec based on kdebase.spec.
