%define upstream_name    Convert-ASN1
Summary:	ASN.1 Encode/Decode library for perl
Name:		perl-%{upstream_name}
Version:	0.34
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/gbarr/perl-Convert-ASN1
Source0:	https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Convert-ASN1-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Math::BigInt)
BuildRequires:	perl-devel

%description
Perl module used to encode and decode ASN.1 data structures using
BER/DER rules.

Needed by webmin to handle the OpenLDAP modules properly.

%prep
%setup -qn %{upstream_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog  examples/*
%{perl_vendorlib}/Convert/*
%{_mandir}/man3/*


