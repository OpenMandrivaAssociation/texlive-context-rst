Name:		texlive-context-rst
Version:	0.4
Release:	1
Summary:	Process reStructuredText with ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-rst
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-rst.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-rst.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-context.bin

%description
The package provides a converter and module for typesetting
reStructuredText with ConTeXt. The module uses several lua
scripts in doing its work. Documentation is supplied in rst,
which seems to be readable as text, but...

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-rst.xml
%{_texmfdistdir}/tex/context/third/rst/rst_context.lua
%{_texmfdistdir}/tex/context/third/rst/rst_directives.lua
%{_texmfdistdir}/tex/context/third/rst/rst_helpers.lua
%{_texmfdistdir}/tex/context/third/rst/rst_parser.lua
%{_texmfdistdir}/tex/context/third/rst/rst_setups.lua
%{_texmfdistdir}/tex/context/third/rst/t-rst.mkiv
%doc %{_texmfdistdir}/doc/context/third/rst/COPYING
%doc %{_texmfdistdir}/doc/context/third/rst/README.rst
%doc %{_texmfdistdir}/doc/context/third/rst/documentation.rst
%doc %{_texmfdistdir}/doc/context/third/rst/hybridtest.tex
%doc %{_texmfdistdir}/doc/context/third/rst/inc-first.rst
%doc %{_texmfdistdir}/doc/context/third/rst/inc-second.rst
%doc %{_texmfdistdir}/doc/context/third/rst/inc-third.rst
%doc %{_texmfdistdir}/doc/context/third/rst/inc.tex
%doc %{_texmfdistdir}/doc/context/third/rst/manual.bib
%doc %{_texmfdistdir}/doc/context/third/rst/manual.pdf
%doc %{_texmfdistdir}/doc/context/third/rst/manual.tex
%doc %{_texmfdistdir}/doc/context/third/rst/moduletest.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
