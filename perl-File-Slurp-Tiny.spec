%define	modname	File-Slurp-Tiny
%define	modver	0.004

Summary:	Simple perl module to slurp a file (use File::Slurper instead)
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://metacpan.org/pod/File::Slurp::Tiny
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/File-Slurp-Tiny-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Simple perl module to slurp a file

This module is obsolete and provided for compatibility with
legacy applications only. Use File::Slurper instead.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3*/*
