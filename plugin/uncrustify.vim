" =====================================================================
"
" 格式化文件, 自带可执行文件, 自带配置文件, 也可以手动配置执行文件
"
"======================================================================
" 用户可以指定可执行文件或配置文件, 如果不指定, 则使用自带的
if exists("g:uncrustify_bin_path")
    let s:bin_path = g:uncrustify_bin_path
else
    let s:bin_path = expand("<sfile>:p:h") . "/uncrustify"
endif

if exists("g:uncrustify_cfg_path")
    let s:cfg_path = g:uncrustify_cfg_path
else
    let s:cfg_path = expand("<sfile>:p:h") . "/me.cfg"
endif

func! s:Uncrustify(begin, end) range
    let language = (&l:ft == "objc") ? "oc" : &l:ft
    let cmd = s:bin_path . " -q -l " . language . " --frag -c " . s:cfg_path
    execute ":" . a:begin . "," . a:end . "! " . cmd
endfunction
command! -range=% Uncrustify call s:Uncrustify(<line1>,<line2>)
