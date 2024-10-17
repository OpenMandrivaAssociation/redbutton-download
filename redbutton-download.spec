Name:           redbutton-download
Version:        20090727
Release:        3
Group:          Development/Other 
License:        GPLv2+
Summary:        Redbutton download for MHEG5 content
Source:         redbutton-download-%{version}.tar.gz
URL:            https://redbutton.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: 	zlib-devel

%description
This package provides a download utility for MHEG5, which is used to make
user interface on TVs.
It is part of the redbutton tools suite.

%prep
%setup -q

%build
make

%install
%__rm -rf %{buildroot}
mkdir -p %buildroot%_bindir
#make install DESTDIR=%buildroot # happens "/bin" to DESTDIR
install -m 755 rb-download %buildroot%_bindir

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/rb-download



%changelog
* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 20090727-2mdv2011.0
+ Revision: 604378
- rebuild for new zlib

* Sun Nov 29 2009 Olivier Faurax <ofaurax@mandriva.org> 20090727-1mdv2010.1
+ Revision: 471592
- missing buildrequires
- import redbutton-download


* Sun Nov 29 2009 Olivier Faurax <olivier.faurax@laposte.net> 20090727-1mdv2009.1
- Initial package

