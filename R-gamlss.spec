%global packname  gamlss
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.2.6
Release:          1
Summary:          Generalised Additive Models for Location Scale and Shape
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.2-6.tar.gz

Requires:         R-graphics R-stats R-splines R-utils R-gamlss.dist R-gamlss.data R-nlme 
Requires:         R-MASS R-survival 

BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-graphics R-stats R-splines R-utils R-gamlss.dist R-gamlss.data R-nlme
BuildRequires:    R-MASS R-survival 

%description
The library for fitting GAMLSS models.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
