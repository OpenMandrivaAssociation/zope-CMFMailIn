%define Product CMFMailIn
%define product cmfmailin
%define name    zope-%{Product}
%define version 1.0.0
%define release %mkrel 10

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


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-10mdv2010.0
+ Revision: 435494
- rebuild
- rebuild

* Sat Aug 09 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-8mdv2009.0
+ Revision: 269877
- rebuild early 2009.0 package (before pixel changes)

* Sun May 11 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.0-7mdv2009.0
+ Revision: 205681
- Should not be noarch ed

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-6mdv2008.0
+ Revision: 91827
- spec cleanup
  package renaming
- package renaming
- import CMFMailIn

