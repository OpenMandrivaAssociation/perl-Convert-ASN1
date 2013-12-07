%define upstream_name    Convert-ASN1
%define upstream_version 0.22

Summary:	ASN.1 Encode/Decode library for perl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	11
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/GBARR/%{upstream_name}-%{upstream_version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Perl module used to encode and decode ASN.1 data structures using
BER/DER rules.

Needed by webmin to handle the OpenLDAP modules properly.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README examples/*
%{perl_vendorlib}/Convert/*
%{_mandir}/man3/*

