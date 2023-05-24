# inganzamarumpu.zsh-theme

# Borrowing fino-time from these oh-my-zsh themes:

function virtualenv_info {
    [ $VIRTUAL_ENV ] && echo '('`basename $VIRTUAL_ENV`') '
}

function prompt_char {
    git branch >/dev/null 2>/dev/null && echo '>' && return
    echo '>'
}

function box_name {
  local box="${SHORT_HOST:-$HOST}"
  [[ -f ~/.box-name ]] && box="$(< ~/.box-name)"
  echo "${box:gs/%/%%}"
}

PROMPT="╭─[%D{%L:%M:%S}] %{$FG[040]%}%n@$(box_name)%{$reset_color%} %{$terminfo[bold]$fg[blue]%}%~%{$reset_color%} \$(git_prompt_info) \$(ruby_prompt_info)
╰─\$(virtualenv_info)\$(prompt_char) "

ZSH_THEME_GIT_PROMPT_PREFIX="%{$FG[226]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$FG[202]%}✘✘✘"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$FG[040]%}✔ "

ZSH_THEME_RUBY_PROMPT_PREFIX=" %{$FG[239]%}using%{$FG[243]%} ‹"
ZSH_THEME_RUBY_PROMPT_SUFFIX="›%{$reset_color%}"

TMOUT=1

TRAPALRM() {
   zle reset-prompt
}
