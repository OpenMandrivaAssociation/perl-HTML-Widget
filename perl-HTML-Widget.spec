%define module	HTML-Widget
%define name	perl-%{module}
%define	modprefix HTML

%define version	1.11
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	HTML Widget And Validation Framework
License:	Artistic/GPL
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel >= 5.8.1
%endif
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
Requires:	perl >= 5.8.1
BuildArch:	noarch

%description
Create easy to maintain HTML widgets!

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}



