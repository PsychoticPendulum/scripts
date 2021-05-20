" |-------------------------------------------------------------------------|
" |  ____                 _     _      ____                        _        |
" | |  _ \ ___ _   _  ___| |__ (_) ___|  _ \ ___ _ __   __ _ _   _(_)_ __   |
" | | |_) / __| | | |/ __| '_ \| |/ __| |_) / _ \ '_ \ / _` | | | | | '_ \  |
" | |  __/\__ \ |_| | (__| | | | | (__|  __/  __/ | | | (_| | |_| | | | | | |
" | |_|   |___/\__, |\___|_| |_|_|\___|_|   \___|_| |_|\__, |\__,_|_|_| |_| |
" |           |___/                                   |___/                 |
" |-------------------------------------------------------------------------| 

if &compatible
  set nocompatible
endif

set backspace=indent,eol,start
set ruler
set suffixes+=.aux,.bbl,.blg,.brf,.cb,.dvi,.idx,.ilg,.ind,.inx,.jpg,.log,.out,.png,.toc
set suffixes-=.h
set suffixes-=.obj

set number relativenumber
set autoindent
syntax enable

set ic
" set hlsearch!

" Move temporary files to a secure location to protect against CVE-2017-1000382
if exists('$XDG_CACHE_HOME')
  let &g:directory=$XDG_CACHE_HOME
else
  let &g:directory=$HOME . '/.cache'
endif
let &g:undodir=&g:directory . '/vim/undo//'
let &g:backupdir=&g:directory . '/vim/backup//'
let &g:directory.='/vim/swap//'
" Create directories if they doesn't exist
if ! isdirectory(expand(&g:directory))
  silent! call mkdir(expand(&g:directory), 'p', 0700)
endif
if ! isdirectory(expand(&g:backupdir))
  silent! call mkdir(expand(&g:backupdir), 'p', 0700)
endif
if ! isdirectory(expand(&g:undodir))
  silent! call mkdir(expand(&g:undodir), 'p', 0700)
endif

" Make shift-insert work like in Xterm
if has('gui_running')
  map <S-Insert> <MiddleMouse>
  map! <S-Insert> <MiddleMouse>
endif
