
%define         _state          stable                                        
%define         _ver		3.1.1

Summary:	K Desktop Environment - administrative tools
Summary(es):	K Desktop Environment - herramientas administrativas
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - °ü¸® µµ±¸
Summary(pl):	K Desktop Environment - narzêdzia administratora
Summary(pt_BR):	K Desktop Environment - ferramentas administrativas
Summary(zh_CN):	KDE¹ÜÀí¹¤¾ß
Name:		kdeadmin
Version:	%{_ver}
Release:	0.3
Epoch:		7
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Icon:		kde-icon.xpm
Requires:	kdelibs >= %{version}
Requires:	pam
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
# Required by kpackage (RPM frontend). Dependency taken from librpm.la
# by libtool.
BuildRequires:	kdelibs-devel = %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	rpm-devel
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%define		no_install_post_chrpath		1

%description
KDE administrative tools. Package includes:
- KCron - KDE Cron daemon
- KDat - Tape backup tool
- KUser - KDE user setup tool
- KSYSV - SYS V Init configuration
- KPackage - KDE support for RPM
- Kwuftpd - KDE ftp daemon
- Kcmlinuz - KDE Linux Kernel Configuration

%description -l es
Herramientas administrativas para KDE. Incluidos en este paquete:
- KSYSV - editor de los archivos de iniciación sysV,
- KUser - herramienta de gestión de usuarios.

%description -l pl
Aplikacje administratorskie dla KDE. Pakiet zawiera:
- KCron - Program cron
- KDat - Narzêdzie do wykonywania kopii zapasowych na ta¶mie.
- KUser - Program do zarz±dzania kontami u¿ytkowników
- KSYSV - Program do konfiguracji startu systemu
- KPackage - Program do zarz±dzania pakietami
- Kwuftpd - Demon FTP dla KDE
- Kcmlinuz - Konfigurator j±dra Linuxa dla KDE

%package kcmlinuz
Summary:	KDE Linux Kernel Configuration
Summary(pl):	Konfigurator j±dra Linuksa dla KDE
Summary(pt_BR):	Configurador do Kernel Linux
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name}-kwuftpd

%description kcmlinuz
A Linux kernel configurator for KDE.

%description kcmlinuz -l pl
Program do konfiguracji j±dra Linuksa.

%description kcmlinuz -l pt_BR
Configurador do Kernel Linux.

%package kdat
Summary:	Tape backup tool
Summary(pl):	Narzêdzie do wykonywania kopii zapasowych na ta¶mie
Group:		X11/Applications
Requires:       kdelibs >= %{version}
Obsoletes:	%{name}-kwuftpd

%description kdat
Tape backup tool.

%description kdat -l pl
Narzêdzie do wykonywania kopii zapasowych na ta¶mie.

%package kcron
Summary:	KDE cron daemon
Summary(pl):	Program cron
Summary(pt_BR):	Gerenciador/agendador de tarefas e interface para o cron
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name}-kwuftpd

%description kcron
Kde version of "CRON".

%description kcron -l pl
Program "cron" w wersji dla KDE.

%description kcron -l pt_BR
Gerenciador/agendador de tarefas e interface para o cron.

%package kpackage
Summary:	RPM front-end KDE
Summary(pl):	Program do manipulacji pakietami
Summary(pt_BR):	Interface para gerenciamento de pacotes RPM/DEB
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Provides:	kpackage
Obsoletes:	kpackage
Obsoletes:	%{name}-kwuftpd

%description kpackage
Package front-end for KDE.

%description kpackage -l pl
Program do manipulowania pakietami w ¶rodowisku KDE.

%description kpackage -l pt_BR
Interface para gerenciamento de pacotes RPM/DEB.

%package ksysv
Summary:	KDE Sys V Init configurator
Summary(pl):	Konfigurator Sys V Init dla KDE
Summary(pt_BR):	Interface para administração da inicialização System V
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name}-kwuftpd

%description ksysv
A Sys V Init configurator for KDE.

%description ksysv -l pl
Program do konfiguracji startu systemu wykorzystuj±cego Sys V Init.

%description ksysv -l pt_BR
Interface para administração da inicialização System V, com
visualização e manipulação gráfica e facilitada dos serviços
disponíveis bem como dos níveis de execução.

%package kuser
Summary:	KDE User management tool
Summary(pl):	Administracja kontami dla KDE
Summary(pt_BR):	Ferramenta para administração de usuários
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name}-kwuftpd

%description kuser
A simple tool for adding/removing users from system and changing user
information.

%description kuser -l pl
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o
nich.

%description kuser -l pt_BR
Ferramenta para administração de usuários do sistema.

%package kwuftpd
Summary:	KDE FTP daemon
Summary(pl):	Wu-FTP daemon for KDE
Summary(pt_BR):	Ferramenta de administração gráfica do WU-FTPD
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	wu-ftpd

%description kwuftpd
Wu-FTP daemon for KDE.

%description kwuftpd -l pl
Zamiennik demona wu-ftp dla KDE.

%description kwuftpd -l pt_BR
Ferramenta de administração gráfica do WU-FTPD (servidor FTP).

%package kxconfig
Summary:	X Window Configuration
Summary(pl):	Konfiguracja X Window
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name}-kwuftpd

%description kxconfig
X Window Configuration Tool.

%description kxconfig -l pl
Narzêdzie do konfiguracji X Window..

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CXXFLAGS="%{rpmcflags} -Wall"
CFLAGS="%{rpmcflags} -Wall"

for plik in `find ./ -name *.desktop` ; do

if [ -d $plik ]; then
	echo $plik
	sed -ie "s/[nb]/[no]/g" $plik
	fi

done
				

%configure \
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
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Settings/KDE,System/Administration}

KDEDIR=%{_prefix} ; export KDEDIR
%{__make} DESTDIR=$RPM_BUILD_ROOT install

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv -f $ALD/System/{More/*.desktop,.}
mv -f $ALD/System/{{ksysv,kuser}.desktop,Administration}
mv -f $ALD/{Settings/Peripherals/kxconfig.desktop,System/Administration}
mv -f $ALD/Settings/{[!K]*,KDE}

cd $ALD/System/Administration
cat kxconfig.desktop |sed -e 's/Icon=xapp/Icon=kxconfig/' \
    > kxconfig.desktop.tmp
mv kxconfig.desktop.tmp kxconfig.desktop
cd -

cd $RPM_BUILD_ROOT%{_pixmapsdir}
mv {locolor,crystalsvg}/16x16/apps/kxconfig.png
cd -

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

#%find_lang kcmlilo	--with-kde
#%find_lang kcmlinuz	--with-kde
#cat kcmlilo.lang >> kcmlinuz.lang
%find_lang kcron	--with-kde
%find_lang kdat		--with-kde
%find_lang kpackage	--with-kde
#%find_lang ksysctrl	--with-kde
%find_lang ksysv	--with-kde
#cat ksysctrl.lang >> ksysv.lang
%find_lang kuser	--with-kde
%find_lang kwuftpd	--with-kde
%find_lang kxconfig	--with-kde
#%find_lang secpolicy	--with-kde
#cat secpolicy.lang >> ksysv.lang

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KCMLINUZ
#################################################
#%files kcmlinuz -f kcmlinuz.lang
%files kcmlinuz
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_li*.la
%attr(755,root,root) %{_libdir}/kde3/kcm_li*.so
%{_datadir}/apps/kcmlinuz
%{_applnkdir}/Settings/KDE/System/li*.desktop

#################################################
#             KCRON
#################################################
%files kcron -f kcron.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcron
%{_datadir}/pixmaps/*/*/*/kcron.png
%{_applnkdir}/System/kcron.desktop

#################################################
#             KDAT
#################################################
%files kdat -f kdat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdat
%{_datadir}/apps/kdat
%{_applnkdir}/System/kdat.desktop
%{_applnkdir}/Utilities/kdat.desktop
%{_pixmapsdir}/[!l]*/*/*/kdat*

#################################################
#             KPACKAGE
#################################################
%files kpackage -f kpackage.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackage
%{_libdir}/kde3/kfile*.la
%attr(755,root,root) %{_libdir}/kde3/kfile*.so
%{_datadir}/apps/kpackage
%{_datadir}/mimelnk/application/x-debian-package.desktop
%{_datadir}/services/kfile*
%{_applnkdir}/System/kpackage.desktop
%{_pixmapsdir}/*/*/*/kpackage.png

#################################################
#             KSYSV
#################################################
%files ksysv -f ksysv.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/secpolicy
%attr(755,root,root) %{_bindir}/ksysv
%{_datadir}/apps/ksysv
%{_datadir}/mimelnk/application/x-ksysv.desktop
%{_datadir}/mimelnk/text/x-ksysv-log.desktop
%{_applnkdir}/System/Administration/ksysv.desktop
%{_pixmapsdir}/*/*/*/ksysv.png
%{_pixmapsdir}/*/*/*/toggle_log.png

#################################################
#             KUSER
#################################################
%files kuser -f kuser.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuser
%{_datadir}/apps/kuser
%{_applnkdir}/System/Administration/kuser.desktop
%{_pixmapsdir}/*/*/*/kuser.png

#################################################
#             KWUFTPD
#################################################
#%files kwuftpd -f kwuftpd.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kwuftpd
#%{_applnkdir}/System/kwuftpd.desktop

#################################################
#             KXCONFIG
#################################################
%files kxconfig -f kxconfig.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxconfig
%{_datadir}/apps/kxconfig
%{_applnkdir}/System/Administration/kxconfig.desktop
%{_pixmapsdir}/*/*/*/kxconfig*
