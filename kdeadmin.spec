%define		REV	20000418
Summary:	K Desktop Environment - administrative tools
Summary(pl):	K Desktop Environment - narzêdzia administratora
Name:		kdeadmin
Version:	2.0
Release:	1.pre_%{REV}
License:	GPL
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Vendor:		The KDE Team
Source0:	ftp://ftp.kde.org/pub/kde/snapshots/current/%{name}-%{REV}.tar.bz2
Requires:	qt >= 2.1, kdelibs = %{version}, pam
BuildRequires:	kdelibs-devel
BuildRequires:	rpm-devel >= 3.0.4
BuildRequires:	pam-devel >= 0.71
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix	/usr/X11R6

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
%setup -q -n %{name}

%build
%{__make} -f Makefile.cvs
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
%{__make} DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KCRON
#################################################
%files kcron
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kcron
%{_applnkdir}/System/kcron.desktop

%{_datadir}/icons/locolor/*x*/apps/kcron.png

#################################################
#             KDAT
#################################################
%files kdat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdat

%{_applnkdir}/Utilities/kdat.desktop

%{_datadir}/icons/hicolor/*x*/apps/kdat.png
%{_datadir}/icons/locolor/*x*/apps/kdat.png

%{_datadir}/icons/locolor/16x16/apps/kdat_*.png
%{_datadir}/icons/locolor/16x16/apps/closed.png
%{_datadir}/icons/locolor/16x16/apps/open.png
%{_datadir}/icons/locolor/16x16/apps/package.png

#################################################
#             KPACKAGE
#################################################
%files kpackage
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kpackage*

%{_applnkdir}/Utilities/kpackage.desktop

%{_datadir}/apps/kpackage

%{_datadir}/icons/locolor/*x*/apps/kpackage.png
%{_datadir}/icons/locolor/16x16/mimetypes/*file.png
%{_datadir}/icons/locolor/32x32/apps/*file.png

%{_datadir}/mimelnk/application/x-debian-package.kdelnk
%{_datadir}/mimelnk/application/x-rpm.kdelnk

#################################################
#             KSYSCONTROL
#################################################
%files ksysctrl
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/ksysctrl
%attr(755,root,root) %{_bindir}/printversion

%{_applnkdir}/System/ksysctrl.desktop

%{_datadir}/apps/ksysctrl

%{_datadir}/icons/locolor/*x*/apps/kpackage.png

%{_datadir}/icons/locolor/16x16/apps/audio.png
%{_datadir}/icons/locolor/16x16/apps/cdrom.png
%{_datadir}/icons/locolor/16x16/apps/conflict.png
%{_datadir}/icons/locolor/16x16/apps/connectors.png
%{_datadir}/icons/locolor/16x16/apps/display.png
%{_datadir}/icons/locolor/16x16/apps/drivectrl.png
%{_datadir}/icons/locolor/16x16/apps/network.png
%{_datadir}/icons/locolor/16x16/apps/printer.png
%{_datadir}/icons/locolor/16x16/apps/res.png
%{_datadir}/icons/locolor/16x16/apps/scsi.png
%{_datadir}/icons/locolor/16x16/apps/storage.png
%{_datadir}/icons/locolor/16x16/apps/system.png
%{_datadir}/icons/locolor/16x16/apps/usb.png

%{_datadir}/toolbar/audio.png
%{_datadir}/toolbar/cdrom.png
%{_datadir}/toolbar/confmark.png
%{_datadir}/toolbar/connectors.png
%{_datadir}/toolbar/display.png
%{_datadir}/toolbar/network.png
%{_datadir}/toolbar/printer.png
%{_datadir}/toolbar/scanner.png
%{_datadir}/toolbar/scsi.png
%{_datadir}/toolbar/storage.png
%{_datadir}/toolbar/system.png
%{_datadir}/toolbar/tuxscreen.png
%{_datadir}/toolbar/usb.png

#################################################
#             KSYSV
#################################################
%files ksysv
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/secpolicy

%{_datadir}/apps/ksysv

%{_datadir}/icons/hicolor/*x*/apps/ksysv.png
%{_datadir}/icons/locolor/*x*/apps/ksysv.png

#################################################
#             KUSER
#################################################
%files kuser
%defattr(644,root,root,755)

%attr(755, root, root) %{_bindir}/kuser

%{_applnkdir}/System/kuser.desktop

%{_datadir}/apps/kuser

%{_datadir}/icons/hicolor/*x*/apps/kuser.png
%{_datadir}/icons/locolor/16x16/apps/kuser.png
%{_datadir}/icons/locolor/32x32/apps/kuser.png

%{_datadir}/icons/locolor/22x22/actions/add_*.png
%{_datadir}/icons/locolor/22x22/actions/delete_*.png
%{_datadir}/icons/locolor/22x22/actions/edit_*.png

#################################################
#             KWUFTPD
#################################################
%files kwuftpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwuftpd
%{_applnkdir}/System/kwuftpd.desktop
