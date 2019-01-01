# uncrustify.vim
Format source code;

# executable setting
## windows
Do nothing, because this has contain a executable file!

## linux
1. install `uncrustify`;
2. let g:uncrustify_bin_path = 'uncrustify'

# configure setting
## use plugin's configure
Do nothing!

## use your configure
1. define your configure;
2. let g:uncrustify_cfg_path = 'xxx/your_cfg_nam.cfg'

## generate your configure
```bash
# 由于更新uncrustify后，配置可能发生变化，所以需要将你的配置与最新的配置进行合并，所以
# 写了个小脚本
$ cd plugin
$ uncrustify --show-config > defaults.cfg
$ python merge.py
$ mv me.cfg me_old.cfg
$ mv new.cfg me.cfg
```

# useage
1. for whole file, run command: `:Uncrustify`
2. for selected context, run command: `:'<,'>Uncrustify`

# define keymap
* format whole file: `nnoremap <Leader>ff :Uncrustify<CR>`
* format selected context: `vnoremap <Leader>ff :'<,'>Uncrustify<CR>`
