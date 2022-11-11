function _try_source() {
    # shellcheck disable=SC1090
    [ -f "$1" ] && source "$1"
}

# Function to source files if they exist
function zshsource() {
    [ -f "$ZDOTDIR/$1" ] && source "$ZDOTDIR/$1"
    _try_source "$ZDOTDIR/$1.zsh"
    _try_source "$ZDOTDIR/$1.plugin.zsh"
    _try_source "$ZDOTDIR/$1.zsh-theme"
}

