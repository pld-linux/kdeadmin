#
# Conditional build:
%bcond_without	i18n	# don't build i18n subpackages
#
%define		_state		stable
%define		_ver		3.2.1
##%define		_snap		040110

Summary:	K Desktop Environment - administrative tools
Summary(es):	K Desktop Environment - herramientas administrativas
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - °ü¸® µµ±¸
Summary(pl):	K Desktop Environment - narzêdzia administratora
Summary(pt_BR):	K Desktop Environment - ferramentas administrativas
Summary(zh_CN):	KDE¹ÜÀí¹¤¾ß
Name:		kdeadmin
Version:	%{_ver}
Release:	0.1
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{_ver}/src/%{name}-%{_ver}.tar.bz2
# Source0-md5:	1ff46933b955cb4bc71cd533c6f730d1
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
%if %{with i18n}
Source1:        kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	eed79dbaa88ff33cf37d86edb3c6e767
%endif
Patch0:		%{name}-3.2branch.diff
Patch1:		%{name}-vcategories.patch
Patch2:		%{name}-gcc34.patch
Icon:		kde-icon.xpm
URL:		http://www.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	ed
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
#BuildRequires:	lilo
BuildRequires:	pam-devel
BuildRequires:	rpm-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE administrative tools. Package includes:
- KCron - KDE Cron daemon,
- KDat - Tape backup tool,
- KUser - KDE user setup tool,
- KSYSV - SYS V Init configuration,
- KPackage - KDE support for RPM,
- Kwuftpd - KDE ftp daemon configuration,
- Kcmlinuz - KDE Linux Kernel Configuration.

%description -l es
Herramientas administrativas para KDE. Incluidos en este paquete:
- KSYSV - editor de los archivos de iniciación sysV,
- KUser - herramienta de gestión de usuarios.

%description -l pl
Aplikacje administratorskie dla KDE. Pakiet zawiera:
- KCron - program cron,
- KDat - narzêdzie do wykonywania kopii zapasowych na ta¶mie,
- KUser - program do zarz±dzania kontami u¿ytkowników,
- KSYSV - program do konfiguracji startu systemu,
- KPackage - program do zarz±dzania pakietami,
- Kwuftpd - konfigurator demona FTP dla KDE,
- Kcmlinuz - konfigurator j±dra Linuksa dla KDE.

%package kcmlilo
Summary:	LILO Configurator
Summary(pl):	Konfigurator LILO
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	lilo
Obsoletes:	%{name}-kcmlinuz < 8:3.1.93.031105-3

%description kcmlilo
LILO configurator for KDE.

%description kcmlilo -l pl
Konfigurator LILO dla KDE.

%package kcmlinuz
Summary:	KDE Linux Kernel Configuration
Summary(pl):	Konfigurator j±dra Linuksa dla KDE
Summary(pt_BR):	Configurador do Kernel Linux
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdat

%description kdat
Tape backup tool.

%description kdat -l pl
Narzêdzie do wykonywania kopii zapasowych na ta¶mie.

%package kcron
Summary:	KDE cron daemon
Summary(pl):	Program cron dla KDE
Summary(pt_BR):	Gerenciador/agendador de tarefas e interface para o cron
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}
Provides:	kpackage
Obsoletes:	kpackage

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
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

%description kuser
A simple tool for adding/removing users from system and changing user
information.

%description kuser -l pl
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o
nich.

%description kuser -l pt_BR
Ferramenta para administração de usuários do sistema.

%package kwuftpd
Summary:	KDE WU-FTP daemon configurator
Summary(pl):	Konfigurator demona WU-FTP dla KDE
Summary(pt_BR):	Ferramenta de administração gráfica do WU-FTPD
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Requires:	wu-ftpd

%description kwuftpd
WU-FTP daemon configurator for KDE.

%description kwuftpd -l pl
Narzêdzie do konfiguracji demona WU-FTP dla KDE.

%description kwuftpd -l pt_BR
Ferramenta de administração gráfica do WU-FTPD (servidor FTP).

%package i18n
Summary:	Common internationalization and localization files for kdeadmin
Summary(pl):	Wspó³dzielone pliki umiêdzynarodawiaj±ce dla pakietów kdeadmin
Group:		X11/Applications
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Common internationalization and localization files for kdeadmin.

%description i18n -l pl
Wspó³dzielone pliki umiêdzynarodawiaj±ce dla pakietów kdeadmin.

%package kcron-i18n
Summary:	Internationalization and localization files for kcron
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcrona
Group:		X11/Applications
Requires:	%{name}-kcron = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kcron-i18n
Internationalization and localization files for kcron.

%description kcron-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcrona.

%package kdat-i18n
Summary:	Internationalization and localization files for kdat
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdat
Group:		X11/Applications
Requires:	%{name}-kdat = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kdat-i18n
Internationalization and localization files for kdat.

%description kdat-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdat.

%package kpackage-i18n
Summary:	Internationalization and localization files for kpackage
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpackage
Group:		X11/Applications
Requires:	%{name}-kpackage = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kpackage-i18n
Internationalization and localization files for kpackage.

%description kpackage-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kpackage.

%package ksysv-i18n
Summary:	Internationalization and localization files for ksysv
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksysv
Group:		X11/Applications
Requires:	%{name}-ksysv = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ksysv-i18n
Internationalization and localization files for ksysv.

%description ksysv-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksysv.

%package kuser-i18n
Summary:	Internationalization and localization files for kuser
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kusera
Group:		X11/Applications
Requires:	%{name}-kuser = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kuser-i18n
Internationalization and localization files for kuser.

%description kuser-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kusera.

%package kcmlilo-i18n
Summary:	Internationalization and localization files for kcmlilo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcmlilo
Group:		X11/Applications
Requires:	%{name}-kcmlilo = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kcmlilo-i18n
Internationalization and localization files for kcmlilo.

%description kcmlilo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcmlilo.

%package kcmlinuz-i18n
Summary:	Internationalization and localization files for kcmlinuz
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcmlinuz
Group:		X11/Applications
Requires:	%{name}-kcmlinuz = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kcmlinuz-i18n
Internationalization and localization files for kcmlinuz.

%description kcmlinuz-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcmlinuz.

%prep
%setup -q 
#%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp /usr/share/automake/config.sub admin

# Do not check for lilo
rm lilo-config/configure.in.in

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
 	--with-pam=yes \
	--with-qt-libraries=%{_libdir} \
	--with-shadow

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
			rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi
%endif

%find_lang kcron	--with-kde
%find_lang kdat		--with-kde
%find_lang kpackage	--with-kde
%find_lang ksysv	--with-kde
%find_lang kuser	--with-kde

%if %{with i18n}
%find_lang desktop_kdeadmin	--with-kde
%find_lang kcmlinuz	--with-kde
%find_lang kcmlilo	--with-kde
%find_lang kfile_deb	--with-kde
cat kfile_deb.lang >> kpackage.lang
%find_lang kfile_rpm	--with-kde
cat kfile_rpm.lang >> kpackage.lang
%find_lang secpolicy	--with-kde
cat secpolicy.lang >> ksysv.lang
%endif

files="kcron \
kdat \
kpackage \
ksysv \
kuser"

for i in $files; do
	> ${i}_en.lang
	echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

durne=`ls -1 *.lang|grep -v _en`

for i in $durne; 
do
	echo $i >> control
	grep -v en\/ $i|grep -v apidocs >> ${i}.1
	if [ -f ${i}.1 ] ; then
		mv ${i}.1 ${i}
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with i18n}
%files i18n -f desktop_kdeadmin.lang
%files kcron-i18n -f kcron.lang
%files kdat-i18n -f kdat.lang
%files kpackage-i18n -f kpackage.lang
%files ksysv-i18n -f ksysv.lang
%files kuser-i18n -f kuser.lang
%files kcmlinuz-i18n -f kcmlinuz.lang
%ifarch %{ix86} 
%files kcmlilo-i18n -f kcmlilo.lang
%endif
%endif

%ifarch %{ix86}
%files kcmlilo
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_lilo.la
%attr(755,root,root) %{_libdir}/kde3/kcm_lilo.so
%{_desktopdir}/kde/lilo.desktop
%endif

%files kcmlinuz
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_linuz.la
%attr(755,root,root) %{_libdir}/kde3/kcm_linuz.so
%{_datadir}/apps/kcmlinuz
%{_desktopdir}/kde/linuz.desktop

%files kcron -f kcron_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcron
%{_desktopdir}/kde/kcron.desktop
%{_iconsdir}/*/*/*/kcron.png

%files kdat -f kdat_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdat
%{_datadir}/apps/kdat
%{_desktopdir}/kde/kdat.desktop
%{_iconsdir}/[!l]*/*/*/kdat*

%files kpackage -f kpackage_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackage
%{_libdir}/kde3/kfile*.la
%attr(755,root,root) %{_libdir}/kde3/kfile*.so
%{_datadir}/apps/kpackage
%{_datadir}/mimelnk/application/x-debian-package.desktop
%{_datadir}/services/kfile*
%{_desktopdir}/kde/kpackage.desktop
%{_iconsdir}/*/*/*/kpackage.png

%files ksysv -f ksysv_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/secpolicy
%attr(755,root,root) %{_bindir}/ksysv
%{_datadir}/apps/ksysv
%{_datadir}/mimelnk/application/x-ksysv.desktop
%{_datadir}/mimelnk/text/x-ksysv-log.desktop
%{_desktopdir}/kde/ksysv.desktop
%{_iconsdir}/*/*/*/ksysv.png
%{_iconsdir}/*/*/*/toggle_log.png

%files kuser -f kuser_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuser
%{_datadir}/apps/kuser
%{_desktopdir}/kde/kuser.desktop
%{_iconsdir}/*/*/*/kuser.png
