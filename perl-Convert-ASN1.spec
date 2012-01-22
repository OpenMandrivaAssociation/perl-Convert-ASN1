%define upstream_name    Convert-ASN1
%define upstream_version 0.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary: 	ASN.1 Encode/Decode library for perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/GBARR/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
Perl module used to encode and decode ASN.1 data structures using
BER/DER rules.

Needed by webmin to handle the OpenLDAP modules properly.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README examples/*
%{perl_vendorlib}/Convert/*
%{_mandir}/*/*
