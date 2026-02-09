%global real_name nullfs

Name:       %{real_name}-kmod-common
Version:    0.22
Release:    1%{?dist}
Summary:    A virtual file system that behaves like /dev/null
License:    GPLv3+
URL:        https://github.com/abbbi/nullfsvfs
BuildArch:  noarch

Source0:    %{url}/archive/v%{version}.tar.gz#/nullfsvfs-%{version}.tar.gz

Requires:   %{real_name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:   %{real_name}-kmod-common = %{?epoch:%{epoch}:}%{version}

%description
A virtual file system that behaves like /dev/null. It can handle regular file
operations but writing to files does not store any data. The file size is
however saved, so reading from the files behaves like reading from /dev/zero
with a fixed size.

Writing and reading is basically an NOOP, so it can be used for performance
testing with applications that require directory structures.

This package contains common files.
 
%prep
%autosetup -p1 -n nullfsvfs-%{version}

%files
%license LICENSE
%doc README.md

%changelog
* Mon Feb 09 2026 Simone Caronni <negativo17@gmail.com> - 0.22-1
- Update to 0.22.

* Mon Dec 01 2025 Simone Caronni <negativo17@gmail.com> - 0.21-1
- Update to 0.21.

* Wed Jun 18 2025 Simone Caronni <negativo17@gmail.com> - 0.19-1
- Update to 0.19.

* Wed Apr 16 2025 Simone Caronni <negativo17@gmail.com> - 0.18-1
- Update to 0.18.

* Wed Nov 29 2023 Simone Caronni <negativo17@gmail.com> - 0.17-1
- First build.

