%define upstream_name	 HTML-Widget
%define upstream_version 1.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	HTML Widget And Validation Framework
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Chained::Fast)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::Data::Accessor)
BuildRequires:	perl(Date::Calc)
BuildRequires:	perl(Email::Valid)
BuildRequires:	perl(HTML::Element) >= 3.22
BuildRequires:	perl(HTML::Scrubber)
BuildRequires:	perl(Module::Pluggable::Fast)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Test::NoWarnings)
BuildArch:	noarch
Requires:	perl(Module::Pluggable::Fast)
Requires:	perl(Class::Accessor::Chained::Fast)

%description
Create easy to maintain HTML widgets!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Disable for now as in fact tests pass, only extra new line in output makes them fail
#make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/HTML


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 406377
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.11-5mdv2009.0
+ Revision: 257243
- rebuild

* Thu Dec 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-3mdv2008.1
+ Revision: 138297
- fix dependencies again

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-2mdv2008.1
+ Revision: 138100
- fix dependencies

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.11-1mdv2008.0
+ Revision: 20151
- 1.11


* Thu Aug 17 2006 Scott Karns <scottk@mandriva.org>
+ 08/17/06 02:11:44 (56537)
Version 1.08

* Sat Aug 12 2006 Scott Karns <scottk@mandriva.org>
+ 08/12/06 13:35:06 (55741)
- Rebuild
- Spec file cleanup

* Sat Aug 12 2006 Scott Karns <scottk@mandriva.org>
+ 08/12/06 13:24:44 (55735)
import perl-HTML-Widget-1.07-2mdv2007.0

* Fri Jun 16 2006 Scott Karns <scottk@mandriva.org> 1.07-2mdv2007.0
- added BuildRequires perl(Test::NoWarnings)

* Tue May 02 2006 Scott Karns <scottk@mandriva.org> 1.07-1mdk
- version 1.07
- BuildRequires updated for new version

* Thu Apr 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdk
- new version
- rpmbuildupdate aware
- spec cleanup
- better buildrequires syntax
- fix directory ownership

* Sat Mar 25 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.05-2mdk
- Add BuildRequires

* Fri Mar 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.05-1mdk
- First Mandriva release

