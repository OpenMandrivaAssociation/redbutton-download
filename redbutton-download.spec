Name:           redbutton-download
Version:        20090727
Release:        %mkrel 2
Group:          Development/Other 
License:        GPLv2+
Summary:        Redbutton download for MHEG5 content
Source:         redbutton-download-%{version}.tar.gz
URL:            http://redbutton.sourceforge.net/
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

