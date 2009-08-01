%define upstream_name	 HTML-Widget
%define upstream_version 1.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	HTML Widget And Validation Framework
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

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
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl(Module::Pluggable::Fast)
Requires:	perl(Class::Accessor::Chained::Fast)

%description
Create easy to maintain HTML widgets!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/HTML
