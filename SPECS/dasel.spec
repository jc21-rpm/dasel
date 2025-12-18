%define debug_package %{nil}

%global gh_user TomWright

Name:           dasel
Version:        3.1.4
Release:        1%{?dist}
Summary:        Select, put and delete data from JSON, TOML, YAML, XML and CSV files with a single tool
Group:          Applications/System
License:        MIT
URL:            https://daseldocs.tomwright.me/
Source:         https://github.com/%{gh_user}/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  git golang

%description
Say good bye to learning new tools just to work with a different data format.
Dasel uses a standard selector syntax no matter the data format. This means
that once you learn how to use dasel you immediately have the ability to
query/modify any of the supported data types without any additional tools
or effort.

%prep
%setup -q -n %{name}-%{version}

%build
go build \
	-o "%{_builddir}/bin/%{name}" \
	./cmd/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Fri Dec 19 2025 Jamie Curnow <jc@jc21.com> 3.1.4-1
- https://github.com/TomWright/dasel/releases/tag/v3.1.4

* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> 2.7.0-1
- https://github.com/TomWright/dasel/releases/tag/v2.7.0

* Wed Jun 21 2023 Jamie Curnow <jc@jc21.com> 2.3.4-1
- https://github.com/TomWright/dasel/releases/tag/v2.3.4
