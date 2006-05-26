Summary:	German resources for Mozilla-firefox
Summary(pl):	Niemieckie pliki jêzykowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-de
Version:	1.5.0.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source0-md5:	579ac08bb4af6022171bc0d50646a88f
URL:		http://www.mozilla.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla-firefox >= %{version}
Requires(post,postun):	textutils
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_libdir}/mozilla-firefox
%define		_chromedir	%{_firefoxdir}/chrome

%description
German resources for Mozilla-firefox.

%description -l pl
Niemieckie pliki jêzykowe dla Mozilli-firefox.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_firefoxdir}/defaults/profile}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/* $RPM_BUILD_ROOT%{_chromedir}
sed -e 's@chrome/de\.jar@de.jar@' $RPM_BUILD_ROOT%{_libdir}/chrome.manifest \
	> $RPM_BUILD_ROOT%{_chromedir}/de.manifest
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_firefoxdir}/defaults/profile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/de.jar
%{_chromedir}/de.manifest
# file conflict:
#%{_firefoxdir}/defaults/profile/*.rdf
