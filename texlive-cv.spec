%global tl_name cv
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A package for creating a curriculum vitae
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cv
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is distributed with two example files; they (and their
formatted output) constitute the only real documentation. Note that cv
is just a package: you choose the overall formatting by deciding which
class to use, while the package provides the detailed formatting.

