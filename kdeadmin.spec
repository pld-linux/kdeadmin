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
Requires:    qt >= 2.1, kdelibs = %{version}

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
Requires:    qt >= 2.1, kdelibs = %{version}

%description kuser
A simple tool for adding/removing users from system and changing
user information.

%description -l pl kuser
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o nich.

%package kpackage
Summary:     RPM front-end KDE
Summary(pl): Program do manipulacji pakietami.
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 2.1, kdelibs = %{version}

%description kpackage
Package front-end for KDE

%description -l pl kpackage
Program do manipulowania pakietami w ¶rodowisku KDE.

%package ksysctrl
Summary:     KDE System configurator	
Summary(pl): Konfigurator Systemudla KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 2.1, kdelibs = %{version}

%description ksysctrl
A System configurator for KDE.

%description -l pl ksysctrl
Program do konfiguracji systemu.

%package ksysv
Summary:     KDE Sys V Init configurator	
Summary(pl): Konfigurator Sys V Init dla KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 2.1, kdelibs = %{version}

%description ksysv
A Sys V Init configurator for KDE.

%description -l pl ksysv
Program do konfiguracji startu systemu wykorzystuj±cego Sys V Init

%package kwuftpd
Summary:     KDE FTP daemon
Summary(pl): Wu-FTP daemon for KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 2.1, kdelibs = %{version}

%description kwuftpd
Wu-FTP daemon for KDE.

%description -l pl kwuftpd
Zamiennik demona wu-ftp dla KDE.

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
	--with-quota \
	--with-shadow \
 	--with-pam="yes"

make

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=%{_prefix}
make DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KCRON
#################################################
%files kcron -f kcron.lang
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kcron
%config(missingok) %{_applnkdir}/System/kcron.desktop

%attr(644,root,root) %{_datadir}/icons/locolor/*x*/apps/kcron.png

#################################################
#             KDAT
#################################################
%files kdat -f kdat.lang
%defattr(644, root, root, 755)

%attr(755, root, root) %{_bindir}/kdat

%config(missingok) %{_applnkdir}/Utilities/kdat.kdelnk

%attr(644,root,root) %{_datadir}/icons/hicolor/*x*/apps/kdat.png
%attr(644,root,root) %{_datadir}/icons/locolor/*x*/apps/kdat.png

%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/kdat_*.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/closed.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/open.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/package.png

#################################################
#             KPACKAGE
#################################################
%files kpackage
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kpackage*

%config(missingok) %{_applnkdir}/Utilities/kpackage.desktop

%{_datadir}/apps/kpackage/

%attr(644,root,root) %{_datadir}/icons/locolor/*x*/apps/kpackage.png

%attr(644,root,root) %{_datadir}/icons/locolor/16x16/mimetypes/*file.png
%attr(644,root,root) %{_datadir}/icons/locolor/32x32/apps/*file.png

%{_datadir}/mimelnk/application/x-debian-package.kdelnk
%{_datadir}/mimelnk/application/x-rpm.kdelnk

#################################################
#             KSYSCONTROL
#################################################
%files ksyscontrol
%defattr(644, root, root, 755)

%attr(755,root,root) %{_bindir}/ksysctrl
%attr(755,root,root) %{_bindir}/printversion

%config(missingok) %{_applnkdir}/System/ksysctrl.desktop

%{_datadir}/apps/ksysctrl/

%attr(644,root,root) %{_datadir}/icons/locolor/*x*/apps/kpackage.png

%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/audio.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/cdrom.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/conflict.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/connector.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/display.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/drivectrl.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/network.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/printer.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/res.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/scsi.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/storage.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/system.png
%attr(644,root,root) %{_datadir}/icons/locolor/16x16/apps/usb.png

%attr(644,root,root) %{_datadir}/toolbar/audio.png
%attr(644,root,root) %{_datadir}/toolbar/cdrom.png
%attr(644,root,root) %{_datadir}/toolbar/confmark.png
%attr(644,root,root) %{_datadir}/toolbar/connector.png
%attr(644,root,root) %{_datadir}/toolbar/display.png
%attr(644,root,root) %{_datadir}/toolbar/network.png
%attr(644,root,root) %{_datadir}/toolbar/printer.png
%attr(644,root,root) %{_datadir}/toolbar/scaner.png
%attr(644,root,root) %{_datadir}/toolbar/scsi.png
%attr(644,root,root) %{_datadir}/toolbar/storage.png
%attr(644,root,root) %{_datadir}/toolbar/system.png
%attr(644,root,root) %{_datadir}/toolbar/tuxscreen.png
%attr(644,root,root) %{_datadir}/toolbar/usb.png

#################################################
#             KSYSV
#################################################
%files ksysv
%defattr(644, root, root, 755)

%{_datadir}/apps/ksysv/

%{_datadir}/icons/hicolor/*x*/ksysv.png
%{_datadir}/icons/locolor/*x*/ksysv.png

#################################################
#             KUSER
#################################################
%files kuser
%defattr(644, root, root, 755)

%attr(755, root, root) %{_bindir}/kuser

%config(missingok) %{_applnkdir}/System/kuser.desktop

%{_datadir}/apps/kuser/

%{_datadir}/icons/hicolor/*x*/kuser.png
%{_datadir}/icons/locolor/16x16/kuser.png
%{_datadir}/icons/locolor/32x32/kuser.png

%{_datadir}/icons/locolor/22x22/actions/add_*.png
%{_datadir}/icons/locolor/22x22/actions/delete_*.png
%{_datadir}/icons/locolor/22x22/actions/edit_*.png

#################################################
#             KWUFTPD
#################################################
%files kwuftpd
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kwuftpd

%config(missingok) %{_allpnkdir}/System/kwuftpd.desktop
