%define	name	cttex
%define	version	1.23
%define	release	%mkrel 12

Summary:	Cttex, Thai word separator program
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Distributable
Group:		System/Internationalization
Source0:	%{name}_%{version}.tar.bz2
URL:		http://linux.thai.net/pub/thailinux/cvs/software/cttex/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	locales-th
Patch0:		ctte-121-cflags.patch

%description
The main part of Cttex is a Thai word separator algorithm using
a dictionary. A wrapper for formatting Thai LaTeX document file is provided
to demonstrate the use of this word-sep routine. The program can also
be used as a simple word-sep filter. 

%prep
%setup -q
%patch0 -p1

%build
PATH=$PATH:. %make

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* testfile 
%{_bindir}/%{name}



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.23-11mdv2011.0
+ Revision: 663432
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.23-10mdv2011.0
+ Revision: 603864
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.23-9mdv2010.1
+ Revision: 522423
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.23-8mdv2010.0
+ Revision: 413281
- rebuild

* Sat Mar 07 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.23-7mdv2009.1
+ Revision: 350878
- Fix patch

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.23-6mdv2009.0
+ Revision: 220520
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.23-5mdv2008.1
+ Revision: 149142
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Adam Williamson <awilliamson@mandriva.org>
    - rebuild for new era, clean spec


* Fri May 12 2006 Stefan van der Eijk <stefan@eijk.nu> 1.23-3mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.23-2mdk
- Rebuild

* Sat Jul 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.23-1mdk
- 1.23
- cosmetics
- quiet setup

