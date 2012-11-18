Summary:	The datahub provides passive plugins which insert events into Zeitgeist
Name:		zeitgeist-datahub
Version:	0.9.5
Release:	1
License:	LGPL v3+
Group:		Applications
Source0:	http://launchpad.net/zeitgeist-datahub/0.9/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	b2b76b82b67363c45e5fe4f39a172775
URL:		https://launchpad.net/zeitgeist-datahub
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libzeitgeist-devel
BuildRequires:	pkg-config
BuildRequires:	telepathy-glib-devel
BuildRequires:	vala
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The datahub provides passive plugins which insert events into
Zeitgeist.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%{_sysconfdir}/xdg/autostart/zeitgeist-datahub.desktop
%attr(755,root,root) %{_bindir}/zeitgeist-datahub
%{_mandir}/man1/zeitgeist-datahub.1*

