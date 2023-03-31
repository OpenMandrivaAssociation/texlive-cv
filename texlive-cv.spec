Name:		texlive-cv
Version:	15878
Release:	2
Summary:	A package for creating a curriculum vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cv
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cv.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
