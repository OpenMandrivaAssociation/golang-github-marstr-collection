# Run tests in check section
%bcond_without check

%global goipath         github.com/marstr/collection
Version:                0.3.3

%global common_description %{expand:
Golang Implementation of a few basic data structures.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang Implementation of a few basic data structures
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.3-1
- First package for Fedora

