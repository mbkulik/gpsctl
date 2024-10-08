Name:		gpsctl
Version:	1.19
Release:	1%{?dist}
Summary:	utility program written for U-Blox GPS board

License:	MIT
URL:		https://github.com/philrandal/gpsctl
Source0:	https://github.com/philrandal/gpsctl/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc

%description
This package includes utility program for UBlox GPS board.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" gcc -std=c11 -g *.c -o gpsctl

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m755 -t $RPM_BUILD_ROOT%{_bindir} gpsctl

%files
%{_bindir}/gpsctl

%changelog
* Fri Oct 04 2024 Michael Kulik <mbk@michaelbkulik.com> 1.19-1
- initial release
