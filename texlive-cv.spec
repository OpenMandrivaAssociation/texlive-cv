# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cv
# catalog-date 2008-06-30 22:37:02 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-cv
Version:	20180303
Release:	1
Summary:	A package for creating a curriculum vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cv
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cv.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is distributed with two example files; they (and
their formatted output) constitute the only real documentation.
Note that cv is just a package: you choose the overall
formatting by deciding which class to use, while the package
provides the detailed formatting.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cv/CV.sty
%doc %{_texmfdistdir}/doc/latex/cv/ApplicationLetter.pdf
%doc %{_texmfdistdir}/doc/latex/cv/ApplicationLetter.tex
%doc %{_texmfdistdir}/doc/latex/cv/CVCTAN.pdf
%doc %{_texmfdistdir}/doc/latex/cv/CVCTAN.tex
%doc %{_texmfdistdir}/doc/latex/cv/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080630-2
+ Revision: 750756
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080630-1
+ Revision: 718193
- texlive-cv
- texlive-cv
- texlive-cv
- texlive-cv

