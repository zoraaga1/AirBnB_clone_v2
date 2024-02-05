# 101-setup_web_static.pp
class web_static_setup {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/data':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static':
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
  }

  file { '/data/web_static/releases/test':
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
  }

  file { '/data/web_static/shared':
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    owner   => 'root',
    group   => 'root',
    content => 'Test content...',
  }

  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
    owner  => 'root',
    group  => 'root',
  }

  file_line { 'nginx_hbnb_static':
    path    => '/etc/nginx/sites-available/default',
    line    => '    location /hbnb_static/ {',
    match   => '^}',
    after   => 'server_name _;',
    notify  => Service['nginx'],
  }
}

include web_static_setup
