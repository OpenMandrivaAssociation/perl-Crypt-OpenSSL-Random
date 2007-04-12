%define name	perl-Crypt-OpenSSL-Random
%define module  Crypt-OpenSSL-Random
%define version	0.03
%define release %mkrel 9

Summary:	Crypt-OpenSSL-Random module for perl 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/I/IR/IROBERTS/Crypt-OpenSSL-Random-0.03.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
Requires:	openssl
Buildrequires: perl-devel
Buildrequires: openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
#BuildArch:	noarch

%description
Crypt-OpenSSL-Random module for perl

%prep
%setup -q -n %{module}-%{version} 
# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} </dev/null
%{__make}
%{__make} test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes 
%{perl_vendorlib}/*/auto/Crypt/OpenSSL/Random/Random.so
%{perl_vendorlib}/*/auto/Crypt/OpenSSL/Random/autosplit.ix
%{perl_vendorlib}/*/Crypt/OpenSSL/Random.pm
%{_mandir}/*/*

