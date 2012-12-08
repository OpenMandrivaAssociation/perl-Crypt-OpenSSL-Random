%define upstream_name    Crypt-OpenSSL-Random
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    10
Summary:	Crypt-OpenSSL-Random module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		Crypt-OpenSSL-Random-0.04-link.patch
Buildrequires: perl-devel
Buildrequires: pkgconfig(openssl)

%description
Crypt-OpenSSL-Random module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0
# perl path hack
find . -type f | xargs %__perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%__perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} </dev/null
%__make

%check
%__make test

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/*/auto/Crypt/OpenSSL/Random/Random.so
%{perl_vendorlib}/*/auto/Crypt/OpenSSL/Random/autosplit.ix
%{perl_vendorlib}/*/Crypt/OpenSSL/Random.pm
%{_mandir}/*/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-9
+ Revision: 765129
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-8
+ Revision: 763632
- rebuilt for perl-5.14.x

* Wed Nov 30 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.40.0-7
+ Revision: 735520
- rebuild
- cleaned up spec

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-6
+ Revision: 667060
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.40.0-5mdv2011.0
+ Revision: 564391
- rebuild for perl 5.12.1

* Tue Jul 20 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.40.0-4mdv2011.0
+ Revision: 555718
- rebuild

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 0.40.0-3mdv2010.1
+ Revision: 532506
- fix linkage
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-2mdv2010.1
+ Revision: 511613
- rebuilt against openssl-0.9.8m

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 403033
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.04-3mdv2009.0
+ Revision: 223581
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2008.1
+ Revision: 152037
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.0
+ Revision: 56122
- new version


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-9mdv2007.0
- Rebuild

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 0.03-8mdk
- rebuilt against openssl-0.9.8a

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-7mdk
- Fix previous mistake

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-6mdk
- Fix BuildRequires

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.03-5mdk
- rebuild for new perl

* Wed Jun 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.03-4mdk
- Move manpages in the standard location (man3 instead of man3pm)

