Summary:     K Desktop Environment - administrative tools
Summary(pl): K Desktop Environment - narzêdzia administratora
Name:        kdeadmin
Version:     1.0
Release:     7
Copyright:   GPL
Group:       X11/KDE/Admin
Vendor:      The KDE Team
Source:      ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.gz
Requires:    qt >= 1.40, kdelibs = %{version}
BuildRoot:   /tmp/%{name}-%{version}-root

%description
KDE administrative tools.
Package includes:
  KUser - KDE user setup tool
  KSYSV - SYS V Init configuration

%description -l pl
Aplikacje administratorskie dla KDE.
Pakiet zawiera:
  KUser - Program do zarz±dzania kontami u¿ytkowników
  KSYSV - Program do konfiguracji startu systemu

%package -n kuser
Summary:     KDE User management tool
Summary(pl): administracja kontami dla KDE
Group:       X11/KDE/Admin
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kuser
A simple tool for adding/removing users from system and changing
user information.

%description -l pl -n kuser
Narzêdzie do dodawania/usuwania u¿ytkowników oraz do zmiany danych o nich.

%package -n ksysv
Summary:     KDE Sys V Init configurator	
Summary(pl): Konfigurator Sys V Init dla KDE
Group:       X11/KDE/Admin
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n ksysv
A Sys V Init configurator for KDE.

%description -l pl -n ksysv
Program do konfiguracji startu systemu wykorzystuj±cego Sys V Init

%prep
%setup -q

%build
export KDEDIR=/usr/X11R6
CXXFLAGS="$RPM_OPT_FLAGS -Wall" CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure --prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=/usr/X11R6
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

# create wmconfig files
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
DIR=$PWD
cd $RPM_BUILD_ROOT/etc/X11/kde/applnk
for kdelnk in `find . -name "*.kdelnk"` ; do
  PKG=kde`basename $kdelnk|sed -e "s/\.kdelnk$//"`;
  SECT=`dirname $kdelnk|sed -e "s/^\.\/*//"`;
  kdelnk2wmconfig $PKG $kdelnk $RPM_BUILD_ROOT/etc/X11/wmconfig/$PKG KDE/$SECT pl
done
cd $DIR

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KUSER
#################################################

%files -n kuser
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/System/kuser.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekuser
%attr(755, root, root) /usr/X11R6/bin/kuser
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kuser
%lang(ru) /usr/X11R6/share/kde/doc/HTML/ru/kuser
/usr/X11R6/share/kde/apps/kuser/
/usr/X11R6/share/kde/icons/mini/kuser.xpm
/usr/X11R6/share/kde/icons/kuser.xpm
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kuser.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kuser.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kuser.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kuser.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kuser.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kuser.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/kuser.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kuser.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kuser.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kuser.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kuser.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kuser.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kuser.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kuser.mo
%lang(pt) /usr/X11R6/share/locale/pt_*/LC_MESSAGES/kuser.mo
%lang(zh) /usr/X11R6/share/locale/zh_*/LC_MESSAGES/kuser.mo

#################################################
#             KSYSV
#################################################

%files -n ksysv
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/System/ksysv.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeksysv
%attr(755, root, root) /usr/X11R6/bin/ksysv
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/ksysv
/usr/X11R6/share/kde/apps/ksysv/
/usr/X11R6/share/kde/icons/ksysv.xpm
/usr/X11R6/share/kde/icons/mini/ksysv.xpm
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/ksysv.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/ksysv.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/ksysv.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/ksysv.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/ksysv.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/ksysv.mo
%lang(pt) /usr/X11R6/share/locale/pt_*/LC_MESSAGES/ksysv.mo
%lang(zh) /usr/X11R6/share/locale/zh_*/LC_MESSAGES/ksysv.mo

%changelog
* Wed Dec  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-7]
- recompiled against libstdc++.so.2.9.

* Fri Oct 16 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-4]
- created new spec based on kdebase.spec.
