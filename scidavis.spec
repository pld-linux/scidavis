Summary:	Scientific Data Analysis and Visualization
Name:		scidavis
Version:	0.2.3
Release: 	5%{?dist}
Source0:	http://download.sourceforge.net/sourceforge/scidavis/%{name}-%{version}.tar.bz2
Source1:	http://download.sourceforge.net/sourceforge/scidavis/scidavis-manual-0.1_2008-02-28.tar.bz2
Patch0:		scidavis-0.2.3-manual.patch
Patch1:		scidavis-0.2.3-pro.patch
URL:		http://scidavis.sourceforge.net/
License:	GPLv2
Group: 		Applications/Engineering
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: desktop-file-utils
BuildRequires: gsl-devel python-devel muParser-devel qwt-devel qwtplot3d-qt4-devel qt4-devel sip-devel PyQt4-devel dos2unix
Requires: hicolor-icon-theme

%description
SciDAVis is a user-friendly data analysis and visualization program primarily
aimed at high-quality plotting of scientific data. It strives to combine an
intuitive, easy-to-use graphical user interface with powerful features such
as Python scriptability.

%package manual
Summary:	Additional manual for SciDAVis
Group:		Documentation

%description manual
This package contains the manual for SciDAVis.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1

sed -i -e 's/50/100/' scidavis/scidavis.xml

%build
cd scidavis
qmake-qt4 scidavis.pro
make %{?_smp_mflags}

%install
cd scidavis
rm -rf %{buildroot}
make INSTALL_ROOT="%{buildroot}" install
install -d %{buildroot}%{_datadir}/applications
desktop-file-install --vendor fedora \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}/%{_datadir}/applications/scidavis.desktop

rm %{buildroot}/%{_datadir}/applications/scidavis.desktop

install -d %{buildroot}%{_datadir}/%{name}/translations
install -D -pm 644 translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/

mkdir %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes/
mkdir %{buildroot}%{_datadir}/icons/hicolor/64x64/mimetypes/
cp %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/scidavis.png %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes/.
cp %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/scidavis.png %{buildroot}%{_datadir}/icons/hicolor/64x64/mimetypes/.
mv %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes/scidavis.png %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes/application-x-sciprj.png
mv %{buildroot}%{_datadir}/icons/hicolor/64x64/mimetypes/scidavis.png %{buildroot}%{_datadir}/icons/hicolor/64x64/mimetypes/application-x-sciprj.png

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
	%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
	%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES README gpl.txt
%exclude %{_sysconfdir}/scidavisrc.pyo
%exclude %{_sysconfdir}/scidavisrc.pyc
%{_bindir}/scidavis
#%{_libdir}/scidavis/
%{_datadir}/applications/*
%{_datadir}/mime/packages/scidavis.xml
%{_datadir}/mimelnk/application/x-sciprj.desktop
%{_datadir}/icons/hicolor/*/mimetypes/application-x-sciprj*
%{_datadir}/icons/hicolor/*/apps/scidavis.*
%{_datadir}/icons/locolor/*/apps/scidavis.*
%{_datadir}/scidavis
%{_sysconfdir}/scidavisrc.py

%files manual
%defattr(-,root,root,-)
%doc manual/*

%changelog
* Sun Jul 19 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.2.3-5
- Rebuild

* Sun Jul 19 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.2.3-4
- Rebuild

* Fri Jul 17 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.2.3-3
- Patch for manual path

* Mon Jul 13 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.2.3-2
- BZ #510968

* Sun Jul 05 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.2.3-1
- Update to 0.2.3

* Wed Apr 22 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.2.2-1
- Update to 0.2.2

* Sat Apr 10 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.2.1-1
- Update to 0.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 09 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.1.4-1
- Update to 0.1.4

* Sun Jan 11 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.1.3-7
- Replace the sip patch by a better one from upstream

* Sun Jan 11 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.1.3-6
- Replace the sip patch by the one from upstream

* Wed Jan 07 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.1.3-5
- Rebuild

* Wed Jan 07 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.3-4
- sip patch (#479118)

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.3-3
- Rebuild for Python 2.6

* Wed Apr 23 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.1.3-2
- Handle correctly the icons

* Wed Apr 23 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.1.3-1
- Update to 0.1.3

* Mon Feb 25 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.1.2-1
- Initial build
