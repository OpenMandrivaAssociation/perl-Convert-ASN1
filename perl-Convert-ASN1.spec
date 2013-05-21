%define upstream_name    Convert-ASN1
%define upstream_version 0.22

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	ASN.1 Encode/Decode library for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/GBARR/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl module used to encode and decode ASN.1 data structures using
BER/DER rules.

Needed by webmin to handle the OpenLDAP modules properly.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-5mdv2012.0
+ Revision: 765109
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-4
+ Revision: 763566
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-3
+ Revision: 763048
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-2
+ Revision: 667052
- mass rebuild

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.1
+ Revision: 409022
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2009.1
+ Revision: 292034
- update to new version 0.22

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.21-2mdv2009.0
+ Revision: 223576
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.21-1mdv2008.1
+ Revision: 136693
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.21-1mdv2008.0
+ Revision: 19816
- 0.21


* Mon Feb 27 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.20-1mdk
- 0.20

* Mon Jun 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.19-2mdk
- rebuild for new Perl

* Mon May 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.19-1mdk
- 0.19

* Fri Apr 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.18-1mdk
- 0.18

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.16-4mdk
- rebuild for new perl
- don't use PREFIX
- rm -rf $RPM_BUILD_ROOT in %%install, not %%build
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.16-3mdk
- rebuild for auto{req,prov}

