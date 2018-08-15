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

# useage
1. for whole file, run command: `:Uncrustify`
2. for selected context, run command: `:'<,'>Uncrustify`

# define keymap
* format whole file: `nnoremap <Leader>ff :Uncrustify<CR>`
* format selected context: `vnoremap <Leader>ff :'<,'>Uncrustify<CR>`
