# 2016.10.11 22:17:49 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/macpath.py
"""Pathname and path-related operations for the Macintosh."""
import os
import warnings
from stat import *
import genericpath
from genericpath import *
__all__ = ['normcase',
 'isabs',
 'join',
 'splitdrive',
 'split',
 'splitext',
 'basename',
 'dirname',
 'commonprefix',
 'getsize',
 'getmtime',
 'getatime',
 'getctime',
 'islink',
 'exists',
 'lexists',
 'isdir',
 'isfile',
 'walk',
 'expanduser',
 'expandvars',
 'normpath',
 'abspath',
 'curdir',
 'pardir',
 'sep',
 'pathsep',
 'defpath',
 'altsep',
 'extsep',
 'devnull',
 'realpath',
 'supports_unicode_filenames']
curdir = ':'
pardir = '::'
extsep = '.'
sep = ':'
pathsep = '\n'
defpath = ':'
altsep = None
devnull = 'Dev:Null'

def normcase(path):
    return path.lower()


def isabs(s):
    """Return true if a path is absolute.
    On the Mac, relative paths begin with a colon,
    but as a special case, paths with no colons at all are also relative.
    Anything else is absolute (the string up to the first colon is the
    volume name)."""
    return ':' in s and s[0] != ':'


def join(s, *p):
    path = s
    for t in p:
        if not s or isabs(t):
            path = t
            continue
        if t[:1] == ':':
            t = t[1:]
        if ':' not in path:
            path = ':' + path
        if path[-1:] != ':':
            path = path + ':'
        path = path + t

    return path


def split(s):
    """Split a pathname into two parts: the directory leading up to the final
    bit, and the basename (the filename, without colons, in that directory).
    The result (s, t) is such that join(s, t) yields the original argument."""
    if ':' not in s:
        return ('', s)
    colon = 0
    for i in range(len(s)):
        if s[i] == ':':
            colon = i + 1

    path, file = s[:colon - 1], s[colon:]
    if path and ':' not in path:
        path = path + ':'
    return (path, file)


def splitext(p):
    return genericpath._splitext(p, sep, altsep, extsep)


splitext.__doc__ = genericpath._splitext.__doc__

def splitdrive(p):
    """Split a pathname into a drive specification and the rest of the
    path.  Useful on DOS/Windows/NT; on the Mac, the drive is always
    empty (don't use the volume name -- it doesn't have the same
    syntactic and semantic oddities as DOS drive letters, such as there
    being a separate current directory per drive)."""
    return ('', p)


def dirname(s):
    return split(s)[0]


def basename(s):
    return split(s)[1]


def ismount(s):
    if not isabs(s):
        return False
    components = split(s)
    return len(components) == 2 and components[1] == ''


def islink(s):
    """Return true if the pathname refers to a symbolic link."""
    try:
        import Carbon.File
        return Carbon.File.ResolveAliasFile(s, 0)[2]
    except:
        return False


def lexists(path):
    """Test whether a path exists.  Returns True for broken symbolic links"""
    try:
        st = os.lstat(path)
    except os.error:
        return False

    return True


def expandvars(path):
    """Dummy to retain interface-compatibility with other operating systems."""
    return path


def expanduser(path):
    """Dummy to retain interface-compatibility with other operating systems."""
    return path


class norm_error(Exception):
    """Path cannot be normalized"""
    pass


def normpath(s):
    """Normalize a pathname.  Will return the same result for
    equivalent paths."""
    if ':' not in s:
        return ':' + s
    comps = s.split(':')
    i = 1
    while i < len(comps) - 1:
        if comps[i] == '' and comps[i - 1] != '':
            if i > 1:
                del comps[i - 1:i + 1]
                i = i - 1
            else:
                raise norm_error, 'Cannot use :: immediately after volume name'
        else:
            i = i + 1

    s = ':'.join(comps)
    if s[-1] == ':' and len(comps) > 2 and s != ':' * len(s):
        s = s[:-1]
    return s


def walk(top, func, arg):
    """Directory tree walk with callback function.
    
    For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'), call func(arg, dirname, fnames).
    dirname is the name of the directory, and fnames a list of the names of
    the files and subdirectories in dirname (excluding '.' and '..').  func
    may modify the fnames list in-place (e.g. via del or slice assignment),
    and walk will only recurse into the subdirectories whose names remain in
    fnames; this can be used to implement a filter, or to impose a specific
    order of visiting.  No semantics are defined for, or required of, arg,
    beyond that arg is always passed to func.  It can be used, e.g., to pass
    a filename pattern, or a mutable object designed to accumulate
    statistics.  Passing None for arg is common."""
    warnings.warnpy3k('In 3.x, os.path.walk is removed in favor of os.walk.', stacklevel=2)
    try:
        names = os.listdir(top)
    except os.error:
        return

    func(arg, top, names)
    for name in names:
        name = join(top, name)
        if isdir(name) and not islink(name):
            walk(name, func, arg)


def abspath(path):
    """Return an absolute path."""
    if not isabs(path):
        if isinstance(path, unicode):
            cwd = os.getcwdu()
        else:
            cwd = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


def realpath(path):
    path = abspath(path)
    try:
        import Carbon.File
    except ImportError:
        return path

    if not path:
        return path
    components = path.split(':')
    path = components[0] + ':'
    for c in components[1:]:
        path = join(path, c)
        try:
            path = Carbon.File.FSResolveAliasFile(path, 1)[0].as_pathname()
        except Carbon.File.Error:
            pass

    return path


supports_unicode_filenames = True
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\macpath.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:17:49 St�edn� Evropa (letn� �as)
