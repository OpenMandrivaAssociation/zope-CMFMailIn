%define Product CMFMailIn
%define product cmfmailin
%define name    zope-%{Product}
%define version 1.0.0
%define release %mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    A Zope product to import emails into CMF sites
License:    GPL
Group:      System/Servers
URL:        http://www.zope.org/Members/NIP/ZMailIn
Source:     %{Product}-%{version}.tar.bz2
Obsoletes:  %{Product}
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
CMFMailIn is a Zope product to import emails into CMF sites.

%prep
%setup -q -n %{Product}-%{version}

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/zope/lib/python/Products/%{Product}
cp -pr * %{buildroot}%{_libdir}/zope/lib/python/Products/%{Product}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt INSTALL.txt LICENSE.txt VERSION.txt
%{_libdir}/zope/lib/python/Products/%{Product}
