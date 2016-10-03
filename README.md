# uncrustify.vim
Format source code;

# executable setting
## windows
Do nothing!

## linux
1. install `uncrustify`;
2. let g:uncrustify_bin_path = 'uncrustify'

# configure setting
## use plugin's configure
Do nothing!
## use your configure
1. define your configure;
2. let g:uncrustify_cfg_path = 'xxx/your_cfg_nam.cfg'

# command
chinese: 支持范围格式化
english: support format in a range!

command: `Uncrustify`

# useage
1. for whole file, run command
    `:Uncrustify`

2. for selected context, run command
    ```
    :'<,'>Uncrustify
    ```

# define keymap
* format whole file: nnoremap <Leader>ff :Uncrustify<CR>
* format selected context: nnoremap <Leader>fr :'<,'>Uncrustify<CR>
