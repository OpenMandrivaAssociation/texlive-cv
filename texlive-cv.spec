Name:		texlive-cv
Version:	20080630
Release:	1
Summary:	A package for creating a curriculum vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cv
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cv.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package is distributed with two example files; they (and
their formatted output) constitute the only real documentation.
Note that cv is just a package: you choose the overall
formatting by deciding which class to use, while the package
provides the detailed formatting.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
