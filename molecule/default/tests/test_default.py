def usrbin_binary_installed(host, path_string):
    path = host.file(path_string)
    return path.exists and \
        path.is_file and \
        path.uid == 0 and \
        path.gid == 0 and \
        path.mode == 0o755


def test_htop(host):
    assert usrbin_binary_installed(host, "/usr/bin/htop")


def test_ncdu(host):
    assert usrbin_binary_installed(host, "/usr/bin/ncdu")


def test_neovim(host):
    assert usrbin_binary_installed(host, "/usr/bin/nvim")


def test_rsync(host):
    assert usrbin_binary_installed(host, "/usr/bin/rsync")


def test_tmux(host):
    assert usrbin_binary_installed(host, "/usr/bin/tmux")


def test_vim(host):
    assert usrbin_binary_installed(host, "/usr/bin/vim")


def test_wget(host):
    assert usrbin_binary_installed(host, "/usr/bin/wget")
