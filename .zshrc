preexec() {
    if [ $(echo $1) != "exit" ]; then
        echo "$$ $SHELL $PWD $EPOCHSECONDS $1" >>"$HOME/.cache/.shell-rich-presence"
    fi
}

precmd() {
    sed -i "" "/^$$/d" "$HOME/.cache/.shell-rich-presence"
}
