%define real_name Convert-ASN1
%define name perl-%{real_name}
%define version 0.21
%define release %mkrel 1

Summary: 	ASN.1 Encode/Decode library for perl
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://www.cpan.org/authors/id/GBARR/%{real_name}-%{version}.tar.bz2
URL: 		http://search.cpan.org/dist/%{real_name}/
BuildRequires:	perl-devel
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-buildroot/
Requires:	perl

%description
Perl module used to encode and decode ASN.1 data structures using
BER/DER rules.

Needed by webmin to handle the OpenLDAP modules properly.

%prep

%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README examples/*
%{perl_vendorlib}/Convert/*
%{_mandir}/*/*

